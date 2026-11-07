#!/usr/bin/env python3
"""Dibuja las letras españolas en las fuentes del juego.

    python3 tools/font.py ROMFS SALIDA [VISTAS]

Lee ROMFS/font/TsukuMin_*.bcfnt y escribe SALIDA/font/ con las mismas fuentes,
más las letras de `letters.py` en sus códigos. Con VISTAS, deja ahí un PNG por
fuente con una frase de prueba.

Cada letra es la base inglesa de la misma fuente (a, e, A, ?, ...) más una
marca: el acento y la tilde de la ñ se dibujan a la medida de cada fuente;
la diéresis usa el punto de la i; ¿ y ¡ son ? y ! girados y bajados hasta la
altura de la x, como en la tipografía española.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bcfnt import Bcfnt, render, sjis, write_png  # noqa: E402
from letters import SPANISH  # noqa: E402

FONTS = ["TsukuMin_9_9", "TsukuMin_12_12", "TsukuMin_14_14", "TsukuMin_16_16"]
SAMPLE = "¿Ñandú? ¡Sí! Áá Éé Íí Óó Úú Üü Ññ pingüino, acción, ¿qué?"

ALPHA = {" ": 0, ".": 4, ":": 6, "-": 8, "+": 10, "*": 12, "#": 14, "@": 15}

# Acento agudo: el chico para la fuente de 9, el de dos filas para las
# mayúsculas y el de tres para las minúsculas de las demás.
ACUTE_SMALL = [" @", "@ "]
ACUTE = {
    2: [" -@", "@+ "],
    3: ["  -@", " +@ ", "@+  "],
}

BASES = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u", "ñ": "n",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U", "Ü": "U", "Ñ": "N",
    "¿": "?", "¡": "!",
}


def pattern(rows):
    return [[ALPHA[c] for c in r] for r in rows]


def ink(g):
    """Primera y última fila, y primera y última columna con tinta."""
    rows = [j for j, r in enumerate(g) if any(r)]
    cols = [k for k in range(len(g[0])) if any(r[k] for r in g)]
    return rows[0], rows[-1], cols[0], cols[-1]


def tilde(width, height=2):
    """Onda suavizada de `width` columnas y dos filas."""
    m = [[0] * width for _ in range(height)]
    for x in range(width):
        t = x / (width - 1) if width > 1 else 0.5
        y = (1 - math.sin(2 * math.pi * t)) / 2 * (height - 1)
        f = int(y)
        frac = y - f
        m[f][x] = max(m[f][x], round(15 * (1 - frac)))
        if f + 1 < height:
            m[f + 1][x] = max(m[f + 1][x], round(15 * frac))
    return m


class Composer:
    def __init__(self, font):
        self.f = font
        self.x_top = ink(self.base("x"))[0]        # primera fila de la x
        self.cap_top = ink(self.base("H"))[0]      # primera fila de la H
        # punto de la i: lo que queda por encima de la altura de la x
        gi = self.base("i")
        self.dot = [r[:] for r in gi[:self.x_top] if any(r)]
        while self.dot and not any(r[0] for r in self.dot) and len(self.dot[0]) > 1:
            self.dot = [r[1:] for r in self.dot]
        width = max(k for r in self.dot for k, v in enumerate(r) if v) + 1
        self.dot = [r[:width] for r in self.dot]

    def base(self, ch):
        return self.f.glyph(self.f.index_of(sjis(ch)))

    def widths_of(self, ch):
        return self.f.widths(self.f.index_of(sjis(ch)))

    def letter(self, ch):
        b = BASES[ch]
        g = [r[:] for r in self.base(b)]
        left, gw, cw = self.widths_of(b)
        if ch in "¿¡":
            return self.rotated(g), (left, gw, cw)
        upper = b.isupper()
        top = self.cap_top if upper else self.x_top
        if not upper:
            for j in range(top):               # quita el punto de la i
                g[j] = [0] * len(g[j])
        r0, r1, c0, c1 = ink(g)
        room = top - 1                         # una fila libre entre la marca y la letra
        if ch in "áéíóúÁÉÍÓÚ":
            if self.f.cell_h <= 12:
                mark = pattern(ACUTE_SMALL)
            else:
                mark = pattern(ACUTE[min(3, room) if not upper else 2])
        elif ch in "ñÑ":
            mark = tilde(max(4, c1 - c0 + 1 + (0 if upper else 1)))
        else:                                  # diéresis
            width = c1 - c0 + 1
            p = self.dot
            pw = len(p[0])
            gap = max(1, width - 2 * pw)
            mark = [r + [0] * gap + r for r in p]
        mh, mw = len(mark), len(mark[0])
        y0 = max(0, top - 1 - mh)
        x0 = round((c0 + c1 + 1) / 2 - mw / 2)
        return self.paste(g, mark, x0, y0, left, cw)

    def paste(self, g, mark, x0, y0, left, cw):
        """Pone la marca sobre la letra; si sobresale a la izquierda, corre el glifo."""
        cell_w = self.f.cell_w
        shift = min(0, x0)
        canvas = [[0] * (cell_w - shift) for _ in g]
        for j, r in enumerate(g):
            for k, v in enumerate(r):
                canvas[j][k - shift] = v
        for j, r in enumerate(mark):
            for k, v in enumerate(r):
                if v:
                    y, x = y0 + j, x0 + k - shift
                    canvas[y][x] = max(canvas[y][x], v)
        cols = [k for k in range(len(canvas[0])) if any(r[k] for r in canvas)]
        a, z = cols[0], cols[-1]
        if a > 0 and shift == 0:
            a = 0                              # el glifo empieza en la columna 0 de su celda
        rows = [r[a:a + cell_w] + [0] * max(0, cell_w - len(r[a:])) for r in canvas]
        return rows, (left + shift + a, z - a + 1, cw)

    def rotated(self, g):
        r0, r1, c0, c1 = ink(g)
        down = self.x_top - self.cap_top
        n = [[0] * len(g[0]) for _ in g]
        for j in range(r0, r1 + 1):
            for k in range(c0, c1 + 1):
                y = r0 + (r1 - j) + down
                if y < len(g):
                    n[y][c0 + (c1 - k)] = g[j][k]
        return n


def compose(original):
    """Bytes de la fuente original → bytes de la fuente con las letras españolas."""
    f = Bcfnt(original)
    c = Composer(f)
    for ch, code in SPANISH.items():
        rows, (left, gw, cw) = c.letter(ch)
        i = f.cmap[code]
        f.set_glyph(i, rows)
        f.set_widths(i, left, gw, cw)
    return f.to_bytes()


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    romfs, out = Path(sys.argv[1]), Path(sys.argv[2])
    previews = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    (out / "font").mkdir(parents=True, exist_ok=True)
    for name in FONTS:
        data = compose((romfs / "font" / f"{name}.bcfnt").read_bytes())
        (out / "font" / f"{name}.bcfnt").write_bytes(data)
        print(f"font/{name}.bcfnt: {len(SPANISH)} letras")
        if previews:
            previews.mkdir(parents=True, exist_ok=True)
            w, h, px = render(Bcfnt(data), [sjis(ch) for ch in SAMPLE], 3)
            write_png(previews / f"{name}.png", w, h, px)


if __name__ == "__main__":
    main()
