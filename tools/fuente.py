#!/usr/bin/env python3
"""Dibuja las letras españolas en las fuentes del juego.

    python3 tools/fuente.py ROMFS SALIDA [VISTAS]

Lee ROMFS/font/TsukuMin_*.bcfnt y escribe SALIDA/font/ con las mismas fuentes,
más las letras de `letras.py` en sus códigos. Con VISTAS, deja ahí un PNG por
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
from letras import ESPANOL  # noqa: E402

FUENTES = ["TsukuMin_9_9", "TsukuMin_12_12", "TsukuMin_14_14", "TsukuMin_16_16"]
PRUEBA = "¿Ñandú? ¡Sí! Áá Éé Íí Óó Úú Üü Ññ pingüino, acción, ¿qué?"

ALFA = {" ": 0, ".": 4, ":": 6, "-": 8, "+": 10, "*": 12, "#": 14, "@": 15}

# Acento agudo: el chico para la fuente de 9, el de dos filas para las
# mayúsculas y el de tres para las minúsculas de las demás.
AGUDO_CHICO = [" @", "@ "]
AGUDO = {
    2: [" -@", "@+ "],
    3: ["  -@", " +@ ", "@+  "],
}

BASES = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u", "ñ": "n",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U", "Ü": "U", "Ñ": "N",
    "¿": "?", "¡": "!",
}


def patron(filas):
    return [[ALFA[c] for c in f] for f in filas]


def tinta(g):
    filas = [j for j, r in enumerate(g) if any(r)]
    cols = [k for k in range(len(g[0])) if any(r[k] for r in g)]
    return filas[0], filas[-1], cols[0], cols[-1]


def tilde(ancho, alto=2):
    """Onda suavizada de `ancho` columnas y dos filas."""
    m = [[0] * ancho for _ in range(alto)]
    for x in range(ancho):
        t = x / (ancho - 1) if ancho > 1 else 0.5
        y = (1 - math.sin(2 * math.pi * t)) / 2 * (alto - 1)
        f = int(y)
        frac = y - f
        m[f][x] = max(m[f][x], round(15 * (1 - frac)))
        if f + 1 < alto:
            m[f + 1][x] = max(m[f + 1][x], round(15 * frac))
    return m


class Compositor:
    def __init__(self, font):
        self.f = font
        self.x_alta = tinta(self.base("x"))[0]       # primera fila de la x
        self.mayus = tinta(self.base("H"))[0]        # primera fila de la H
        # punto de la i: lo que queda por encima de la altura de la x
        gi = self.base("i")
        self.punto = [r[:] for r in gi[:self.x_alta] if any(r)]
        while self.punto and not any(r[0] for r in self.punto) and len(self.punto[0]) > 1:
            self.punto = [r[1:] for r in self.punto]
        ancho = max(k for r in self.punto for k, v in enumerate(r) if v) + 1
        self.punto = [r[:ancho] for r in self.punto]

    def base(self, ch):
        return self.f.glyph(self.f.index_of(sjis(ch)))

    def anchos(self, ch):
        return self.f.widths(self.f.index_of(sjis(ch)))

    def letra(self, ch):
        b = BASES[ch]
        g = [r[:] for r in self.base(b)]
        left, gw, cw = self.anchos(b)
        if ch in "¿¡":
            return self.girada(g), (left, gw, cw)
        mayuscula = b.isupper()
        tope = self.mayus if mayuscula else self.x_alta
        if not mayuscula:
            for j in range(tope):            # quita el punto de la i
                g[j] = [0] * len(g[j])
        r0, r1, c0, c1 = tinta(g)
        disponible = tope - 1                # una fila libre entre la marca y la letra
        if ch in "áéíóúÁÉÍÓÚ":
            if self.f.cell_h <= 12:
                marca = patron(AGUDO_CHICO)
            else:
                marca = patron(AGUDO[min(3, disponible) if not mayuscula else 2])
        elif ch in "ñÑ":
            marca = tilde(max(4, c1 - c0 + 1 + (0 if mayuscula else 1)))
        else:                                # diéresis
            ancho = c1 - c0 + 1
            p = self.punto
            pw = len(p[0])
            sep = max(1, ancho - 2 * pw)
            marca = [r + [0] * sep + r for r in p]
        mh, mw = len(marca), len(marca[0])
        y0 = max(0, tope - 1 - mh)
        x0 = round((c0 + c1 + 1) / 2 - mw / 2)
        return self.pegar(g, marca, x0, y0, left, cw)

    def pegar(self, g, marca, x0, y0, left, cw):
        """Pone la marca sobre la letra; si sobresale a la izquierda, corre el glifo."""
        ancho_celda = self.f.cell_w
        desde = min(0, x0)
        lienzo = [[0] * (ancho_celda - desde) for _ in g]
        for j, r in enumerate(g):
            for k, v in enumerate(r):
                lienzo[j][k - desde] = v
        for j, r in enumerate(marca):
            for k, v in enumerate(r):
                if v:
                    y, x = y0 + j, x0 + k - desde
                    lienzo[y][x] = max(lienzo[y][x], v)
        cols = [k for k in range(len(lienzo[0])) if any(r[k] for r in lienzo)]
        a, z = cols[0], cols[-1]
        if a > 0 and desde == 0:
            a = 0                            # el glifo empieza en la columna 0 de su celda
        filas = [r[a:a + ancho_celda] + [0] * max(0, ancho_celda - len(r[a:])) for r in lienzo]
        return filas, (left + desde + a, z - a + 1, cw)

    def girada(self, g):
        r0, r1, c0, c1 = tinta(g)
        baja = self.x_alta - self.mayus
        n = [[0] * len(g[0]) for _ in g]
        for j in range(r0, r1 + 1):
            for k in range(c0, c1 + 1):
                y = r0 + (r1 - j) + baja
                if y < len(g):
                    n[y][c0 + (c1 - k)] = g[j][k]
        return n


def componer(original):
    """Bytes de la fuente original → bytes de la fuente con las letras españolas."""
    f = Bcfnt(original)
    c = Compositor(f)
    for ch, code in ESPANOL.items():
        filas, (left, gw, cw) = c.letra(ch)
        i = f.cmap[code]
        f.set_glyph(i, filas)
        f.set_widths(i, left, gw, cw)
    return f.to_bytes()


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    romfs, salida = Path(sys.argv[1]), Path(sys.argv[2])
    vistas = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    (salida / "font").mkdir(parents=True, exist_ok=True)
    for nombre in FUENTES:
        datos = componer((romfs / "font" / f"{nombre}.bcfnt").read_bytes())
        (salida / "font" / f"{nombre}.bcfnt").write_bytes(datos)
        print(f"font/{nombre}.bcfnt: {len(ESPANOL)} letras")
        if vistas:
            vistas.mkdir(parents=True, exist_ok=True)
            w, h, px = render(Bcfnt(datos), [sjis(ch) for ch in PRUEBA], 3)
            write_png(vistas / f"{nombre}.png", w, h, px)


if __name__ == "__main__":
    main()
