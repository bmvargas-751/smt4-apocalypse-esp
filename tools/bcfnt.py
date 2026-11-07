#!/usr/bin/env python3
"""Fuentes de IVA (.bcfnt de 3DS): leer y cambiar glifos sin tocar la estructura.

    python3 tools/bcfnt.py info FUENTE
    python3 tools/bcfnt.py roundtrip FUENTE...      decodifica y recodifica las hojas, y compara
    python3 tools/bcfnt.py sheet FUENTE N SALIDA.png
    python3 tools/bcfnt.py text FUENTE "texto" SALIDA.png [ESCALA]

Solo se reemplazan dibujos y anchos de glifos que ya existen: el mapa de
caracteres (CMAP) y el tamaño del archivo no cambian.

Las hojas son texturas A4 (4 bits de alfa por píxel) en bloques de 8×8 en
orden Morton. Cada glifo ocupa una celda de (ancho+1)×(alto+1) dentro de la hoja.
"""
import struct
import sys
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letters import SPANISH  # noqa: E402

MORTON = [(sum(((i >> (2 * b)) & 1) << b for b in range(3)),
           sum(((i >> (2 * b + 1)) & 1) << b for b in range(3))) for i in range(64)]


class Bcfnt:
    def __init__(self, origen):
        """`origen`: la ruta de la fuente o sus bytes."""
        if isinstance(origen, (bytes, bytearray)):
            self.data = bytearray(origen)
        else:
            self.data = bytearray(Path(origen).read_bytes())
        d = self.data
        if d[:4] != b"CFNT":
            raise ValueError("no es CFNT")
        o = struct.unpack_from("<H", d, 6)[0]
        if d[o:o + 4] != b"FINF":
            raise ValueError("falta FINF")
        (_, self.line_feed, self.alt_index, *self.default_width, self.encoding,
         tglp, cwdh, cmap, self.height, self.width, self.ascent, _) = struct.unpack_from(
            "<BBHBBBBIIIBBBB", d, o + 8)
        t = tglp - 8
        (self.cell_w, self.cell_h, self.baseline, self.max_w, self.sheet_size, self.sheets,
         self.fmt, self.cols, self.rows, self.sheet_w, self.sheet_h, self.sheet_data) = struct.unpack_from(
            "<BBBBIHHHHHHI", d, t + 8)
        if self.fmt != 11:
            raise ValueError(f"formato de hoja {self.fmt} no soportado (solo A4)")
        self.per_sheet = self.cols * self.rows
        # anchos: índice → posición en el archivo de (izquierda, ancho del glifo, avance)
        self.width_at = {}
        c = cwdh - 8
        while c >= 0:
            start, end, nxt = struct.unpack_from("<HHI", d, c + 8)
            for i in range(start, end + 1):
                self.width_at[i] = c + 16 + 3 * (i - start)
            c = nxt - 8 if nxt else -1
        # mapa de caracteres: código → índice
        self.cmap = {}
        c = cmap - 8
        while c >= 0:
            begin, end, method, _, nxt = struct.unpack_from("<HHHHI", d, c + 8)
            p = c + 20
            if method == 0:
                first = struct.unpack_from("<H", d, p)[0]
                for k in range(begin, end + 1):
                    self.cmap[k] = first + k - begin
            elif method == 1:
                for k in range(begin, end + 1):
                    v = struct.unpack_from("<H", d, p + 2 * (k - begin))[0]
                    if v != 0xFFFF:
                        self.cmap[k] = v
            else:
                for j in range(struct.unpack_from("<H", d, p)[0]):
                    k, v = struct.unpack_from("<HH", d, p + 2 + 4 * j)
                    self.cmap[k] = v
            c = nxt - 8 if nxt else -1
        self._sheets = {}

    # hojas
    def _sheet_offset(self, n):
        return self.sheet_data + n * self.sheet_size

    def sheet(self, n):
        if n not in self._sheets:
            w, h = self.sheet_w, self.sheet_h
            raw = self.data[self._sheet_offset(n):self._sheet_offset(n) + self.sheet_size]
            px = bytearray(w * h)
            tiles_x = w // 8
            for t in range((w // 8) * (h // 8)):
                tx, ty = (t % tiles_x) * 8, (t // tiles_x) * 8
                base = t * 32
                for i, (mx, my) in enumerate(MORTON):
                    b = raw[base + (i >> 1)]
                    px[(ty + my) * w + tx + mx] = (b >> 4) if i & 1 else (b & 15)
            self._sheets[n] = px
        return self._sheets[n]

    def _encode_sheet(self, n):
        w, h = self.sheet_w, self.sheet_h
        px = self._sheets[n]
        raw = bytearray(self.sheet_size)
        tiles_x = w // 8
        for t in range((w // 8) * (h // 8)):
            tx, ty = (t % tiles_x) * 8, (t // tiles_x) * 8
            base = t * 32
            for i, (mx, my) in enumerate(MORTON):
                v = px[(ty + my) * w + tx + mx] & 15
                raw[base + (i >> 1)] |= v << 4 if i & 1 else v
        o = self._sheet_offset(n)
        self.data[o:o + self.sheet_size] = raw

    # glifos
    def _cell(self, index):
        n, k = divmod(index, self.per_sheet)
        r, c = divmod(k, self.cols)
        return n, c * (self.cell_w + 1) + 1, r * (self.cell_h + 1) + 1

    def glyph(self, index):
        """Filas de alfa (0-15) de la celda, de arriba abajo."""
        n, x, y = self._cell(index)
        px = self.sheet(n)
        w = self.sheet_w
        return [list(px[(y + j) * w + x:(y + j) * w + x + self.cell_w]) for j in range(self.cell_h)]

    def set_glyph(self, index, rows):
        n, x, y = self._cell(index)
        px = self.sheet(n)
        w = self.sheet_w
        for j in range(self.cell_h):
            px[(y + j) * w + x:(y + j) * w + x + self.cell_w] = bytes(rows[j][:self.cell_w])

    def widths(self, index):
        return struct.unpack_from("<bBB", self.data, self.width_at[index])

    def set_widths(self, index, left, glyph_w, char_w):
        struct.pack_into("<bBB", self.data, self.width_at[index], left, glyph_w, char_w)

    def index_of(self, code):
        return self.cmap.get(code, self.alt_index)

    def to_bytes(self):
        for n in self._sheets:
            self._encode_sheet(n)
        return bytes(self.data)

    def save(self, path):
        Path(path).write_bytes(self.to_bytes())


def sjis(ch):
    """Código de la fuente para un carácter, como lo escribe el texto del juego."""
    if ch in SPANISH:
        return SPANISH[ch]
    if ch == " ":
        ch = "　"
    elif "!" <= ch <= "~":
        ch = chr(ord(ch) + 0xFEE0)
    b = ch.encode("cp932")
    return b[0] << 8 | b[1] if len(b) == 2 else b[0]


def write_png(path, w, h, gray):
    rows = b"".join(b"\0" + bytes(gray[y * w:(y + 1) * w]) for y in range(h))
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
    Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0))
                           + chunk(b"IDAT", zlib.compress(rows, 9)) + chunk(b"IEND", b""))


def render(font, codes, scale=4, pad=2):
    """Dibuja una línea de glifos (blanco sobre negro), como la pondría el juego."""
    pen, placed = pad, []
    for code in codes:
        i = font.index_of(code)
        left, gw, cw = font.widths(i)
        placed.append((pen + left, font.glyph(i), gw))
        pen += cw
    w, h = pen + pad, font.cell_h + 2 * pad
    canvas = [0] * (w * h)
    for x0, g, gw in placed:
        for j, row in enumerate(g):
            for k in range(min(gw, len(row))):
                if 0 <= x0 + k < w and row[k]:
                    p = (pad + j) * w + x0 + k
                    canvas[p] = max(canvas[p], row[k] * 17)
    big = [canvas[(y // scale) * w + x // scale] for y in range(h * scale) for x in range(w * scale)]
    return w * scale, h * scale, big


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "info":
        f = Bcfnt(a[1])
        print(f"celda {f.cell_w}×{f.cell_h}, línea base {f.baseline}, interlineado {f.line_feed}, "
              f"{len(f.cmap)} caracteres, {f.sheets} hojas de {f.sheet_w}×{f.sheet_h}, codificación {f.encoding}")
    elif len(a) >= 2 and a[0] == "roundtrip":
        ok = True
        for p in a[1:]:
            f = Bcfnt(p)
            orig = bytes(f.data)
            for n in range(f.sheets):
                f.sheet(n)
                f._encode_sheet(n)
            same = bytes(f.data) == orig
            ok &= same
            print(f"{'idéntico' if same else 'DISTINTO'}: {p}")
        sys.exit(0 if ok else 1)
    elif len(a) == 4 and a[0] == "sheet":
        f = Bcfnt(a[1])
        write_png(a[3], f.sheet_w, f.sheet_h, [v * 17 for v in f.sheet(int(a[2]))])
    elif len(a) >= 4 and a[0] == "text":
        f = Bcfnt(a[1])
        w, h, px = render(f, [sjis(c) for c in a[2]], int(a[4]) if len(a) > 4 else 4)
        write_png(a[3], w, h, px)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
