"""Arma los archivos traducidos a partir de la copia del jugador.

Lee de la imagen solo los archivos que cambian: las fuentes (a las que se les
dibujan las letras españolas), los mensajes (.mbm) y las tablas (.tbb) que
tienen traducción en `translation/` (y en `tests/`, si se pide).
Devuelve {ruta en el RomFS: bytes}.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mbm  # noqa: E402
import tbb  # noqa: E402
from ctr import Image, InvalidImage  # noqa: E402
from font import FONTS, compose  # noqa: E402

GAME_ID = 0x00040000001A6B00           # versión europea
REPO = Path(__file__).resolve().parent.parent


def jsonl_files(folder):
    return sorted(folder.rglob("*.jsonl")) if folder.is_dir() else []


def read_translations(paths):
    """{archivo del juego: {clave interna: texto}}; los últimos JSONL pisan a los primeros."""
    out = {}
    for path in paths:
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            if not line.strip():
                continue
            d = json.loads(line)
            rel, sub = d["key"].rsplit("#", 1)
            if rel.endswith(".mbm"):
                if not d["es"].endswith("{FFFF}"):
                    raise ValueError(f"{path}:{n}: el texto debe terminar en {{FFFF}}")
                key = int(sub)
            elif rel.endswith(".tbb"):
                key = tuple(int(x) for x in sub.split("."))
            else:
                raise ValueError(f"{path}:{n}: no sé aplicar textos a {rel}")
            out.setdefault(rel, {})[key] = d["es"]
    return out


def build(rom, test=False, log=print):
    img = Image(rom)
    if img.program_id != GAME_ID:
        raise InvalidImage(f"esta copia es {img.product} ({img.program_id:016X}); por ahora la "
                           f"traducción es para la versión europea ({GAME_ID:016X})")
    files = {}
    log("Dibujando las letras españolas en las fuentes...")
    for name in FONTS:
        rel = f"font/{name}.bcfnt"
        files[rel] = compose(img.read_file(rel))
    sources = jsonl_files(REPO / "translation") + (jsonl_files(REPO / "tests") if test else [])
    texts = read_translations(sources)
    log(f"Aplicando la traducción ({sum(len(t) for t in texts.values())} textos)...")
    for rel, changes in sorted(texts.items()):
        if rel not in img.files():
            raise ValueError(f"{rel}: ese archivo no está en el juego")
        tool = mbm if rel.endswith(".mbm") else tbb
        files[rel] = tool.apply_texts(img.read_file(rel), changes, rel)
    return files
