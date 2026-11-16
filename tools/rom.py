#!/usr/bin/env python3
"""Arma una copia traducida de la imagen del juego (.3ds/.cci o .cxi descifrada).

    python3 tools/rom.py verify JUEGO.3ds      revisa todos los hashes de la imagen

La función build_rom() la usa el instalador. La imagen nueva es la original con:
  - el code.bin del ExeFS reemplazado por el traducido, sin comprimir (en el
    exheader se apaga la marca de código comprimido);
  - el RomFS con los archivos traducidos: se conservan las tablas de carpetas y
    archivos, se actualizan la posición y el tamaño de cada archivo y se
    recalculan los tres niveles de hashes del IVFC;
  - los hashes del NCCH recalculados (exheader, ExeFS y RomFS) y, en un .3ds,
    las particiones siguientes (manual, actualización) corridas a continuación.
Las firmas RSA no se pueden rehacer; los emuladores y Luma3DS no las piden.
"""
import hashlib
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ctr import Image, InvalidImage, NONE, u32, u64  # noqa: E402

BLOCK = 0x1000          # bloque de hash del IVFC (2^12)
CHUNK = 1 << 22         # copia en tramos de 4 MiB


def align(n, a):
    return (n + a - 1) // a * a


def sha(b):
    return hashlib.sha256(b).digest()


# ---------- RomFS ----------

def romfs_plan(img, replaced):
    """Tablas del nivel 3 con las posiciones nuevas y la lista de lo que hay que escribir.

    Devuelve (meta, data_off, entries, l3_size): meta son los bytes del nivel 3 antes
    de los datos; entries, [(posición en el nivel 3, origen)], donde origen es bytes
    (archivo traducido) o (posición en la imagen, tamaño) (archivo sin cambios).
    """
    base, _ = img.romfs
    ivfc = img.read(base, 0x60)
    l3 = base + align(0x60 + u32(ivfc, 0x08), BLOCK)
    hdr = img.read(l3, 0x28)
    data_off = u32(hdr, 0x24)
    meta = bytearray(img.read(l3, data_off))
    fm_off, fm_size = u32(hdr, 0x1C), u32(hdr, 0x20)
    dm_off = u32(hdr, 0x0C)

    def name(o, at):
        n = u32(meta, o + at)
        return bytes(meta[o + at + 4:o + at + 4 + n]).decode("utf-16-le")

    paths = {}  # posición de la entrada en meta → ruta

    def walk(d, prefix):
        f = u32(meta, dm_off + d + 0x0C)
        while f != NONE:
            paths[fm_off + f] = prefix + name(fm_off + f, 0x1C)
            f = u32(meta, fm_off + f + 0x04)
        c = u32(meta, dm_off + d + 0x08)
        while c != NONE:
            walk(c, prefix + name(dm_off + c, 0x14) + "/")
            c = u32(meta, dm_off + c + 0x04)

    walk(0, "")
    if fm_off + fm_size > data_off:
        raise InvalidImage("RomFS con tablas inesperadas")
    # Mismo orden que el original; cada archivo alineado a 16 bytes, como en el juego.
    order = sorted(paths, key=lambda e: u64(meta, e + 0x08))
    entries, pos = [], 0
    for e in order:
        path = paths[e]
        old_off, old_size = u64(meta, e + 0x08), u64(meta, e + 0x10)
        src = replaced.get(path)
        size = len(src) if src is not None else old_size
        pos = align(pos, 16)
        struct.pack_into("<QQ", meta, e + 0x08, pos, size)
        entries.append((data_off + pos, src if src is not None else (l3 + data_off + old_off, old_size)))
        pos += size
    missing = set(replaced) - set(paths.values())
    if missing:
        raise ValueError(f"no están en el RomFS: {sorted(missing)[:3]}")
    return bytes(meta), data_off, entries, data_off + pos


def ivfc_layout(l3_size, master_size_old=None):
    """Tamaños y posiciones lógicas de los tres niveles para un nivel 3 de l3_size bytes."""
    l2 = align(l3_size, BLOCK) // BLOCK * 32
    l1 = align(l2, BLOCK) // BLOCK * 32
    master = align(l1, BLOCK) // BLOCK * 32
    lo1 = 0
    lo2 = align(lo1 + l1, BLOCK)
    lo3 = align(lo2 + l2, BLOCK)
    return master, (lo1, l1), (lo2, l2), (lo3, l3_size)


