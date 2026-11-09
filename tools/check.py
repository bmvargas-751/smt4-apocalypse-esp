#!/usr/bin/env python3
"""Validador: los chequeos mecánicos de la traducción, cada uno con su regla.

    python3 tools/check.py NOMBRE_DE_LOTE      las líneas de un lote (y escribe checks.jsonl)
    python3 tools/check.py --all               toda la traducción

Cada aviso trae la clave, el chequeo, la regla (STYLE.md, TECH.md o
GLOSSARY.md) y el detalle. Los chequeos generales vienen de THL; los de
códigos, saltos, caja, bytes y caracteres son de IVA.
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
import layout  # noqa: E402
import tbb  # noqa: E402

EN_WORDS = re.compile(r"\b(the|you|and|what|this|that|is|are|was|don't|I'm|it's|with|for|have|just|gonna)\b", re.I)
SENTENCE = re.compile(r"[a-záéíóúñ']{3,} [a-záéíóúñ']{3,}")
SPACING = re.compile(r"  |\s+[,.;:!?](?![.\d])|\.\.\.\.")
VOSOTROS = re.compile(
    r"\b(?:vosotr[oa]s|vuestr[oa]s?|os)\b"
    r"|\b(?!samuráis\b)\w+(?:áis|éis)\b"
    r"|\b(?!(?:\w*(?:dad|tad)|pared|red|sed|usted|merced|césped|huésped|Madrid|David|Brigid|lid|vid|ardid|adalid)\b)"
    r"\w{2,}(?:ad|ed|id)(?:me|nos|lo|la|los|las|le|les)?(?=\s*[!.,?…]|\s*$)"
    r"|\b(?!caos\b)\w{3,}aos\b|\bidos\b"
    r"|\b(?:estad|venid|mirad|esperad|escuchad|dejad|tened|haced|decid|poned|salid|seguid|volved|traed|sacad|id a)\b",
    re.I)
REGIONAL = re.compile(
    r"\b(vale(?! del compendio)|tío|tía|venga|guay|mola\w*|coger|cog[ií]\w*|ordenador|móvil|pasta(?! de dientes| dental)|majo|maja|gilipollas|joder|"
    r"hostia\w*|pillar|pill[eé]\w*|flipa\w*|chaval\w*|enfad\w+|puls(?:a|as|ar|ando|ado|aste|e|en|ó)|vídeos?|ratón|bombona|"
    r"gafas|bañador\w*|nevera\w*|fard(?:ar|ando|ado|aba\w*|ó|a|as|an|e|es|en)|moter[oa]s?|tragaperras|aparc\w+|jerséis|jersey|"
    r"auriculares|setas?|coches?|cubos? de basura|marcapáginas|ambientador\w*|megafonía)\b", re.I)
LATAM = re.compile(
    r"¿ya\?|\b(fome|qué lata|plata|tomar desayuno|chido|bac[aá]n|boludo|wey|pana|harto|(?-i:po)|cachai|recién|qué onda|nomás)\b",
    re.I)
Y_E = re.compile(r"(?<![\w])[yY] (?=[hH]?[iíIÍ](?![aeouáéóú]))")
O_U = re.compile(r"(?<![\w])[oO] (?=[hH]?[oóOÓ])")
PERCENT = re.compile(r"\d %")


def visible(s):
    return layout.TOKEN.sub(" ", s).replace("\n", " ")


def tags(s):
    return [t for t in layout.TOKEN.findall(s) if t != layout.BR]


def term_rx(t_es):
    """El término del glosario con su plural, su género o su conjugación.

    Cada palabra larga pierde su terminación (-o, -a, -es, -ar...) y acepta
    cualquier otra: «Estado alterado» acepta «estados alterados», «Físico»
    acepta «físicas» y «registrar» acepta «registro».
    """
    parts = []
    for w in re.split(r"\s+", plain(t_es.strip())):
        if len(w) > 4 and w.isalpha():
            stem = re.sub(r"(?:es|os|as|ar|er|ir|[aeos])$", "", w)
            parts.append(re.escape(stem) + r"\w*")
        elif w.isalpha() and len(w) > 2:
            parts.append(re.escape(w) + r"(?:s|es)?")  # plural de palabras cortas: Hada, Hadas
        else:
            parts.append(re.escape(w))
    return re.compile(r"(?<!\w)" + r"\s+".join(parts) + r"(?!\w)", re.I)


def plain(s):
    """Sin tildes, para comparar «Magia» con «mágico»."""
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()


def check(key, es):
    eng = corpus.english()[key]
    kind = corpus.kind_of(key)
    en = corpus.reading_en(key)
    out = []

    def warn(name, rule, detail):
        out.append({"key": key, "check": name, "regla": rule, "detalle": detail})

    if not es.strip():
        warn("vacia", "T-8", "sin texto")
        return out
    ven, ves = visible(en), visible(es)
    if es == en and SENTENCE.search(ven):
        warn("sin_traducir", "T-8", "igual al inglés")
        return out
    if len(EN_WORDS.findall(ves)) >= 3 and len(EN_WORDS.findall(ves)) >= len(ves.split()) / 4:
        warn("ingles_mezclado", "T-8", "parece tener frases en inglés")

    m = corpus.meter()
    if kind == "mbm":
        if tags(en) != tags(es):
            warn("codigos", "T-1", f"inglés {' '.join(tags(en)) or '-'} | español {' '.join(tags(es)) or '-'}")
        if en.count(layout.BR) != es.count(layout.BR):
            warn("saltos", "T-2", f"saltos fijos: inglés {en.count(layout.BR)}, español {es.count(layout.BR)}")
        width, rows = corpus.file_limits(corpus.rel_of(key))
        wrapped = layout.wrap(es, m, width)
        if max(layout.page_lines(wrapped)) > rows:
            warn("caja", "T-3", f"{max(layout.page_lines(wrapped))} renglones en una página (máximo {rows})")
        lines = es.replace(layout.BR, " ").replace("{F802}", " ")  # un salto separa palabras
        too_wide = [w for w in re.split(r"[ \n]", layout.TOKEN.sub("", lines)) if m.width(w) > width]
        if too_wide:
            warn("caja", "T-3", f"palabra más ancha que la caja: {too_wide[0]}")
    else:
        try:
            n = len(tbb.encode(es))
            if n > eng["max"]:
                warn("bytes", "T-4", f"{n} bytes, el máximo es {eng['max']}")
        except UnicodeEncodeError as e:
            warn("caracteres", "T-5", f"no se puede escribir en la tabla: {e.object[e.start:e.end]}")
        _, t, _, o = re.match(r"(.*)#(\d+)\.(\d+)\.(\d+)$", key).groups()
        cw = corpus.column_width(corpus.rel_of(key), int(t), int(o))
        wide = [line for line in es.split("\n") if m.width(line) > cw]
        if wide:
            warn("ancho", "T-3", f"renglón de {m.width(wide[0])} px; el inglés de esta columna llega a {cw}")
        if es.count("\n") > en.count("\n"):
            warn("renglones", "T-3", f"{es.count(chr(10)) + 1} renglones; el inglés tiene {en.count(chr(10)) + 1}")
    if Counter(re.findall(r"%[sd]", en)) != Counter(re.findall(r"%[sd]", es)):
        warn("codigos", "T-1", "los %d o %s no coinciden con el inglés")
    missing = m.missing(es)
    if missing:
        warn("caracteres", "T-5", "la fuente no tiene: " + " ".join(missing))

    if not re.match(r"[\s.…—]*[a-záéíóúñ]", ves.strip()):
        # «?» suelto, tras «x», tras coma o entre comillas («???») es un valor desconocido, no una pregunta
        if len(re.findall(r"(?<![\sx,(/?“\"«])\?", " " + ves)) > ves.count("¿"):
            warn("falta_apertura", "E-52", "falta ¿")
        if len(re.findall(r"(?<!\s)!", " " + ves)) > ves.count("¡"):  # «!» suelto es un marcador, no una exclamación
            warn("falta_apertura", "E-52", "falta ¡")
    if SPACING.search(layout.TOKEN.sub("X", es)) and not SPACING.search(layout.TOKEN.sub("X", en)):  # un código ocupa su lugar
        warn("espacios", "E-54", "espacios o puntos de más")
    if PERCENT.search(ves):
        warn("porcentaje", "E-57", "porcentaje con espacio")
    if re.search(r"[“”\"]", ven) and not re.search(r"[“”]", ves):
        warn("comillas", "E-58", "el inglés tiene comillas y el español no")
    for name, rule, rx in (("vosotros", "E-11", VOSOTROS), ("regional", "E-12", REGIONAL),
                           ("regional", "E-13", LATAM)):
        found = sorted({x.group(0).lower() for x in rx.finditer(ves)})
        if found:
            warn(name, rule, ", ".join(found))
    for name, rule, rx in (("y_e", "E-51", Y_E), ("o_u", "E-51", O_U)):
        hit = rx.search(ves)
        if hit:
            warn(name, rule, ves[hit.start():hit.start() + 20])
    le, ls = len(ven), len(ves)
    if ls > le * 1.6 + 20:
        warn("largo", "E-3", f"{ls} caracteres; el inglés tiene {le}")
    for t_en, t_es in corpus.glossary():
        if re.search(rf"(?<![A-Za-z]){re.escape(t_en)}(?![A-Za-z])", ven) and not term_rx(t_es).search(plain(ves)):
            warn("glosario", "G-3", f"{t_en} → {t_es}")
    return out


def run(keys, done):
    warnings = []
    for k in keys:
        if k in done:
            warnings += check(k, done[k])
        else:
            warnings.append({"key": k, "check": "vacia", "regla": "T-8", "detalle": "sin traducción"})
    return warnings


def main():
    a = argparse.ArgumentParser()
    a.add_argument("batch", nargs="?")
    a.add_argument("--all", action="store_true")
    args = a.parse_args()
    done = corpus.translations()
    if args.all:
        keys = [k for k in corpus.english() if k in done]
    elif args.batch:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from batch import batch_dir, load_batch
        keys = [it["key"] for it in load_batch(args.batch)["items"]]
    else:
        sys.exit(__doc__)
    warnings = run(keys, done)
    if args.batch:
        with open(batch_dir(args.batch) / "checks.jsonl", "w", encoding="utf-8") as w:
            for x in warnings:
                w.write(json.dumps(x, ensure_ascii=False) + "\n")
    for x in warnings:
        print(f"{x['key']}  {x['check']} [{x['regla']}]  {x['detalle']}")
    summary = Counter(x["check"] for x in warnings)
    print(f"{len(keys)} líneas, {len(warnings)} avisos" + (f": {dict(summary)}" if summary else ""))


if __name__ == "__main__":
    main()
