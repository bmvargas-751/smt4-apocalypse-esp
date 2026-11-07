"""Arma los archivos traducidos a partir de la copia del jugador.

Lee de la imagen solo los archivos que cambian: las fuentes (a las que se les
dibujan las letras españolas) y los .mbm que tienen traducción en
`translation/` (y en `tests/`, si se pide). Devuelve {ruta en el RomFS: bytes}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ctr import Image, InvalidImage  # noqa: E402
from font import FONTS, compose  # noqa: E402
from mbm import apply_texts, read_texts  # noqa: E402

GAME_ID = 0x00040000001A6B00           # versión europea
REPO = Path(__file__).resolve().parent.parent


def jsonl_files(folder):
    return sorted(folder.rglob("*.jsonl")) if folder.is_dir() else []


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
    texts = read_texts(sources)
    log(f"Aplicando la traducción ({sum(len(t) for t in texts.values())} mensajes)...")
    for rel, changes in sorted(texts.items()):
        if rel not in img.files():
            raise ValueError(f"{rel}: ese archivo no está en el juego")
        files[rel] = apply_texts(img.read_file(rel), changes, rel)
    return files