def write_romfs(img, out, start, replaced, log):
    """Escribe el RomFS en out desde start; devuelve (tamaño, tamaño de la región de hash)."""
    meta, data_off, entries, l3_size = romfs_plan(img, replaced)
    master_size, (lo1, l1), (lo2, l2), (lo3, _) = ivfc_layout(l3_size)
    p3 = align(0x60 + master_size, BLOCK)       # el nivel 3 va primero
    p1 = p3 + align(l3_size, BLOCK)
    p2 = p1 + align(l1, BLOCK)
    total = p2 + align(l2, BLOCK)

    # Nivel 3: tablas y datos, con los hashes de cada bloque de 4 KiB al vuelo.
    l2_hashes = bytearray()
    buf = bytearray()
    out.seek(start + p3)

    def put(b):
        nonlocal buf
        out.write(b)
        data = bytes(buf) + bytes(b) if buf else bytes(b)
        mv = memoryview(data)
        full = len(data) // BLOCK * BLOCK
        for i in range(0, full, BLOCK):
            l2_hashes.extend(sha(mv[i:i + BLOCK]))
        buf = bytearray(mv[full:])

    written = 0

    def pad_to(n):
        nonlocal written
        if n > written:
            put(bytes(n - written))
            written = n

    put(meta)
    written = len(meta)
    pad_to(data_off)
    done = 0
    for i, (pos, src) in enumerate(entries):
        pad_to(pos)
        if isinstance(src, bytes):
            put(src)
            written += len(src)
        else:
            off, size = src
            while size:
                n = min(size, CHUNK)
                put(img.read(off, n))
                off, size, written = off + n, size - n, written + n
        if i * 10 // len(entries) != done:
            done = i * 10 // len(entries)
            log(f"  RomFS: {done * 10} %")
    if buf:
        l2_hashes.extend(sha(bytes(buf) + bytes(BLOCK - len(buf))))
        out.write(bytes(align(written, BLOCK) - written))

    def hashes(level):
        level = bytes(level) + bytes(align(len(level), BLOCK) - len(level))
        return b"".join(sha(level[i:i + BLOCK]) for i in range(0, len(level), BLOCK))

    l1_hashes = hashes(l2_hashes)
    master = hashes(l1_hashes)
    out.seek(start + p1)
    out.write(l1_hashes + bytes(align(l1, BLOCK) - l1))
    out.seek(start + p2)
    out.write(bytes(l2_hashes) + bytes(align(l2, BLOCK) - l2))

    header = bytearray(0x60)
    header[0:4] = b"IVFC"
    struct.pack_into("<II", header, 4, 0x10000, master_size)
    for k, (lo, size) in enumerate([(lo1, l1), (lo2, l2), (lo3, l3_size)]):
        struct.pack_into("<QQI", header, 0x0C + k * 0x18, lo, size, 12)
    struct.pack_into("<I", header, 0x54, 0x5C)
    out.seek(start)
    out.write(bytes(header) + master + bytes(p3 - 0x60 - len(master)))
    return total, align(0x60 + master_size, 0x200)


# ---------- ExeFS y NCCH ----------

def build_exefs(img, code):
    """ExeFS con .code = code (sin comprimir) y los demás archivos iguales."""
    base, _ = img.exefs
    h = img.read(base, 0x200)
    files = []
    for i in range(10):
        n = h[i * 16:i * 16 + 8].rstrip(b"\0").decode()
        if n:
            off, size = struct.unpack_from("<II", h, i * 16 + 8)
            files.append((n, code if n == ".code" else img.read(base + 0x200 + off, size)))
    head, body = bytearray(0x200), bytearray()
    for i, (n, data) in enumerate(files):
        struct.pack_into("<8sII", head, i * 16, n.encode(), len(body), len(data))
        head[0x200 - 32 * (i + 1):0x200 - 32 * i] = sha(data)
        body += data + bytes(align(len(data), 0x200) - len(data))
    return bytes(head + body)


