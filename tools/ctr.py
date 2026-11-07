#!/usr/bin/env python3
"""Lee una imagen de 3DS descifrada (.3ds/.cci o .cxi): cabecera, RomFS y ExeFS.

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


class InvalidImage(ValueError):
    pass


class Image:
    def __init__(self, path):
        self.f = open(path, "rb")
        head = self.read(0, 0x200)
        if head[0x100:0x104] == b"NCSD":
            self.ncch_off = u32(head, 0x120) * 0x200
        elif head[0x100:0x104] == b"NCCH":
            self.ncch_off = 0
        else:
            raise InvalidImage("no es una imagen de 3DS (.3ds, .cci o .cxi)")
        h = self.read(self.ncch_off, 0x200)
        if h[0x100:0x104] != b"NCCH":
            raise InvalidImage("la partición del juego no es NCCH")
        flags = h[0x188:0x190]
        if not flags[7] & 0x4:
            raise InvalidImage("la imagen está cifrada; hace falta una descifrada")
        unit = 0x200 << flags[6]
        self.program_id = u64(h, 0x118)
        self.product = h[0x150:0x160].rstrip(b"\0").decode()
        self.exefs = (self.ncch_off + u32(h, 0x1A0) * unit, u32(h, 0x1A4) * unit)
        self.romfs = (self.ncch_off + u32(h, 0x1B0) * unit, u32(h, 0x1B4) * unit)
        self._files = None

    def read(self, off, size):
        self.f.seek(off)
        return self.f.read(size)

    def files(self):
        """Índice del RomFS: ruta → (posición en la imagen, tamaño)."""
        if self._files is not None:
            return self._files
        base, _ = self.romfs
        ivfc = self.read(base, 0x60)
        if ivfc[:4] != b"IVFC":
            raise InvalidImage("el RomFS no empieza con IVFC")
        block = 1 << u32(ivfc, 0x4C)
        l3 = base + (0x60 + u32(ivfc, 0x08) + block - 1) // block * block
        hdr = self.read(l3, 0x28)
        dir_meta = self.read(l3 + u32(hdr, 0x0C), u32(hdr, 0x10))
        file_meta = self.read(l3 + u32(hdr, 0x1C), u32(hdr, 0x20))
        data = l3 + u32(hdr, 0x24)

        def name(meta, o, at):
            n = u32(meta, o + at)
            return meta[o + at + 4:o + at + 4 + n].decode("utf-16-le")

        index = {}

        def walk(d, prefix):
            f = u32(dir_meta, d + 0x0C)
            while f != NONE:
                index[prefix + name(file_meta, f, 0x1C)] = (data + u64(file_meta, f + 0x08),
                                                            u64(file_meta, f + 0x10))
                f = u32(file_meta, f + 0x04)
            c = u32(dir_meta, d + 0x08)
            while c != NONE:
                walk(c, prefix + name(dir_meta, c, 0x14) + "/")
                c = u32(dir_meta, c + 0x04)

        walk(0, "")
        self._files = index
        return index

    def read_file(self, path):
        off, size = self.files()[path]
        return self.read(off, size)


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
    total = 0
    for path, (off, size) in img.files().items():
        dest = out / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as w:
            left = size
            while left:
                chunk = img.read(off, min(left, 1 << 24))
                w.write(chunk)
                off += len(chunk)
                left -= len(chunk)
        total += size
    print(f"romfs/  {len(img.files())} archivos, {total:,} bytes")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("info", "extract"):
        sys.exit(__doc__)
    try:
        img = Image(sys.argv[2])
    except InvalidImage as e:
        sys.exit(f"{sys.argv[2]}: {e}")
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
