#!/usr/bin/env python3
"""Términos oficiales de SMT V: Vengeance (inglés → español) para el glosario.

    python3 tools/smt5v.py candidates [--paks CARPETA] [--out SALIDA.tsv]

Lee las tablas de nombres de SMT V en inglés y en español (habilidades,
objetos, personajes y demonios, razas, estados), las empareja por posición
(cada idioma tiene las mismas entradas en el mismo orden) y busca cada término
inglés en los textos de IVA (los JSONL de `mbm.py export` y `tbb.py export`).
Escribe un TSV con: inglés, español oficial, tabla de SMT V, veces en IVA.
Lo extraído es texto de otro juego: el TSV queda fuera del repo.

Los paquetes de SMT V vienen comprimidos con Oodle. Se descomprimen con ooz,
de código abierto, compilado en cada equipo con `tools/build_ooz.sh` (no va
en el repo). Por defecto se busca en ../smt4a-local/ooz/libooz.so.
"""
import argparse
import ctypes
import json
import os
import re
import struct
import sys
import zlib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOCAL = REPO.parent / "smt4a-local"
PAKS = Path("/mnt/c/Steam/steamapps/common/SMT5V/Project/Content/Paks")
OOZ = LOCAL / "ooz" / "libooz.so"
BINTABLE = "Project/Content/L10N/{lang}/Blueprints/Gamedata/BinTable/"
TABLES = {
    "habilidad": "Battle/Skill/SkillName.uexp",
    "objeto": "Item/ItemName.uexp",
    "personaje": "Common/CharacterName.uexp",
    "raza": "Common/DevilRace.uexp",
    "estado": "Camp/Status/StatusConditionName.uexp",
}
GUID = re.compile(r"^[0-9A-F]{32}$")


# ---------- paquetes de Unreal Engine 4 (versión 11, índice sin cifrar) ----------

def _fstring(b, o):
    n = struct.unpack_from("<i", b, o)[0]
    o += 4
    if n == 0:
        return "", o
    if n < 0:
        return b[o:o - 2 * n].decode("utf-16-le").rstrip("\0"), o - 2 * n
    return b[o:o + n].decode("utf-8", "replace").rstrip("\0"), o + n


def pak_index(path):
    """{ruta: (compresión, posición, tamaño descomprimido)} de un .pak."""
    with open(path, "rb") as f:
        size = os.path.getsize(path)
        f.seek(size - 512)
        tail = f.read(512)
        k = tail.rfind(struct.pack("<I", 0x5A6F12E1))
        _, ioff, isz = struct.unpack_from("<IQQ", tail, k + 4)
        methods = [tail[k + 44 + 32 * i:k + 76 + 32 * i].rstrip(b"\0").decode() for i in range(5)]
        f.seek(ioff)
        idx = f.read(isz)
        mount, o = _fstring(idx, 0)
        o += 12                                        # cantidad de entradas, semilla
        if struct.unpack_from("<i", idx, o)[0]:
            o += 4 + 36
        else:
            o += 4
        o += 4                                         # hay índice de directorios
        fdi_off, fdi_size = struct.unpack_from("<qq", idx, o)
        o += 36
        enc_size = struct.unpack_from("<i", idx, o)[0]
        enc = idx[o + 4:o + 4 + enc_size]
        f.seek(fdi_off)
        fdi = f.read(fdi_size)
    out = {}
    p = 4
    for _ in range(struct.unpack_from("<i", fdi, 0)[0]):
        d, p = _fstring(fdi, p)
        nf = struct.unpack_from("<i", fdi, p)[0]
        p += 4
        for _ in range(nf):
            name, p = _fstring(fdi, p)
            eo = struct.unpack_from("<i", fdi, p)[0]
            p += 4
            if eo < 0:
                continue
            v = struct.unpack_from("<I", enc, eo)[0]
            q = eo + 4 + (4 if v & 0x3F == 0x3F else 0)
            method = (v >> 23) & 0x3F

            def rd(safe):
                nonlocal q
                fmt, n = ("<I", 4) if safe else ("<Q", 8)
                x = struct.unpack_from(fmt, enc, q)[0]
                q += n
                return x
            off = rd(v >> 31 & 1)
            usize = rd(v >> 30 & 1)
            path_in = (mount + d + name).replace("../../../", "")
            out[path_in] = (methods[method - 1] if method else "", off, usize)
    return out


