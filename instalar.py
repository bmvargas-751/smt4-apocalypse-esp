#!/usr/bin/env python3
"""Instalador de la traducción al español de Shin Megami Tensei IV: Apocalypse.

Con doble clic en instalar.bat (Windows), o desde una terminal:

    python3 instalar.py                                  menú
    python3 instalar.py --rom JUEGO.3ds --destino azahar|citra|sd [--carpeta RUTA] [--prueba]
    python3 instalar.py --desinstalar --destino azahar|citra|sd [--carpeta RUTA]

Arma los archivos traducidos desde tu propia copia del juego (versión europea,
.3ds/.cci o .cxi descifrado) y los copia a:
  azahar, citra  la carpeta de mods del emulador (load/mods/00040000001A6B00);
                 --carpeta indica la carpeta de usuario si no se encuentra sola
  sd             la SD de una 3DS con Luma3DS (luma/titles/00040000001A6B00);
                 --carpeta es la raíz de la SD
--prueba agrega los textos de prueba de pruebas/.
Desinstalar borra solo los archivos que instaló este programa.
"""
import argparse
import datetime
import json
import os
import platform
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI / "tools"))
from ctr import ImagenInvalida  # noqa: E402
from parche import ID_JUEGO, construir  # noqa: E402

TITULO = f"{ID_JUEGO:016X}"
MANIFIESTO = "traduccion-es.json"
CONFIG = AQUI / "instalar.json"
EMULADORES = {
    "azahar": {"nombre": "Azahar", "windows": "Azahar", "linux": "azahar-emu", "mac": "Azahar"},
    "citra": {"nombre": "Citra", "windows": "Citra", "linux": "citra-emu", "mac": "Citra"},
}


class Error(Exception):
    pass


# ---------- dónde instalar ----------

def es_wsl():
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except OSError:
        return False


def carpetas_de_usuario(emu):
    """Carpetas de usuario posibles del emulador, de la más probable a la menos."""
    e = EMULADORES[emu]
    sistema = platform.system()
    candidatas = []
    if sistema == "Windows" and os.environ.get("APPDATA"):
        candidatas.append(Path(os.environ["APPDATA"]) / e["windows"])
    elif sistema == "Darwin":
        candidatas.append(Path.home() / "Library" / "Application Support" / e["mac"])
    else:
        datos = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
        candidatas.append(datos / e["linux"])
        if es_wsl():
            candidatas += sorted(Path("/mnt/c/Users").glob(f"*/AppData/Roaming/{e['windows']}"))
    return [c for c in candidatas if c.is_dir()]


def destino_de(tipo, carpeta=None, preguntar=None):
    """Carpeta donde va la traducción (la que contiene romfs/)."""
    if tipo == "sd":
        if not carpeta:
            raise Error("falta la raíz de la SD (--carpeta)")
        return Path(carpeta) / "luma" / "titles" / TITULO
    if carpeta:
        usuario = Path(carpeta)
    else:
        encontradas = carpetas_de_usuario(tipo)
        if len(encontradas) == 1:
            usuario = encontradas[0]
        elif encontradas and preguntar:
            usuario = Path(preguntar("¿Cuál?", [str(c) for c in encontradas]))
        else:
            nombre = EMULADORES[tipo]["nombre"]
            raise Error(f"no encontré la carpeta de usuario de {nombre}; indícala con --carpeta "
                        f"(es la que tiene load, sdmc y config)")
    if not usuario.is_dir():
        raise Error(f"no existe la carpeta {usuario}")
    return usuario / "load" / "mods" / TITULO


# ---------- instalar y desinstalar ----------

