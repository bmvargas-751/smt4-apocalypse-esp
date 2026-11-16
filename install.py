#!/usr/bin/env python3
"""Instalador de la traducción al español de Shin Megami Tensei IV: Apocalypse.

Con doble clic en el .exe o en install.bat (Windows), o desde una terminal:

    python3 install.py                                   menú: crea la copia traducida
    python3 install.py --rom JUEGO.3ds [--output SALIDA.3ds] [--test]
    python3 install.py --rom JUEGO.3ds --target azahar|citra|sd [--folder RUTA] [--test]
    python3 install.py --uninstall --target azahar|citra|sd [--folder RUTA]

Sin --target, crea una copia traducida de tu juego (versión europea, .3ds/.cci o
.cxi descifrado), junto a la original: «NOMBRE (Español).3ds». La original no se toca.

Con --target, en lugar de eso, instala la traducción como mod en:
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
FROZEN = getattr(sys, "frozen", False)  # el .exe de PyInstaller
sys.path.insert(0, str(HERE / "tools"))
from ctr import InvalidImage  # noqa: E402
from patch import GAME_ID, build, build_code, build_code_bin  # noqa: E402
from rom import build_rom  # noqa: E402

TITLE_ID = f"{GAME_ID:016X}"
MANIFEST = "smt4a-esp.json"
CONFIG = (Path(sys.executable).parent if FROZEN else HERE) / "install.json"
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
    installed = json.loads(manifest.read_text(encoding="utf-8"))
    for rel in installed["files"]:
        (romfs / rel).unlink(missing_ok=True)
    if installed.get("code"):
        code = target / installed["code"]
        code.unlink(missing_ok=True)
        if code.parent != target and code.parent.is_dir() and not any(code.parent.iterdir()):
            code.parent.rmdir()
    for d in sorted((p for p in romfs.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    if romfs.is_dir() and not any(romfs.iterdir()):
        romfs.rmdir()
    manifest.unlink()
    if target.is_dir() and not any(target.iterdir()):
        target.rmdir()
    log(f"Traducción desinstalada de {target}")


def default_output(rom):
    rom = Path(rom)
    return rom.with_name(f"{rom.stem} (Español){rom.suffix}")


def make_rom(rom, output=None, test=False, log=print):
    """Crea la copia traducida del juego; devuelve su ruta."""
    output = Path(output) if output else default_output(rom)
    if output.resolve() == Path(rom).resolve():
        raise Error("la copia traducida no puede reemplazar a la original")
    files = build(rom, test=test, log=log)
    pair = build_code_bin(rom, test=test, log=log)
    log(f"Creando {output.name} (tarda unos minutos)...")
    tmp = output.with_name(output.name + ".tmp")
    try:
        build_rom(rom, tmp, files, pair[1] if pair else None, log=log)
        tmp.replace(output)
    finally:
        tmp.unlink(missing_ok=True)
    log(f"Listo: {output}")
    return output


def code_path(target):
    """Dónde va el parche del ejecutable: Luma3DS lo lee junto a romfs/; Azahar y Citra, en exefs/."""
    return Path("code.ips") if target.parent.name == "titles" else Path("exefs") / "code.ips"


def install(rom, target, test=False, log=print):
    romfs = target / "romfs"
    if not (target / MANIFEST).exists() and romfs.is_dir() and any(romfs.rglob("*")):
        raise Error(f"ya hay otro mod en {romfs}; quítalo antes de instalar la traducción")
    code = code_path(target)
    if not (target / MANIFEST).exists() and (target / code).exists():
        raise Error(f"ya hay otro parche del ejecutable en {target / code}; quítalo antes de instalar la traducción")
    files = build(rom, test=test, log=log)
    ips = build_code(rom, test=test, log=log)
    if (target / MANIFEST).exists():
        uninstall(target, log=lambda _: None)
    for rel, data in files.items():
        (romfs / rel).parent.mkdir(parents=True, exist_ok=True)
        (romfs / rel).write_bytes(data)
    if ips:
        (target / code).parent.mkdir(parents=True, exist_ok=True)
        (target / code).write_bytes(ips)
    (target / MANIFEST).write_text(json.dumps({
        "game": TITLE_ID,
        "installed": datetime.datetime.now().isoformat(timespec="seconds"),
        "test": test,
        "files": sorted(files),
        "code": code.as_posix() if ips else None,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"Listo: {len(files)} archivos en {romfs}" + (f", y el parche del ejecutable en {target / code}" if ips else ""))


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
    print("Crea una copia traducida de tu juego, junto a la original (que no se toca).\n")
    cfg = load_config()
    rom = ask_path("Arrastra aquí tu copia del juego (.3ds) y presiona Enter:", cfg.get("rom"))
    if not rom:
        raise Error("falta la copia del juego")
    cfg["rom"] = rom
    save_config(cfg)
    make_rom(rom, test=test)


def pause():
    """Con doble clic en el .exe, la ventana se cerraría sin dejar leer el resultado."""
    if FROZEN:
        try:
            input("\nPresiona Enter para salir.")
        except (KeyboardInterrupt, EOFError):
            pass


def main():
    a = argparse.ArgumentParser(description="Instala la traducción al español de SMT IV: Apocalypse.")
    a.add_argument("--rom", help="tu copia del juego (.3ds o .cxi descifrado)")
    a.add_argument("--output", help="dónde crear la copia traducida (sin --target)")
    a.add_argument("--target", choices=["azahar", "citra", "sd"])
    a.add_argument("--folder", help="carpeta de usuario del emulador, o raíz de la SD")
    a.add_argument("--uninstall", action="store_true")
    a.add_argument("--test", action="store_true", help="agrega los textos de tests/")
    args = a.parse_args()
    try:
        if not args.target and not args.rom:
            menu(args.test)
            pause()
        elif not args.target:
            make_rom(args.rom, args.output, test=args.test)
        elif args.uninstall:
            uninstall(target_dir(args.target, args.folder))
        else:
            if not args.rom:
                raise Error("falta --rom")
            install(args.rom, target_dir(args.target, args.folder), test=args.test)
    except (Error, InvalidImage, ValueError, OSError) as e:
        print(f"Error: {e}")
        pause()
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nCancelado.")


if __name__ == "__main__":
    main()
