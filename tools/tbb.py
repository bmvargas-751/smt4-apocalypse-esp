#!/usr/bin/env python3
"""Tablas de IVA (.tbb): nombres y textos cortos en campos de largo fijo.

    python3 tools/tbb.py roundtrip ROMFS        reescribe todos los textos, sin cambios, y compara
    python3 tools/tbb.py export ROMFS SALIDA    los textos a un JSONL {key, max, en}
    python3 tools/tbb.py columns ROMFS          las columnas de texto de cada tabla

Formato (deducido del juego):
  "TBCR", u32 tamaño de la cabecera, u32 cantidad de tablas, u32 0,
  u32 × (cantidad - 1) posiciones de las tablas 2..n, relativas al fin de la
  cabecera (la primera empieza ahí mismo).
  Cada tabla: "TBL1", u32 tamaño de los datos, u32 tamaño del registro (0 = un
  solo bloque), u32 16; después los registros.

Los textos no tienen esquema: se detectan como columnas, es decir, una
posición del registro donde casi todos los registros tienen un texto terminado
en cero. El espacio de cada texto llega hasta el primer byte no cero de
cualquier registro después de su texto, o hasta la columna siguiente.

Clave de cada texto: «archivo#tabla.registro.posición». `max` es el largo
máximo en bytes, sin el cero final. Las letras españolas ocupan 2 bytes (los
códigos de `letters.py`); el resto del ASCII, 1. Un salto de línea es \\n.
"""
import json
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letters import BY_CODE, SPANISH  # noqa: E402

TEXT_BYTES = set(range(0x20, 0x7F)) | {0x0A}
EXCLUDED = ("test/",)                 # tablas de prueba de los desarrolladores
GOOD = re.compile(rb"[A-Za-z]{2}|[\x81-\x9f\xe0-\xef][\x40-\xfc]")   # letras, o japonés de 2 bytes
IDENT = re.compile(r"^[A-Za-z0-9_.\-]*$")
JAPANESE = re.compile("[\u3040-\u30ff\u4e00-\u9fff]")


def decode(raw):
    """Shift-JIS con las letras españolas; ValueError si no es texto válido."""
    out, i = [], 0
    while i < len(raw):
        c = raw[i]
        if c < 0x80 or 0xA1 <= c <= 0xDF:
            out.append(raw[i:i + 1].decode("cp932"))
            i += 1
            continue
        if i + 1 >= len(raw):
            raise ValueError("carácter cortado")
        code = c << 8 | raw[i + 1]
        out.append(BY_CODE.get(code) or raw[i:i + 2].decode("cp932"))
        i += 2
    return "".join(out)


def encode(s):
    out = bytearray()
    for c in s:
        if c in SPANISH:
            out += SPANISH[c].to_bytes(2, "big")
        else:
            out += c.encode("cp932")
    return bytes(out)


def text_at(rec, o):
    """El texto que empieza en `o` (bytes hasta el cero), o None si no parece texto."""
    e = rec.find(b"\0", o)
    if e < 0:
        return None
    s = rec[o:e]
    if all(c in TEXT_BYTES for c in s):
        return s
    if all(c >= 0x20 or c == 0x0A for c in s):
        try:
            text = decode(s)
        except (ValueError, UnicodeError):
            return None
        if any("\uff61" <= ch <= "\uff9f" for ch in text):
            return None                       # katakana de un byte: son datos, no texto
        return s if encode(text) == s else None
    return None


