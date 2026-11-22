"""Hooks del kit de traducción de juegos para SMT IV: Apocalypse (loc.json, «hooks»).

El kit cuenta, mide y revisa igual que las herramientas de este repo, porque usa las mismas:

  section(key), excluded(key, item)   las secciones y exclusiones de tools/progress.py
  encode(key, es)                     los bytes de las tablas y del ejecutable (T-4), con tools/tbb.py
  check(key, item, es)                la caja y el ancho en píxeles (T-3) y la fuente (T-5), con tools/check.py

La traducción ya está en el formato del kit (translation/, {key, es}): no hacen falta
read_translation ni write_translation.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check as smt_check  # noqa: E402
import corpus as smt_corpus  # noqa: E402
import progress as smt_progress  # noqa: E402
import tbb  # noqa: E402

# lo demás (códigos, saltos, bytes, español neutro, glosario) ya lo revisa el kit
OWN = {"caja", "ancho", "renglones"}


def section(key):
    return smt_progress.section_of(key.rsplit("#", 1)[0])


def excluded(key, item):
    if section(key) is None:
        return True
    raw = smt_corpus.english().get(key, {}).get("en", "")
    return smt_progress.excluded(key, raw)


def encode(key, es):
    return tbb.encode(es)


def check(key, item, es):
    out = []
    for w in smt_check.check(key, es):
        if w["check"] in OWN or (w["check"] == "caracteres" and w["detalle"].startswith("la fuente no tiene")):
            out.append((w["check"], w["regla"], w["detalle"]))
    return out
