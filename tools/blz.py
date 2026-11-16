"""Descompresión BLZ (LZ hacia atrás), la del code.bin de los juegos de 3DS.

    python3 tools/blz.py ENTRADA SALIDA
"""
import struct
import sys


def decompress(src):
    inc_len = struct.unpack_from("<I", src, len(src) - 4)[0]
    if not inc_len:
        return src[:-4]
    hdr_len = src[-5]
    enc_len = struct.unpack_from("<I", src, len(src) - 8)[0] & 0xFFFFFF
    dec_len = len(src) - enc_len
    pak = bytes(reversed(src[dec_len:dec_len + enc_len - hdr_len]))
    raw = bytearray(enc_len + inc_len)
    p = r = 0
    mask = flags = 0
    while r < len(raw):
        mask >>= 1
        if not mask:
            if p >= len(pak):
                break
            flags, p, mask = pak[p], p + 1, 0x80
        if not flags & mask:
            if p >= len(pak):
                break
            raw[r] = pak[p]
            r, p = r + 1, p + 1
        else:
            if p + 1 >= len(pak):
                break
            pos = pak[p] << 8 | pak[p + 1]
            p += 2
            n = min((pos >> 12) + 3, len(raw) - r)
            pos = (pos & 0xFFF) + 3
            for _ in range(n):
                raw[r] = raw[r - pos]
                r += 1
    return src[:dec_len] + bytes(reversed(raw))


if __name__ == "__main__":
    data = decompress(open(sys.argv[1], "rb").read())
    open(sys.argv[2], "wb").write(data)
    print(f"{len(data):,} bytes")
