#!/usr/bin/env python3
"""Instalador de la traducción al español de Shin Megami Tensei IV: Apocalypse.

Con doble clic en install.bat (Windows), o desde una terminal:

    python3 install.py                                   menú
    python3 install.py --rom JUEGO.3ds --target azahar|citra|sd [--folder RUTA] [--test]
    python3 install.py --uninstall --target azahar|citra|sd [--folder RUTA]

Arma los archivos traducidos desde tu propia copia del juego (versión europea,
.3ds/.cci o .cxi descifrado) y los copia a:
  azahar, citra  la carpeta de mods del emulador (load/mods/00040000001A6B00);
                 --folder indica la carpeta de usuario si no se encuentra sola
  sd             la SD de una 3DS con Luma3DS (luma/titles/00040000001A6B00);
                 --folder es la raíz de la SD
--test agrega los textos de prueba de tests/.
Desinstalar borra solo los archivos que instaló este programa.
"""
import argparse
import datetime
import json
import os
import platform
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "tools"))
from ctr import InvalidImage  # noqa: E402
from patch import GAME_ID, build  # noqa: E402

TITLE_ID = f"{GAME_ID:016X}"
MANIFEST = "smt4a-esp.json"
CONFIG = HERE / "install.json"
EMULATORS = {
    "azahar": {"name": "Azahar", "windows": "Azahar", "linux": "azahar-emu", "mac": "Azahar"},
    "citra": {"name": "Citra", "windows": "Citra", "linux": "citra-emu", "mac": "Citra"},
}


class Error(Exception):
    pass


# ---------- dónde instalar ----------

def is_wsl():
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except OSError:
        return False


def user_dirs(emu):
    """Carpetas de usuario posibles del emulador, de la más probable a la menos."""
    e = EMULATORS[emu]
    system = platform.system()
    candidates = []
    if system == "Windows" and os.environ.get("APPDATA"):
        candidates.append(Path(os.environ["APPDATA"]) / e["windows"])
    elif system == "Darwin":
        candidates.append(Path.home() / "Library" / "Application Support" / e["mac"])
    else:
        data = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
        candidates.append(data / e["linux"])
        if is_wsl():
            candidates += sorted(Path("/mnt/c/Users").glob(f"*/AppData/Roaming/{e['windows']}"))
    return [c for c in candidates if c.is_dir()]


def target_dir(kind, folder=None, ask=None):
    """Carpeta donde va la traducción (la que contiene romfs/)."""
    if kind == "sd":
        if not folder:
            raise Error("falta la raíz de la SD (--folder)")
        return Path(folder) / "luma" / "titles" / TITLE_ID
    if folder:
        user = Path(folder)
    else:
        found = user_dirs(kind)
        if len(found) == 1:
            user = found[0]
        elif found and ask:
            user = Path(ask("¿Cuál?", [str(c) for c in found]))
        else:
            name = EMULATORS[kind]["name"]
            raise Error(f"no encontré la carpeta de usuario de {name}; indícala con --folder "
                        f"(es la que tiene load, sdmc y config)")
    if not user.is_dir():
        raise Error(f"no existe la carpeta {user}")
    return user / "load" / "mods" / TITLE_ID


# ---------- instalar y desinstalar ----------

def uninstall(target, log=print):
    manifest = target / MANIFEST
    if not manifest.exists():
        raise Error(f"no hay una traducción instalada por este programa en {target}")
    romfs = target / "romfs"
    for rel in json.loads(manifest.read_text(encoding="utf-8"))["files"]:
        (romfs / rel).unlink(missing_ok=True)
    for d in sorted((p for p in romfs.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    if romfs.is_dir() and not any(romfs.iterdir()):
        romfs.rmdir()
    manifest.unlink()
    if target.is_dir() and not any(target.iterdir()):
        target.rmdir()
    log(f"Traducción desinstalada de {target}")


def install(rom, target, test=False, log=print):
    romfs = target / "romfs"
    if not (target / MANIFEST).exists() and romfs.is_dir() and any(romfs.rglob("*")):
        raise Error(f"ya hay otro mod en {romfs}; quítalo antes de instalar la traducción")
    files = build(rom, test=test, log=log)
    if (target / MANIFEST).exists():
        uninstall(target, log=lambda _: None)
    for rel, data in files.items():
        (romfs / rel).parent.mkdir(parents=True, exist_ok=True)
        (romfs / rel).write_bytes(data)
    (target / MANIFEST).write_text(json.dumps({
        "game": TITLE_ID,
        "installed": datetime.datetime.now().isoformat(timespec="seconds"),
        "test": test,
        "files": sorted(files),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"Listo: {len(files)} archivos en {romfs}")


# ---------- menú ----------

def load_config():
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_config(cfg):
    try:
        CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    except OSError:
        pass


def choose(question, options):
    print(question)
    for i, o in enumerate(options, 1):
        print(f"  {i}) {o}")
    while True:
        r = input("> ").strip()
        if r.isdigit() and 1 <= int(r) <= len(options):
            return options[int(r) - 1]


def ask_path(question, previous=None):
    extra = f" [Enter: {previous}]" if previous else ""
    r = input(f"{question}{extra}\n> ").strip().strip('"').strip("'")
    return r or previous


def menu(test):
    print("Traducción al español de Shin Megami Tensei IV: Apocalypse\n")
    cfg = load_config()
    places = {"Azahar": "azahar", "Citra": "citra", "La SD de una 3DS (Luma3DS)": "sd"}
    action = choose("¿Qué quieres hacer?", ["Instalar", "Desinstalar", "Salir"])
    if action == "Salir":
        return
    kind = places[choose("¿Dónde?", list(places))]
    if kind == "sd":
        cfg["sd"] = ask_path("Raíz de la SD (por ejemplo E:\\):", cfg.get("sd"))
        target = target_dir("sd", cfg["sd"])
    else:
        try:
            target = target_dir(kind, cfg.get(kind), ask=choose)
        except Error as e:
            print(f"No pude encontrarla sola: {e}")
            cfg[kind] = ask_path("Carpeta de usuario del emulador:", cfg.get(kind))
            target = target_dir(kind, cfg[kind])
    if action == "Desinstalar":
        uninstall(target)
    else:
        rom = ask_path("Arrastra aquí tu copia del juego (.3ds) y presiona Enter:", cfg.get("rom"))
        cfg["rom"] = rom
        install(rom, target, test=test)
        if kind == "sd":
            print("En la 3DS, activa «Enable game patching» en la configuración de Luma3DS "
                  "(mantén SELECT al encenderla).")
    save_config(cfg)


def main():
    a = argparse.ArgumentParser(description="Instala la traducción al español de SMT IV: Apocalypse.")
    a.add_argument("--rom", help="tu copia del juego (.3ds o .cxi descifrado)")
    a.add_argument("--target", choices=["azahar", "citra", "sd"])
    a.add_argument("--folder", help="carpeta de usuario del emulador, o raíz de la SD")
    a.add_argument("--uninstall", action="store_true")
    a.add_argument("--test", action="store_true", help="agrega los textos de tests/")
    args = a.parse_args()
    try:
        if not args.target:
            menu(args.test)
        elif args.uninstall:
            uninstall(target_dir(args.target, args.folder))
        else:
            if not args.rom:
                raise Error("falta --rom")
            install(args.rom, target_dir(args.target, args.folder), test=args.test)
    except (Error, InvalidImage, ValueError, OSError) as e:
        sys.exit(f"Error: {e}")
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nCancelado.")


if __name__ == "__main__":
    main()
