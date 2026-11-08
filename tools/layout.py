#!/usr/bin/env python3
"""Renglones de los mensajes: ancho en píxeles, saltos que se ven y partición.

    python3 tools/layout.py stats ROMFS ARCHIVO.mbm     ancho máximo y renglones por página

El juego no parte el texto solo: cada renglón termina en {F801}, y {F802}
empieza una página nueva. En el inglés hay dos clases de salto:
  fijo   separa opciones de una lista, o una frase de otra: se conserva;
  suelto solo sirve para que el párrafo quepa en la caja.
El traductor ve el texto con los saltos sueltos cambiados por un espacio
(«forma de lectura») y escribe solo los fijos. Al instalar, cada renglón se
parte por palabras para que no pase del renglón más ancho del inglés en el
mismo archivo (medido en píxeles con la fuente del juego).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bcfnt import Bcfnt  # noqa: E402
from letters import SPANISH  # noqa: E402

TOKEN = re.compile(r"(\{[0-9A-F]{4}\})")
SPEAKER = re.compile(r"\{F812\}.*?\{0000\}")    # nombre de quien habla: va en su etiqueta, no en la caja
BR, PAGE, END = "{F801}", "{F802}", "{FFFF}"
SENTENCE_END = tuple(".!?:”’)…")
MEASURE_FONT = "font/TsukuMin_14_14.bcfnt"      # la misma fuente para medir el inglés y el español


class Meter:
    def __init__(self, font):
        self.font = font if isinstance(font, Bcfnt) else Bcfnt(font)
        self._cache = {}

    def char(self, ch):
        if ch not in self._cache:
            if ch in SPANISH:
                code = SPANISH[ch]
            else:
                c = "　" if ch == " " else (chr(ord(ch) + 0xFEE0) if "!" <= ch <= "~" else ch)
                try:
                    b = c.encode("cp932")
                    code = b[0] << 8 | b[1] if len(b) == 2 else b[0]
                except UnicodeEncodeError:
                    code = None
            if code is None or code not in self.font.cmap:
                self._cache[ch] = None
            else:
                self._cache[ch] = self.font.widths(self.font.cmap[code])[2]
        return self._cache[ch]

    def width(self, line):
        """Ancho en píxeles de un renglón (los códigos y el nombre de quien habla no ocupan lugar)."""
        return sum(self.char(c) or 0 for c in TOKEN.sub("", SPEAKER.sub("", line)))

    def missing(self, text):
        """Caracteres que la fuente no tiene."""
        return sorted({c for c in TOKEN.sub("", text) if c != "\n" and self.char(c) is None})


def lines_of(msg):
    """Renglones de un mensaje: [(texto, terminó en {F801})], sin el {FFFF} final."""
    body = msg[:-len(END)] if msg.endswith(END) else msg
    parts = body.split(BR)
    return [(p, i < len(parts) - 1) for i, p in enumerate(parts)]


def page_lines(msg):
    """Renglones por página."""
    counts, n = [], 0
    for text, _ in lines_of(msg):
        if text.startswith(PAGE):
            counts.append(n)
            n = 0
        if TOKEN.sub("", text).strip():
            n += 1
    counts.append(n)
    return counts


def limits(meter, messages):
    """(ancho máximo en px, renglones máximos por página) del inglés de un archivo."""
    width, rows = 0, 0
    for msg in messages:
        for text, _ in lines_of(msg):
            width = max(width, meter.width(text))
        rows = max([rows] + page_lines(msg))
    return width, rows


def reading_form(msg, meter, max_width):
    """El mensaje con los saltos sueltos cambiados por un espacio."""
    lines = lines_of(msg)
    prose = msg.lstrip().startswith(("〉", PAGE)) or bool(re.search(r"[.!?]\s|[.!?]$", TOKEN.sub(" ", msg)))
    out = []
    for i, (text, broke) in enumerate(lines):
        out.append(text)
        if not broke:
            continue
        nxt = lines[i + 1][0] if i + 1 < len(lines) else ""
        visible_next = TOKEN.sub("", nxt)
        soft = (
            prose and visible_next.strip() and not nxt.startswith(PAGE) and not visible_next.startswith("〉")
            and TOKEN.sub("", text).strip()
            and (visible_next[:1].islower()
                 or (not TOKEN.sub("", text).rstrip().endswith(SENTENCE_END)
                     and meter.width(text) >= 0.75 * max_width))
        )
        out.append(" " if soft else BR)
    joined = "".join(out)
    joined = re.sub(r" {2,}", " ", joined)
    return joined + (END if msg.endswith(END) else "")


def wrap(msg, meter, max_width):
    """Parte por palabras los renglones que pasan del ancho máximo."""
    out = []
    for text, broke in lines_of(msg):
        if meter.width(text) <= max_width:
            out.append(text + (BR if broke else ""))
            continue
        text = SPEAKER.sub(lambda m: m.group().replace(" ", "\0"), text)   # el nombre no se corta
        words, cur = text.split(" "), ""
        pieces = []
        for w in words:
            trial = w if not cur else cur + " " + w
            if cur and meter.width(trial) > max_width:
                pieces.append(cur)
                cur = w
            else:
                cur = trial
        pieces.append(cur)
        out.append(BR.join(pieces).replace("\0", " ") + (BR if broke else ""))
    return "".join(out) + (END if msg.endswith(END) else "")


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "stats":
        from mbm import Mbm
        root = Path(sys.argv[2])
        meter = Meter(root / MEASURE_FONT)
        m = Mbm((root / sys.argv[3]).read_bytes())
        msgs = [m.texts[i] for i in m.order]
        w, r = limits(meter, msgs)
        print(f"ancho máximo {w} px, {r} renglones por página")
        for t in msgs[:8]:
            print("  ", reading_form(t, meter, w))
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