class Tbb:
    def __init__(self, data):
        if data[:4] != b"TBCR":
            raise ValueError("no es TBCR")
        self.data = bytearray(data)
        hdr, count = struct.unpack_from("<II", data, 4)
        rel = [0] + list(struct.unpack_from(f"<{count - 1}I", data, 16)) if count > 1 else [0]
        self.tables = []                      # (posición de los datos, tamaño, tamaño del registro)
        for r in rel:
            o = hdr + r
            if data[o:o + 4] != b"TBL1":
                raise ValueError(f"tabla sin TBL1 en {o:#x}")
            size, rec, th = struct.unpack_from("<III", data, o + 4)
            self.tables.append((o + th, size, rec))
        self._fields = None

    def records(self, t):
        start, size, rec = self.tables[t]
        if rec == 0:
            return [(start, size)]
        return [(start + k * rec, rec) for k in range(size // rec)]

    def fields(self):
        """{(tabla, registro, posición): (capacidad en bytes con el cero, texto)}."""
        if self._fields is not None:
            return self._fields
        found = {}
        for t in range(len(self.tables)):
            recs = [bytes(self.data[a:a + n]) for a, n in self.records(t)]
            if not recs:
                continue
            width = len(recs[0])
            cand = []
            for o in range(width):
                vals = [text_at(r, o) for r in recs]
                valid = [v for v in vals if v is not None]
                good = sum(1 for v in valid if len(v) >= 3 and GOOD.search(v))
                if not good or len(valid) < max(1, 0.9 * len(recs)) or good < 0.2 * len(valid):
                    continue
                if o > 0:
                    inside = sum(1 for r, v in zip(recs, vals) if v and (r[o - 1] in TEXT_BYTES or r[o - 1] >= 0x80))
                    if inside > 0.5 * sum(1 for v in vals if v):
                        continue                 # está a mitad de un texto, no al principio
                cand.append(o)
            starts = [o for o in cand if o - 1 not in cand]
            for i, o in enumerate(starts):
                nxt = starts[i + 1] if i + 1 < len(starts) else width
                bound, longest = nxt, 0
                for r in recs:
                    v = text_at(r, o)
                    if v is not None:
                        e = o + len(v) + 1
                        longest = max(longest, len(v) + 1)
                        bound = min(bound, next((k for k in range(e, nxt) if r[k]), nxt))
                if longest > nxt - o:
                    continue                  # un texto pisa la columna siguiente: no es un campo
                # si un registro ya usa esos bytes para su texto, en los demás también son del campo
                bound = max(bound, longest)
                for k, r in enumerate(recs):
                    v = text_at(r, o)
                    if v:
                        found[(t, k, o)] = (bound - o, decode(v))
        self._fields = found
        return found

    def set_text(self, key, text):
        cap, _ = self.fields()[key]
        raw = encode(text)
        if len(raw) + 1 > cap:
            raise ValueError(f"{key}: {len(raw)} bytes, el máximo es {cap - 1}")
        t, k, o = key
        a, _ = self.records(t)[k]
        self.data[a + o:a + o + cap] = raw + bytes(cap - len(raw))

    def build(self):
        return bytes(self.data)


def key_str(rel, key):
    return f"{rel}#{key[0]}.{key[1]}.{key[2]}"


def parse_key(s):
    rel, k = s.rsplit("#", 1)
    return rel, tuple(int(x) for x in k.split("."))


def is_identifier(t):
    return bool(IDENT.match(t)) and bool(re.search(r"[_\d]|[a-z][A-Z]", t) or t.islower() or t.isupper())


def column_kind(texts):
    """«id» si es una columna de nombres internos (archivos, etiquetas); si no, «texto»."""
    return "id" if sum(map(is_identifier, texts)) >= 0.8 * len(texts) else "texto"


def text_fields(tbb, kind="texto"):
    """Campos por tipo: «texto» (lo que ve el jugador, en inglés), «ja» (textos en japonés
    de columnas de texto) o «id» (columnas de nombres internos)."""
    cols = {}
    for (t, k, o), (cap, text) in tbb.fields().items():
        cols.setdefault((t, o), []).append(((t, k, o), cap, text))
    out = {}
    for items in cols.values():
        col = column_kind([x[2] for x in items])
        for key, cap, text in items:
            k = col if col == "id" else ("ja" if JAPANESE.search(text) else "texto")
            if k == kind:
                out[key] = (cap, text)
    return out


def apply_texts(original, texts, name="?"):
    """Bytes de un .tbb + {(tabla, registro, posición): texto} → bytes con esos textos."""
    tbb = Tbb(original)
    for key, es in texts.items():
        where = f"{name}#{'.'.join(map(str, key))}"
        if key not in tbb.fields():
            raise ValueError(f"{where}: ese texto no existe")
        cap = tbb.fields()[key][0]
        if len(encode(es)) + 1 > cap:
            raise ValueError(f"{where}: «{es}» ocupa {len(encode(es))} bytes y el máximo es {cap - 1}")
        tbb.set_text(key, es)
    return tbb.build()


def roundtrip(root):
    root = Path(root)
    files = sorted(root.rglob("*.tbb"))
    fails = 0
    for p in files:
        data = p.read_bytes()
        tbb = Tbb(data)
        for key, (_, text) in tbb.fields().items():
            tbb.set_text(key, text)
        if tbb.build() != data:
            fails += 1
            print(f"DISTINTO: {p.relative_to(root)}")
    print(f"{len(files) - fails} de {len(files)} archivos idénticos")
    return fails == 0


def export(root, out):
    root = Path(root)
    n = 0
    with open(out, "w", encoding="utf-8") as w:
        for p in sorted(root.rglob("*.tbb")):
            rel = p.relative_to(root).as_posix()
            if rel.startswith(EXCLUDED):
                continue
            for key, (cap, text) in sorted(text_fields(Tbb(p.read_bytes())).items()):
                w.write(json.dumps({"key": key_str(rel, key), "max": cap - 1, "en": text},
                                   ensure_ascii=False) + "\n")
                n += 1
    print(f"{n} textos en {out}")


def columns(root):
    root = Path(root)
    for p in sorted(root.rglob("*.tbb")):
        rel = p.relative_to(root).as_posix()
        tbb = Tbb(p.read_bytes())
        cols = {}
        for (t, k, o), (cap, text) in tbb.fields().items():
            cols.setdefault((t, o), []).append((cap, text))
        for (t, o), items in sorted(cols.items()):
            texts = [x[1] for x in items]
            kind = column_kind(texts)
            if kind == "texto" and sum(1 for x in texts if JAPANESE.search(x)) >= 0.5 * len(texts):
                kind = "ja"
            sample = " | ".join(sorted(set(texts), key=len, reverse=True)[:2]).replace("\n", "⏎")
            print(f"{kind:5} {rel}#{t}.*.{o} máx {items[0][0] - 1} ×{len(items)} :: {sample[:90]}")


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "roundtrip":
        sys.exit(0 if roundtrip(a[1]) else 1)
    if len(a) >= 3 and a[0] == "export":
        export(a[1], a[2])
        return
    if len(a) >= 2 and a[0] == "columns":
        columns(a[1])
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