def desinstalar(destino, aviso=print):
    manifiesto = destino / MANIFIESTO
    if not manifiesto.exists():
        raise Error(f"no hay una traducción instalada por este programa en {destino}")
    romfs = destino / "romfs"
    for rel in json.loads(manifiesto.read_text(encoding="utf-8"))["archivos"]:
        (romfs / rel).unlink(missing_ok=True)
    for d in sorted((p for p in romfs.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    if romfs.is_dir() and not any(romfs.iterdir()):
        romfs.rmdir()
    manifiesto.unlink()
    if destino.is_dir() and not any(destino.iterdir()):
        destino.rmdir()
    aviso(f"Traducción desinstalada de {destino}")


def instalar(rom, destino, prueba=False, aviso=print):
    romfs = destino / "romfs"
    if not (destino / MANIFIESTO).exists() and romfs.is_dir() and any(romfs.rglob("*")):
        raise Error(f"ya hay otro mod en {romfs}; quítalo antes de instalar la traducción")
    archivos = construir(rom, prueba=prueba, aviso=aviso)
    if (destino / MANIFIESTO).exists():
        desinstalar(destino, aviso=lambda _: None)
    for rel, datos in archivos.items():
        (romfs / rel).parent.mkdir(parents=True, exist_ok=True)
        (romfs / rel).write_bytes(datos)
    (destino / MANIFIESTO).write_text(json.dumps({
        "juego": TITULO,
        "instalado": datetime.datetime.now().isoformat(timespec="seconds"),
        "prueba": prueba,
        "archivos": sorted(archivos),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    aviso(f"Listo: {len(archivos)} archivos en {romfs}")


# ---------- menú ----------

def leer_config():
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def guardar_config(cfg):
    try:
        CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    except OSError:
        pass


def elegir(pregunta, opciones):
    print(pregunta)
    for i, o in enumerate(opciones, 1):
        print(f"  {i}) {o}")
    while True:
        r = input("> ").strip()
        if r.isdigit() and 1 <= int(r) <= len(opciones):
            return opciones[int(r) - 1]


def ruta(pregunta, anterior=None):
    extra = f" [Enter: {anterior}]" if anterior else ""
    r = input(f"{pregunta}{extra}\n> ").strip().strip('"').strip("'")
    return r or anterior


def menu(prueba):
    print("Traducción al español de Shin Megami Tensei IV: Apocalypse\n")
    cfg = leer_config()
    lugares = {"Azahar": "azahar", "Citra": "citra", "La SD de una 3DS (Luma3DS)": "sd"}
    accion = elegir("¿Qué quieres hacer?", ["Instalar", "Desinstalar", "Salir"])
    if accion == "Salir":
        return
    tipo = lugares[elegir("¿Dónde?", list(lugares))]
    if tipo == "sd":
        cfg["sd"] = ruta("Raíz de la SD (por ejemplo E:\\):", cfg.get("sd"))
        destino = destino_de("sd", cfg["sd"])
    else:
        try:
            destino = destino_de(tipo, cfg.get(tipo), preguntar=elegir)
        except Error as e:
            print(f"No pude encontrarla sola: {e}")
            cfg[tipo] = ruta("Carpeta de usuario del emulador:", cfg.get(tipo))
            destino = destino_de(tipo, cfg[tipo])
    if accion == "Desinstalar":
        desinstalar(destino)
    else:
        rom = ruta("Arrastra aquí tu copia del juego (.3ds) y presiona Enter:", cfg.get("rom"))
        cfg["rom"] = rom
        instalar(rom, destino, prueba=prueba)
        if tipo == "sd":
            print("En la 3DS, activa «Enable game patching» en la configuración de Luma3DS "
                  "(mantén SELECT al encenderla).")
    guardar_config(cfg)


def main():
    a = argparse.ArgumentParser(description="Instala la traducción al español de SMT IV: Apocalypse.")
    a.add_argument("--rom", help="tu copia del juego (.3ds o .cxi descifrado)")
    a.add_argument("--destino", choices=["azahar", "citra", "sd"])
    a.add_argument("--carpeta", help="carpeta de usuario del emulador, o raíz de la SD")
    a.add_argument("--desinstalar", action="store_true")
    a.add_argument("--prueba", action="store_true", help="agrega los textos de pruebas/")
    args = a.parse_args()
    try:
        if not args.destino:
            menu(args.prueba)
        elif args.desinstalar:
            desinstalar(destino_de(args.destino, args.carpeta))
        else:
            if not args.rom:
                raise Error("falta --rom")
            instalar(args.rom, destino_de(args.destino, args.carpeta), prueba=args.prueba)
    except (Error, ImagenInvalida, ValueError, OSError) as e:
        sys.exit(f"Error: {e}")
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nCancelado.")


if __name__ == "__main__":
    main()
