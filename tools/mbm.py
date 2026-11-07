#!/usr/bin/env python3
"""Archivos de mensajes de IVA (.mbm, formato MSG2).

    python3 tools/mbm.py roundtrip ROMFS        lee y reescribe todos, sin cambios, y compara
    python3 tools/mbm.py export ROMFS SALIDA    todos los mensajes a un JSONL
    python3 tools/mbm.py apply ROMFS TEXTOS.jsonl SALIDA
                                                escribe en SALIDA los archivos con los textos
                                                {key, es} de TEXTOS.jsonl

Formato (deducido del juego; lo que no se entiende se copia tal cual):
  0x00  u32 0, "MSG2", u32 0x10000, u32 tamaño (en 631 de 1243 archivos no coincide
        con el largo y el juego anda igual), u32 cantidad,
        u32 inicio de la tabla (0x20), 8 bytes en cero
  tabla: cantidad × (u32 id, u32 tamaño, u32 posición, u32 0); tamaño 0 = vacía
  textos: palabras de 16 bits big-endian; un carácter Shift-JIS de doble byte,
        o un código F8xx, o FFFF (fin del mensaje)
  Entre la tabla y el primer texto puede haber relleno, y después del último
  texto puede haber restos de otra versión; los dos se conservan.

En el texto exportado, el inglés de ancho completo (Ｔｈｅ) se ve como ASCII
(The) y el espacio ideográfico como espacio. Las letras españolas usan los
códigos de `letras.py`. Toda palabra que no sea un carácter de doble byte se
escribe como {XXXX}.
"""
import json
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letras import ESPANOL, POR_CODIGO  # noqa: E402

TAG = re.compile(r"\{([0-9A-F]{4})\}")


def to_text(raw):
    out = []
    for j in range(0, len(raw), 2):
        w = raw[j:j + 2]
        if w[0] == 0xF8 or w == b"\xff\xff":
            out.append("{%s}" % w.hex().upper())
            continue
        if w[0] << 8 | w[1] in POR_CODIGO:
            out.append(POR_CODIGO[w[0] << 8 | w[1]])
            continue
        try:
            c = w.decode("cp932")
        except UnicodeDecodeError:
            c = ""
        if len(c) != 1 or c.encode("cp932") != w or c in "{}":
            out.append("{%s}" % w.hex().upper())
        elif c == "　":
            out.append(" ")
        elif "！" <= c <= "～":
            out.append(chr(ord(c) - 0xFEE0))
        else:
            out.append(c)
    return "".join(out)


def from_text(s):
    out = bytearray()
    pos = 0
    for m in TAG.finditer(s):
        out += _chars(s[pos:m.start()])
        out += bytes.fromhex(m.group(1))
        pos = m.end()
    out += _chars(s[pos:])
    return bytes(out)


def _chars(s):
    out = bytearray()
    for c in s:
        if c in ESPANOL:
            out += ESPANOL[c].to_bytes(2, "big")
            continue
        if c == " ":
            c = "　"
        elif "!" <= c <= "~":
            c = chr(ord(c) + 0xFEE0)
        b = c.encode("cp932")
        if len(b) != 2:
            raise ValueError(f"carácter sin codificar: {c!r}")
        out += b
    return bytes(out)


