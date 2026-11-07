#!/usr/bin/env python3
"""Lee una imagen .3ds descifrada: muestra su cabecera y extrae el RomFS y el ExeFS.

    python3 tools/ctr.py info    JUEGO.3ds
    python3 tools/ctr.py extract JUEGO.3ds DESTINO

DESTINO queda con romfs/ (los archivos del juego) y exefs/ (code.bin y otros).
Solo lee la imagen; no la modifica.
"""
import struct
import sys
from pathlib import Path

NONE = 0xFFFFFFFF


def u32(b, o):
    return struct.unpack_from("<I", b, o)[0]


def u64(b, o):
    return struct.unpack_from("<Q", b, o)[0]


class Image:
    def __init__(self, path):
        self.f = open(path, "rb")
        ncsd = self.read(0, 0x200)
        if ncsd[0x100:0x104] != b"NCSD":
            sys.exit("No es una imagen .3ds (falta NCSD).")
        self.ncch_off = u32(ncsd, 0x120) * 0x200
        h = self.read(self.ncch_off, 0x200)
        if h[0x100:0x104] != b"NCCH":
            sys.exit("La partición 0 no es NCCH.")
        flags = h[0x188:0x190]
        if not flags[7] & 0x4:
            sys.exit("La imagen está cifrada; hace falta una descifrada.")
        unit = 0x200 << flags[6]
        self.program_id = u64(h, 0x118)
        self.product = h[0x150:0x160].rstrip(b"\0").decode()
        self.exefs = (self.ncch_off + u32(h, 0x1A0) * unit, u32(h, 0x1A4) * unit)
        self.romfs = (self.ncch_off + u32(h, 0x1B0) * unit, u32(h, 0x1B4) * unit)

    def read(self, off, size):
        self.f.seek(off)
        return self.f.read(size)


def info(img):
    print(f"Producto:  {img.product}")
    print(f"ID:        {img.program_id:016X}")
    print(f"ExeFS:     {img.exefs[1]:,} bytes")
    print(f"RomFS:     {img.romfs[1]:,} bytes")


def extract_exefs(img, out):
    base, _ = img.exefs
    h = img.read(base, 0x200)
    for i in range(10):
        name = h[i * 16:i * 16 + 8].rstrip(b"\0").decode()
        off, size = struct.unpack_from("<II", h, i * 16 + 8)
        if name and size:
            (out / name).write_bytes(img.read(base + 0x200 + off, size))
            print(f"exefs/{name}  {size:,} bytes")


def extract_romfs(img, out):
    base, _ = img.romfs
    ivfc = img.read(base, 0x60)
    if ivfc[:4] != b"IVFC":
        sys.exit("El RomFS no empieza con IVFC.")
    master_hash = u32(ivfc, 0x08)
    block = 1 << u32(ivfc, 0x4C)
    l3 = base + (0x60 + master_hash + block - 1) // block * block
    hdr = img.read(l3, 0x28)
    dir_meta = img.read(l3 + u32(hdr, 0x0C), u32(hdr, 0x10))
    file_meta = img.read(l3 + u32(hdr, 0x1C), u32(hdr, 0x20))
    data = l3 + u32(hdr, 0x24)

    def name(meta, o, at):
        n = u32(meta, o + at)
        return meta[o + at + 4:o + at + 4 + n].decode("utf-16-le")

    count = total = 0

    def walk(d, path):
        nonlocal count, total
        path.mkdir(parents=True, exist_ok=True)
        f = u32(dir_meta, d + 0x0C)
        while f != NONE:
            off, size = u64(file_meta, f + 0x08), u64(file_meta, f + 0x10)
            dest = path / name(file_meta, f, 0x1C)
            with open(dest, "wb") as w:
                pos = data + off
                left = size
                while left:
                    chunk = img.read(pos, min(left, 1 << 24))
                    w.write(chunk)
                    pos += len(chunk)
                    left -= len(chunk)
            count += 1
            total += size
            f = u32(file_meta, f + 0x04)
        c = u32(dir_meta, d + 0x08)
        while c != NONE:
            walk(c, path / name(dir_meta, c, 0x14))
            c = u32(dir_meta, c + 0x04)

    walk(0, out)
    print(f"romfs/  {count} archivos, {total:,} bytes")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("info", "extract"):
        sys.exit(__doc__)
    img = Image(sys.argv[2])
    if sys.argv[1] == "info":
        info(img)
        return
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    out = Path(sys.argv[3])
    (out / "exefs").mkdir(parents=True, exist_ok=True)
    info(img)
    extract_exefs(img, out / "exefs")
    extract_romfs(img, out / "romfs")


if __name__ == "__main__":
    main()