def write_ncch(img, out, start, code, replaced, log):
    """Escribe el NCCH traducido en out desde start; devuelve su tamaño."""
    nc = img.ncch_off
    h = bytearray(img.read(nc, 0x200))
    unit = 0x200 << h[0x18E]
    exefs_off = u32(h, 0x1A0) * unit
    # Todo lo que va antes del ExeFS (cabecera, exheader, logo, región plana) queda igual.
    out.seek(start)
    pre = bytearray(img.read(nc, exefs_off))
    if code is not None:
        exh = pre[0x200:0x600]
        exh[0x0D] &= ~1                      # el code.bin ya no va comprimido
        pre[0x200:0x600] = exh
        struct.pack_into("32s", h, 0x160, sha(bytes(exh)))
        exefs = build_exefs(img, code)
    else:
        exefs = img.read(*img.exefs)
    out.write(pre)  # la cabecera (h) se escribe al final, con los tamaños y hashes nuevos
    out.seek(start + exefs_off)
    out.write(exefs)
    exefs_size = align(len(exefs), unit)
    out.write(bytes(exefs_size - len(exefs)))
    romfs_off = align(exefs_off + exefs_size, BLOCK)
    log("Armando el RomFS...")
    romfs_size, romfs_hash = write_romfs(img, out, start + romfs_off, replaced, log)
    romfs_size = align(romfs_size, unit)
    total = romfs_off + romfs_size
    struct.pack_into("<I", h, 0x104, total // unit)
    struct.pack_into("<II", h, 0x1A0, exefs_off // unit, exefs_size // unit)
    struct.pack_into("<III", h, 0x1B0, romfs_off // unit, romfs_size // unit, romfs_hash // unit)
    struct.pack_into("32s", h, 0x1C0, sha(exefs[:u32(h, 0x1A8) * unit]))
    romfs_head = out_read(out, start + romfs_off, romfs_hash)
    struct.pack_into("32s", h, 0x1E0, sha(romfs_head))
    out.seek(start)
    out.write(h)
    return total


def out_read(out, off, n):
    out.flush()
    with open(out.name, "rb") as r:
        r.seek(off)
        return r.read(n)


def build_rom(src, dst, replaced, code=None, log=print):
    """Escribe en dst la imagen src con los archivos de RomFS replaced ({ruta: bytes}) y el code.bin code."""
    img = Image(src)
    head = img.read(0, 0x200)
    with open(dst, "wb") as out:
        if head[0x100:0x104] != b"NCSD":
            write_ncch(img, out, 0, code, replaced, log)
            return
        ncsd = bytearray(head + img.read(0x200, img.ncch_off - 0x200))
        parts = [struct.unpack_from("<II", ncsd, 0x120 + 8 * i) for i in range(8)]
        start = parts[0][0] * 0x200
        size0 = write_ncch(img, out, start, code, replaced, log)
        pos = start + align(size0, 0x200)
        struct.pack_into("<II", ncsd, 0x120, parts[0][0], align(size0, 0x200) // 0x200)
        for i in range(1, 8):
            off, size = parts[i]
            if not size:
                continue
            log(f"Copiando la partición {i}...")
            out.seek(pos)
            src_off, left = off * 0x200, size * 0x200
            while left:
                n = min(left, CHUNK)
                out.write(img.read(src_off, n))
                src_off, left = src_off + n, left - n
            struct.pack_into("<II", ncsd, 0x120 + 8 * i, pos // 0x200, size)
            pos += size * 0x200
        if pos > u32(ncsd, 0x104) * 0x200:
            raise ValueError("la imagen traducida no entra en el tamaño de la tarjeta")
        out.seek(0)
        out.write(ncsd)


# ---------- verificación ----------

def verify(path, log=print):
    """Revisa los hashes del exheader, el ExeFS y los tres niveles del RomFS. Devuelve los errores."""
    img = Image(path)
    nc = img.ncch_off
    h = img.read(nc, 0x200)
    unit = 0x200 << h[0x18E]
    errors = []
    if sha(img.read(nc + 0x200, 0x400)) != h[0x160:0x180]:
        errors.append("hash del exheader")
    eb, _ = img.exefs
    eh = img.read(eb, 0x200)
    if sha(img.read(eb, u32(h, 0x1A8) * unit)) != h[0x1C0:0x1E0]:
        errors.append("hash del ExeFS")
    for i in range(10):
        n = eh[i * 16:i * 16 + 8].rstrip(b"\0")
        if n:
            off, size = struct.unpack_from("<II", eh, i * 16 + 8)
            if sha(img.read(eb + 0x200 + off, size)) != eh[0x200 - 32 * (i + 1):0x200 - 32 * i]:
                errors.append(f"hash de exefs/{n.decode()}")
    rb, _ = img.romfs
    if sha(img.read(rb, u32(h, 0x1B8) * unit)) != h[0x1E0:0x200]:
        errors.append("hash de la cabecera del RomFS")
    iv = img.read(rb, 0x60)
    master_size = u32(iv, 0x08)
    levels = [struct.unpack_from("<QQ", iv, 0x0C + k * 0x18) for k in range(3)]
    p3 = align(0x60 + master_size, BLOCK)
    p1 = p3 + align(levels[2][1], BLOCK)
    p2 = p1 + align(levels[0][1], BLOCK)
    phys = [p1, p2, p3]
    expected = img.read(rb + 0x60, master_size)
    for k in range(3):
        size = levels[k][1]
        got = bytearray()
        off = rb + phys[k]
        for i in range(0, size, BLOCK):
            got += sha(img.read(off + i, BLOCK) if i + BLOCK <= size
                       else img.read(off + i, size - i) + bytes(BLOCK - (size - i)))
            if k == 2 and i % (BLOCK * 25600) == 0:
                log(f"  nivel 3: {i * 100 // size} %")
        if bytes(got) != expected[:len(got)] or len(got) != len(expected):
            errors.append(f"hashes del nivel {k + 1} del RomFS")
        if k < 2:
            expected = img.read(rb + phys[k], levels[k][1])
    return errors


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "verify":
        errs = verify(sys.argv[2])
        print("todos los hashes bien" if not errs else "errores: " + ", ".join(errs))
        sys.exit(1 if errs else 0)
    sys.exit(__doc__)
