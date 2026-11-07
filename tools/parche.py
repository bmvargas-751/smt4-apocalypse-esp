"""Arma los archivos traducidos a partir de la copia del jugador.

Lee de la imagen solo los archivos que cambian: las fuentes (a las que se les
dibujan las letras españolas) y los .mbm que tienen traducción en
`traduccion/` (y en `pruebas/`, si se pide). Devuelve {ruta en el RomFS: bytes}.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ctr import Image, ImagenInvalida  # noqa: E402
from fuente import FUENTES, componer  # noqa: E402
from mbm import aplicar, leer_textos  # noqa: E402

ID_JUEGO = 0x00040000001A6B00          # versión europea
REPO = Path(__file__).resolve().parent.parent


def jsonl_de(carpeta):
    return sorted(carpeta.rglob("*.jsonl")) if carpeta.is_dir() else []


def construir(rom, prueba=False, aviso=print):
    img = Image(rom)
    if img.program_id != ID_JUEGO:
        raise ImagenInvalida(f"esta copia es {img.product} ({img.program_id:016X}); por ahora la "
                             f"traducción es para la versión europea ({ID_JUEGO:016X})")
    archivos = {}
    aviso("Dibujando las letras españolas en las fuentes...")
    for nombre in FUENTES:
        rel = f"font/{nombre}.bcfnt"
        archivos[rel] = componer(img.read_file(rel))
    fuentes_texto = jsonl_de(REPO / "traduccion") + (jsonl_de(REPO / "pruebas") if prueba else [])
    textos = leer_textos(fuentes_texto)
    aviso(f"Aplicando la traducción ({sum(len(t) for t in textos.values())} mensajes)...")
    for rel, cambios in sorted(textos.items()):
        if rel not in img.files():
            raise ValueError(f"{rel}: ese archivo no está en el juego")
        archivos[rel] = aplicar(img.read_file(rel), cambios, rel)
    return archivos
