#!/usr/bin/env python3
"""Archivos de mensajes de IVA (.mbm, formato MSG2).

    python3 tools/mbm.py roundtrip ROMFS        lee y reescribe todos, sin cambios, y compara
    python3 tools/mbm.py export ROMFS SALIDA    todos los mensajes a un JSONL

Formato (deducido del juego; lo que no se entiende se copia tal cual):
  0x00  u32 0, "MSG2", u32 0x10000, u32 tamaño (no siempre coincide), u32 cantidad,
        u32 inicio de la tabla (0x20), 8 bytes en cero
  tabla: cantidad × (u32 id, u32 tamaño, u32 posición, u32 0); tamaño 0 = vacía
  textos: palabras de 16 bits big-endian; un carácter Shift-JIS de doble byte,
        o un código F8xx, o FFFF (fin del mensaje)
  Entre la tabla y el primer texto puede haber relleno, y después del último
  texto puede haber restos de otra versión; los dos se conservan.

En el texto exportado, el inglés de ancho completo (Ｔｈｅ) se ve como ASCII
(The) y el espacio ideográfico como espacio. Toda palabra que no sea un
carácter de doble byte se escribe como {XXXX}.
"""
import json
import re
import struct
import sys
from pathlib import Path

TAG = re.compile(r"\{([0-9A-F]{4})\}")


def to_text(raw):
    out = []
    for j in range(0, len(raw), 2):
        w = raw[j:j + 2]
        if w[0] == 0xF8 or w == b"\xff\xff":
            out.append("{%s}" % w.hex().upper())
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


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "roundtrip":
        sys.exit(0 if roundtrip(sys.argv[2]) else 1)
    if len(sys.argv) >= 4 and sys.argv[1] == "export":
        export(sys.argv[2], sys.argv[3])
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
