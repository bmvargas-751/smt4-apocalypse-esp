#!/usr/bin/env python3
"""Adaptador del kit de traducción de juegos: escribe el original en el formato común del kit.

    python3 tools/kit_adapter.py export [SALIDA]

Por defecto escribe ../local/smt4-apocalypse/kit-source.jsonl (el «source» de loc.json): una línea
{key, en, max?} por texto, en el orden del juego. Los mensajes van en forma de lectura
(TECH.md, T-2), como los ve el traductor; las tablas y el ejecutable llevan su «max» en
bytes (T-4). Se lee de la extracción local, igual que las demás herramientas
(corpus.english), así que hay que volver a exportar si cambia la extracción.

La traducción no necesita adaptador: translation/ ya tiene el formato del kit ({key, es}).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402


def export(out):
    n = 0
    with open(out, "w", encoding="utf-8") as w:
        for key, d in corpus.english().items():
            row = {"key": key, "en": corpus.reading_en(key)}
            if d.get("max") is not None:
                row["max"] = d["max"]
            w.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
    print(f"{n} textos en {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "export":
        sys.exit(__doc__)
    export(Path(sys.argv[2]) if len(sys.argv) > 2 else corpus.LOCAL / "kit-source.jsonl")
