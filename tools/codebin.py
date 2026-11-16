#!/usr/bin/env python3
"""Textos del ejecutable (exefs/code.bin, ya descomprimido): exportar, ida y vuelta y parche IPS.

    python3 tools/codebin.py export    CODE.bin SALIDA.jsonl
    python3 tools/codebin.py roundtrip CODE.bin
    python3 tools/codebin.py ips       CODE.bin TRADUCCION.jsonl... SALIDA.ips [--fullwidth]

Los textos están en Shift-JIS de ancho completo («Ｆｉｒｅ»), terminados en 00, y el
código los busca con direcciones relativas al PC, sin tabla de punteros: cada
traducción tiene que caber en el lugar del original. Ese lugar es el texto, su 00
y el relleno de ceros hasta el siguiente múltiplo de 4; lo que sigue puede ser
código o datos, y no se toca.

La traducción se escribe como en las tablas: letras de un byte (ASCII) y las
españolas con los códigos de letters.py (2 bytes). Con --fullwidth, en ancho
completo como el inglés (ocupa el doble).

Clave de cada texto: «exefs/code.bin#0xOFFSET» (posición en el archivo; la dirección
en memoria es 0x100000 + OFFSET, porque los tres segmentos van seguidos).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letters import BY_CODE, SPANISH  # noqa: E402

PREFIX = "exefs/code.bin"
# Letras y números de ancho completo (Ａ-Ｚ, ａ-ｚ, ０-９): marcan un texto en inglés.
FULL_LATIN = re.compile(rb"\x82[\x4f-\x9a]")
JAPANESE = re.compile("[぀-ヿ一-鿿]")
WORD = re.compile("[A-Za-z]{2}")


def key(off):
    return f"{PREFIX}#0x{off:X}"


def offset(k):
    return int(k.split("#", 1)[1], 16)


def decode(raw):
    """Shift-JIS (con las letras españolas) a texto legible: el ancho completo pasa a ASCII."""
    out, i = [], 0
    while i < len(raw):
        c = raw[i]
        if c < 0x80 or 0xA1 <= c <= 0xDF:
            out.append(raw[i:i + 1].decode("cp932"))
            i += 1
            continue
        if i + 1 >= len(raw):
            raise ValueError("carácter cortado")
        code = c << 8 | raw[i + 1]
        out.append(BY_CODE.get(code) or raw[i:i + 2].decode("cp932"))
        i += 2
    s = "".join(out)
    return "".join(" " if ch == "　" else chr(ord(ch) - 0xFEE0) if "！" <= ch <= "～" else ch
                   for ch in s)


def encode(s, fullwidth=False):
    out = bytearray()
    for ch in s:
        if ch in SPANISH:
            out += SPANISH[ch].to_bytes(2, "big")
        elif fullwidth and ch == " ":
            out += "　".encode("cp932")
        elif fullwidth and "!" <= ch <= "~":
            out += chr(ord(ch) + 0xFEE0).encode("cp932")
        else:
            out += ch.encode("cp932")
    return bytes(out)


# Prefijo de un byte que puede ir antes de la primera letra de ancho completo: un dato del juego.
FORMAT_PREFIX = re.compile(rb"%[-0-9]*[sdux] ?$")


def start(code, i):
    """Dónde empieza el texto que contiene la letra de ancho completo de `i`.

    Se retrocede solo sobre caracteres de dos bytes de Shift-JIS (0x81-0x84); antes
    puede venir código o datos sin un 00 en medio («Heal» va justo después de una
    instrucción), así que el ASCII suelto no cuenta, salvo un formato como «%s ».
    """
    while i >= 2 and 0x81 <= code[i - 2] <= 0x84 and 0x40 <= code[i - 1] <= 0xFC and code[i - 1] != 0x7F:
        i -= 2
    head = code[max(0, i - 8):i]
    m = FORMAT_PREFIX.search(head)
    if m and (i - len(head) + m.start() == 0 or code[i - len(head) + m.start() - 1] == 0):
        i -= len(head) - m.start()
    return i


def find_texts(code):
    """Los textos en inglés: [(offset, largo, lugar)], con el lugar en bytes sin el 00 final."""
    found, seen = [], set()
    for m in FULL_LATIN.finditer(code):
        s = start(code, m.start())
        if s in seen or (found and s < found[-1][0] + found[-1][1]):
            continue
        e = code.find(b"\0", m.start())
        raw = code[s:e]
        seen.add(s)
        if len(FULL_LATIN.findall(raw)) < 2:
            continue
        try:
            text = decode(raw)
        except (ValueError, UnicodeDecodeError):
            continue
        if JAPANESE.search(text) or any(ord(ch) < 0x20 for ch in text):
            continue
        # Sin dos letras seguidas no hay qué traducir (pisos «B1F», rangos «10~19», cifras,
        # datos que parecen texto); la tabla de conversión a ancho completo es del juego.
        if not WORD.search(text) or "ABCDEFGHIJKLMNOPQRSTUVWXYZ" in text:
            continue
        # Lugar: hasta el múltiplo de 4 siguiente al 00, mientras siga habiendo ceros.
        end = (e + 1 + 3) & ~3
        stop = e + 1
        while stop < end and code[stop] == 0:
            stop += 1
        found.append((s, len(raw), stop - s - 1))
    return found


def export(code):
    for off, n, room in find_texts(code):
        yield {"key": key(off), "max": room, "en": decode(code[off:off + n])}


def roundtrip(code):
    """Escribe cada texto original en su lugar (con su 00 y el relleno) y compara con el archivo.

    Devuelve (bytes distintos, textos que mezclan anchos): estos últimos tienen ASCII
    de un byte entre las letras de ancho completo («%s Macca», «Drain: »), así que
    pasarlos todos a ancho completo no daría el original; no es un error.
    """
    new = bytearray(code)
    mixed = 0
    for off, n, room in find_texts(code):
        raw = code[off:off + n]
        mixed += encode(decode(raw), fullwidth=True) != raw
        new[off:off + room + 1] = raw + bytes(room + 1 - len(raw))
    return [hex(i) for i in range(len(code)) if new[i] != code[i]], mixed


def apply(code, texts, fullwidth=False):
    """Escribe las traducciones ({clave: texto}); devuelve (código nuevo, errores)."""
    rooms = {key(off): (off, room) for off, _, room in find_texts(code)}
    new, errors = bytearray(code), []
    for k, s in texts.items():
        if k not in rooms:
            errors.append(f"{k}: no es un texto del ejecutable")
            continue
        off, room = rooms[k]
        try:
            raw = encode(s, fullwidth)
        except UnicodeEncodeError as e:
            errors.append(f"{k}: carácter sin código ({e.object[e.start]!r})")
            continue
        if len(raw) > room:
            errors.append(f"{k}: {len(raw)} bytes, caben {room}")
            continue
        new[off:off + room + 1] = raw + bytes(room + 1 - len(raw))
    return bytes(new), errors


def ips(old, new):
    """Parche IPS con las diferencias (Luma3DS, Azahar y Citra lo aplican al code.bin descomprimido)."""
    out = bytearray(b"PATCH")
    i = 0
    while i < len(new):
        if new[i] == old[i]:
            i += 1
            continue
        j = i
        while j < len(new) and j - i < 0xFFFF and (new[j] != old[j] or new[j + 1:j + 5] != old[j + 1:j + 5]):
            j += 1
        start = i - 1 if i == 0x454F46 else i  # «EOF» como offset se leería como el final
        out += start.to_bytes(3, "big") + (j - start).to_bytes(2, "big") + new[start:j]
        i = j
    if len(out) > 5 and max(len(new), len(old)) > 0xFFFFFF:
        raise ValueError("code.bin demasiado grande para IPS")
    return bytes(out + b"EOF")


def read_jsonl(paths):
    texts = {}
    for p in paths:
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                if r["key"].startswith(PREFIX + "#") and r.get("es"):
                    texts[r["key"]] = r["es"]
    return texts


def main():
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == "export":
        code = Path(a[1]).read_bytes()
        rows = list(export(code))
        with open(a[2], "w", encoding="utf-8") as w:
            for r in rows:
                w.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{len(rows)} textos en {a[2]}")
    elif len(a) == 2 and a[0] == "roundtrip":
        code = Path(a[1]).read_bytes()
        bad, mixed = roundtrip(code)
        n = len(find_texts(code))
        print(f"{n} textos ({mixed} mezclan anchos); "
              + ("ida y vuelta idéntica" if not bad else f"{len(bad)} bytes distintos: {bad[:10]}"))
        sys.exit(1 if bad else 0)
    elif len(a) >= 4 and a[0] == "ips":
        full = "--fullwidth" in a
        a = [x for x in a if x != "--fullwidth"]
        code = Path(a[1]).read_bytes()
        new, errors = apply(code, read_jsonl(a[2:-1]), fullwidth=full)
        for e in errors:
            print(e)
        Path(a[-1]).write_bytes(ips(code, new))
        print(f"{a[-1]}: {sum(1 for i in range(len(code)) if code[i] != new[i])} bytes cambiados")
        sys.exit(1 if errors else 0)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
