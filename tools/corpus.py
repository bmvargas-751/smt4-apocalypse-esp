"""El texto del juego y la traducción, para los scripts del lote.

Lo del juego se lee de la extracción local (../smt4a-local: romfs/, en.jsonl y
tbb.jsonl); la traducción, de translation/. Una clave es «archivo#número» en
los mensajes y «archivo#tabla.registro.posición» en las tablas.
La traducción de los mensajes se guarda en forma de lectura (ver layout.py).
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layout  # noqa: E402
from bcfnt import Bcfnt  # noqa: E402
from font import compose  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
LOCAL = REPO.parent / "smt4a-local"
ROMFS = LOCAL / "romfs"
TRANSLATION = REPO / "translation"


def rel_of(key):
    return key.rsplit("#", 1)[0]


def kind_of(key):
    return "tbb" if rel_of(key).endswith(".tbb") else "mbm"


def translation_file(rel):
    return TRANSLATION / f"{rel}.jsonl"


@lru_cache(maxsize=1)
def english():
    """{clave: {"en": texto original, "max": bytes (tablas)}} en el orden del juego."""
    out = {}
    for name in ("en.jsonl", "tbb.jsonl"):
        path = LOCAL / name
        if not path.exists():
            tool = "mbm" if name == "en.jsonl" else "tbb"
            sys.exit(f"No encuentro {path}; créalo con: python3 tools/{tool}.py export ROMFS {path}")
        for line in open(path, encoding="utf-8"):
            d = json.loads(line)
            out[d["key"]] = {"en": d["en"], "max": d.get("max")}
    return out


@lru_cache(maxsize=1)
def meter():
    """Medidor con la fuente de medir ya con las letras españolas."""
    data = (ROMFS / layout.MEASURE_FONT).read_bytes()
    return layout.Meter(Bcfnt(compose(data)))


@lru_cache(maxsize=None)
def file_limits(rel):
    """(ancho máximo en px, renglones por página) del inglés de un archivo de mensajes."""
    msgs = [v["en"] for k, v in english().items() if rel_of(k) == rel]
    return layout.limits(meter(), msgs)


def reading_en(key):
    """El inglés como lo ve el traductor."""
    en = english()[key]["en"]
    if kind_of(key) == "tbb":
        return en
    return layout.reading_form(en, meter(), file_limits(rel_of(key))[0])


@lru_cache(maxsize=None)
def column_width(rel, table, offset):
    """Ancho en px del renglón más ancho del inglés en una columna de tabla."""
    prefix = f"{rel}#{table}."
    w = 0
    for k, v in english().items():
        if k.startswith(prefix) and k.endswith(f".{offset}"):
            for line in v["en"].split("\n"):
                w = max(w, meter().width(line))
    return w


def translations():
    """{clave: texto} de todo translation/."""
    out = {}
    for path in sorted(TRANSLATION.rglob("*.jsonl")):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                out[d["key"]] = d["es"]
    return out


def save(changes):
    """Escribe {clave: texto} en translation/, un archivo por archivo del juego, en el orden del juego."""
    order = {k: i for i, k in enumerate(english())}
    by_file = {}
    for k, es in changes.items():
        by_file.setdefault(rel_of(k), {})[k] = es
    for rel, items in by_file.items():
        path = translation_file(rel)
        current = {}
        if path.exists():
            for line in open(path, encoding="utf-8"):
                if line.strip():
                    d = json.loads(line)
                    current[d["key"]] = d["es"]
        current.update(items)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as w:
            for k in sorted(current, key=lambda k: order.get(k, 1 << 30)):
                w.write(json.dumps({"key": k, "es": current[k]}, ensure_ascii=False) + "\n")


def glossary():
    """[(inglés, español)] de la tabla de GLOSSARY.md."""
    out = []
    path = REPO / "GLOSSARY.md"
    if not path.exists():
        return out
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Inglés |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and cells[0] and not set(cells[0]) <= set("-:"):
                out.append((cells[0], cells[1]))
    return out


def rule_ids():
    """Los números de regla de STYLE.md, TECH.md y GLOSSARY.md (E-1, T-3, G-2...)."""
    ids = set()
    for name in ("STYLE.md", "TECH.md", "GLOSSARY.md"):
        path = REPO / name
        if path.exists():
            ids |= set(re.findall(r"\*\*([ETG]-\d+)\*\*", path.read_text(encoding="utf-8")))
    return ids