class Mbm:
    def __init__(self, data):
        if data[4:8] != b"MSG2":
            raise ValueError("no es MSG2")
        self.header = data[:0x20]
        # el campo de tamaño se actualiza solo si coincidía con el largo del archivo
        self.size_ok = struct.unpack_from("<I", data, 0x0C)[0] == len(data)
        count, table = struct.unpack_from("<II", data, 0x10)
        self.table = table
        self.entries = [list(struct.unpack_from("<IIII", data, table + 16 * i)) for i in range(count)]
        live = sorted((e for e in self.entries if e[1]), key=lambda e: e[2])
        table_end = table + 16 * count
        start = live[0][2] if live else table_end
        self.pad = data[table_end:start]
        pos = start
        for e in live:
            if e[2] != pos:
                raise ValueError(f"hueco entre textos en {pos:#x}")
            pos += e[1]
        self.tail = data[pos:]
        # texto de cada entrada, en el orden en que están guardados
        self.order = [self.entries.index(e) for e in live]
        self.texts = {i: to_text(data[self.entries[i][2]:self.entries[i][2] + self.entries[i][1]])
                      for i in self.order}

    def build(self):
        blobs = {i: from_text(self.texts[i]) for i in self.order}
        pos = self.table + 16 * len(self.entries) + len(self.pad)
        entries = [e[:] for e in self.entries]
        for i in self.order:
            entries[i][1], entries[i][2] = len(blobs[i]), pos
            pos += len(blobs[i])
        out = bytearray(self.header)
        for e in entries:
            out += struct.pack("<IIII", *e)
        out += self.pad
        for i in self.order:
            out += blobs[i]
        out += self.tail
        if self.size_ok:
            struct.pack_into("<I", out, 0x0C, len(out))
        return bytes(out)


def roundtrip(root):
    files = sorted(Path(root).rglob("*.mbm"))
    fails = 0
    for p in files:
        data = p.read_bytes()
        try:
            same = Mbm(data).build() == data
        except ValueError as e:
            same = False
            print(f"{p.relative_to(root)}: {e}")
        if not same:
            fails += 1
            print(f"DISTINTO: {p.relative_to(root)}")
    print(f"{len(files) - fails} de {len(files)} archivos idénticos")
    return fails == 0


def export(root, out):
    n = 0
    with open(out, "w", encoding="utf-8") as w:
        for p in sorted(Path(root).rglob("*.mbm")):
            m = Mbm(p.read_bytes())
            rel = p.relative_to(root).as_posix()
            for i in sorted(m.order):
                w.write(json.dumps({"key": f"{rel}#{m.entries[i][0]}", "en": m.texts[i]},
                                   ensure_ascii=False) + "\n")
                n += 1
    print(f"{n} mensajes en {out}")


def leer_textos(archivos):
    """{key, es} de uno o más JSONL → {archivo .mbm: {id: texto}}; los últimos pisan a los primeros."""
    cambios = {}
    for jsonl in archivos:
        for n, linea in enumerate(open(jsonl, encoding="utf-8"), 1):
            if not linea.strip():
                continue
            d = json.loads(linea)
            rel, ident = d["key"].rsplit("#", 1)
            if not d["es"].endswith("{FFFF}"):
                raise ValueError(f"{jsonl}:{n}: el texto debe terminar en {{FFFF}}")
            cambios.setdefault(rel, {})[int(ident)] = d["es"]
    return cambios


def aplicar(original, textos, nombre="?"):
    """Bytes de un .mbm + {id: texto} → bytes del .mbm con esos textos."""
    m = Mbm(original)
    por_id = {m.entries[i][0]: i for i in m.order}
    for ident, es in textos.items():
        if ident not in por_id:
            raise ValueError(f"{nombre}#{ident}: ese mensaje no existe")
        m.texts[por_id[ident]] = es
    return m.build()


def apply(root, jsonl, out):
    """Escribe en `out` los .mbm de `root` con los textos {key, es} de `jsonl`."""
    root, out = Path(root), Path(out)
    for rel, textos in sorted(leer_textos([jsonl]).items()):
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(aplicar((root / rel).read_bytes(), textos, rel))
        print(f"{rel}: {len(textos)} mensajes")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "roundtrip":
        sys.exit(0 if roundtrip(sys.argv[2]) else 1)
    if len(sys.argv) >= 4 and sys.argv[1] == "export":
        export(sys.argv[2], sys.argv[3])
        return
    if len(sys.argv) >= 5 and sys.argv[1] == "apply":
        apply(sys.argv[2], sys.argv[3], sys.argv[4])
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