class Paks:
    def __init__(self, folder=PAKS, ooz=OOZ):
        self.folder = Path(folder)
        self.index = {}
        for pak in sorted(self.folder.glob("*.pak")):
            for k, v in pak_index(pak).items():
                self.index[k] = (pak,) + v
        self._kd = None
        self.ooz = Path(ooz)

    def _oodle(self, src, usize):
        if self._kd is None:
            if not self.ooz.exists():
                sys.exit(f"No encuentro {self.ooz}; compílalo con tools/build_ooz.sh")
            lib = ctypes.CDLL(str(self.ooz))
            self._kd = getattr(lib, "_Z17Kraken_DecompressPKhmPhm")
            self._kd.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t]
            self._kd.restype = ctypes.c_int
        dst = ctypes.create_string_buffer(usize + 64)
        if self._kd(src, len(src), dst, usize) != usize:
            raise ValueError("Oodle no pudo descomprimir el bloque")
        return dst.raw[:usize]

    def read(self, path):
        pak, method, off, usize = self.index[path]
        with open(pak, "rb") as f:
            f.seek(off)
            h = f.read(64 * 1024)
            cm = struct.unpack_from("<I", h, 24)[0]
            p = 48
            if cm == 0:
                f.seek(off + p + 5)
                return f.read(usize)
            count = struct.unpack_from("<I", h, p)[0]
            p += 4
            blocks = [struct.unpack_from("<qq", h, p + 16 * i) for i in range(count)]
            p += 16 * count
            flags, bsize = struct.unpack_from("<BI", h, p)
            if flags & 1:
                raise ValueError(f"{path}: cifrado")
            out, left = bytearray(), usize
            for a, b in blocks:
                f.seek(off + a)
                src = f.read(b - a)
                n = min(bsize, left)
                out += self._oodle(src, n) if method == "Oodle" else zlib.decompress(src)
                left -= n
            return bytes(out)


# ---------- tablas de textos ----------

def fstrings(b):
    """Todas las cadenas de un .uexp (UTF-8 o UTF-16), en orden."""
    out, p = [], 0
    while p + 4 <= len(b):
        n = struct.unpack_from("<i", b, p)[0]
        if 0 < n < 4096 and p + 4 + n <= len(b) and b[p + 3 + n] == 0:
            try:
                s = b[p + 4:p + 3 + n].decode("utf-8")
                if s and all(c >= " " or c in "\n\r\t" for c in s):
                    out.append(s)
                    p += 4 + n
                    continue
            except UnicodeDecodeError:
                pass
        if -4096 < n < 0 and p + 4 - 2 * n <= len(b) and b[p + 2 - 2 * n:p + 4 - 2 * n] == b"\0\0":
            try:
                s = b[p + 4:p + 2 - 2 * n].decode("utf-16-le")
                if s:
                    out.append(s)
                    p += 4 - 2 * n
                    continue
            except UnicodeDecodeError:
                pass
        p += 1
    return out


def texts(paks, table, lang):
    return [s for s in fstrings(paks.read(BINTABLE.format(lang=lang) + table)) if not GUID.match(s)]


def official_pairs(paks):
    """[(inglés, español, tabla)] sin repetir y sin entradas sin uso."""
    seen, out = set(), []
    for kind, table in TABLES.items():
        en, es = texts(paks, table, "en"), texts(paks, table, "es")
        if len(en) != len(es):
            print(f"aviso: {table} tiene {len(en)} entradas en inglés y {len(es)} en español", file=sys.stderr)
        for a, b in zip(en, es):
            a, b = a.strip(), b.strip()
            if not a or a.startswith("NOT USED") or a in ("-", "?", "???") or (a, b) in seen:
                continue
            seen.add((a, b))
            out.append((a, b, kind))
    return out


def iva_texts():
    out = []
    for name in ("en.jsonl", "tbb.jsonl"):
        path = LOCAL / name
        if path.exists():
            out += [json.loads(line)["en"] for line in open(path, encoding="utf-8")]
    return out


def candidates(paks, out):
    pairs = official_pairs(paks)
    big = "\n".join(iva_texts())
    rows = []
    for en, es, kind in pairs:
        if len(en) < 2:
            continue
        n = len(re.findall(rf"(?<![A-Za-z]){re.escape(en)}(?![A-Za-z])", big))
        if n:
            rows.append((en, es, kind, n))
    rows.sort(key=lambda r: (-r[3], r[0]))
    with open(out, "w", encoding="utf-8") as w:
        w.write("en\tes_smtv\ttabla\tveces_en_iva\n")
        for r in rows:
            w.write("\t".join(map(str, r)) + "\n")
    by_kind = {}
    for r in rows:
        by_kind[r[2]] = by_kind.get(r[2], 0) + 1
    print(f"{len(pairs)} términos oficiales; {len(rows)} aparecen en IVA {by_kind} → {out}")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("command", choices=["candidates"])
    a.add_argument("--paks", default=str(PAKS))
    a.add_argument("--ooz", default=str(OOZ))
    a.add_argument("--out", default=str(LOCAL / "glossary-candidates.tsv"))
    args = a.parse_args()
    candidates(Paks(args.paks, args.ooz), args.out)


if __name__ == "__main__":
    main()
