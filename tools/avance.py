#!/usr/bin/env python3
"""Avance de la traducción por sección.

    python3 tools/avance.py [--en EN.jsonl] [--readme]

Cuenta los mensajes del juego (EN.jsonl, de `mbm.py export`; por defecto
../smt4a-local/en.jsonl) y los traducidos en traduccion/. Con --readme
reescribe las tablas entre <!-- avance --> y <!-- /avance --> en README.md y
en traduccion/README.md, y la etapa actual (lo primero pendiente de PLAN.md).
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Fase 6 del plan, en orden. Cada archivo de mensajes va a la sección del
# prefijo más largo que le corresponda.
SECCIONES = [
    ("6.1", "Interfaz", "Menús, sistema, combate, fusión, tiendas, guardado, StreetPass y tutoriales", [
        "title/", "saveLoadER/", "saveLoadUI/", "clear_save/", "camp/", "unite/", "shop/", "npc_shop/",
        "terminal/", "cec/", "bible/", "fountain/", "name/", "battle/BattleUI.mbm", "battle/Common/",
        "battle/ResultMsg.mbm", "battle/SkillInfoMess.mbm", "event/HowTo/", "addon/aoc_", "map/all/"]),
    ("6.2", "Tablas", "Nombres de objetos, demonios, misiones y lugares, y textos cortos de menús (.tbb)", None),
    ("6.3", "Datos", "Descripciones de objetos y habilidades, perfiles de demonios y base de datos de cazadores", [
        "item/", "battle/SkillHelpMess.mbm", "status/", "event/HunterDataBase/"]),
    ("6.4", "Historia", "Eventos, combates de la historia, mapas y tu cuarto", [
        "event/e", "battle/event/", "battle/gameover/", "map/", "mikado/", "ones_room/"]),
    ("6.5", "Secundarias", "Misiones, centro de misiones, personajes de la ciudad y charlas con el compañero", [
        "event/quest/", "quest_center/", "npc_room/", "event/PartnerTopic/"]),
    ("6.6", "Negociaciones", "Conversaciones con demonios, por personalidad", ["battle/talk/"]),
    ("6.7", "Demonios en combate", "Frases de demonios y compañeros en combate y en StreetPass", [
        "battle/DevilMsg/", "camp/CecDevilMsg/", "battle/PartnerAttack.mbm", "battle/Legion/"]),
    ("6.8", "Contenido descargable", "Misiones descargables", ["addon/testdata/"]),
]
EXCLUIDOS = ["test/"]          # mensajes de prueba de los desarrolladores


def seccion_de(archivo):
    if any(archivo.startswith(p) for p in EXCLUIDOS):
        return None
    mejor = (0, "Sin asignar")
    for _, nombre, _, prefijos in SECCIONES:
        for p in prefijos or []:
            if archivo.startswith(p) and len(p) > mejor[0]:
                mejor = (len(p), nombre)
    return mejor[1]


def contar(en):
    total, hechos = {}, {}
    claves = {}
    for linea in open(en, encoding="utf-8"):
        k = json.loads(linea)["key"]
        s = seccion_de(k.split("#")[0])
        if s:
            claves[k] = s
            total[s] = total.get(s, 0) + 1
    for jsonl in sorted((REPO / "traduccion").rglob("*.jsonl")):
        for linea in open(jsonl, encoding="utf-8"):
            if linea.strip():
                d = json.loads(linea)
                if d.get("es") and d["key"] in claves:
                    s = claves[d["key"]]
                    hechos[s] = hechos.get(s, 0) + 1
    return total, hechos


def num(n):
    return f"{n:,}".replace(",", ".")


def pct(a, b):
    return f"{100 * a / b:.1f} %".replace(".", ",") if b else "—"


def tabla(total, hechos, con_contenido):
    cab = "| Fase | Sección |" + (" Contenido |" if con_contenido else "") + " Traducidos | Total | % |"
    sep = "|---|---|" + ("---|" if con_contenido else "") + "---:|---:|---:|"
    filas = [cab, sep]
    for fase, nombre, contenido, prefijos in SECCIONES:
        extra = f" {contenido} |" if con_contenido else ""
        if prefijos is None:
            filas.append(f"| {fase} | {nombre} |{extra} — | por medir | — |")
            continue
        t, h = total.get(nombre, 0), hechos.get(nombre, 0)
        filas.append(f"| {fase} | {nombre} |{extra} {num(h)} | {num(t)} | {pct(h, t)} |")
    if total.get("Sin asignar"):
        filas.append(f"| | Sin asignar |{' |' if con_contenido else ''} {num(hechos.get('Sin asignar', 0))} "
                     f"| {num(total['Sin asignar'])} | |")
    t, h = sum(total.values()), sum(hechos.values())
    filas.append(f"| | **Total** |{' |' if con_contenido else ''} **{num(h)}** | **{num(t)}** | **{pct(h, t)}** |")
    return "\n".join(filas)


def etapa_actual():
    fase = None
    for linea in (REPO / "PLAN.md").read_text(encoding="utf-8").splitlines():
        if linea.startswith("### "):
            fase = linea[4:].strip()
        elif linea.startswith("- [ ] ") and fase:
            item = re.sub(r"\s+", " ", linea[6:]).strip()
            return f"{fase}: {item}"
    return "todas las fases del plan están terminadas"


def reemplazar(path, bloque):
    s = path.read_text(encoding="utf-8")
    nuevo, n = re.subn(r"(<!-- avance[^>]*-->\n).*?(<!-- /avance -->)",
                       lambda m: m.group(1) + bloque + "\n" + m.group(2), s, flags=re.S)
    if not n:
        sys.exit(f"{path}: faltan las marcas <!-- avance --> y <!-- /avance -->")
    path.write_text(nuevo, encoding="utf-8")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--en", default=str(REPO.parent / "smt4a-local" / "en.jsonl"))
    a.add_argument("--readme", action="store_true")
    args = a.parse_args()
    if not Path(args.en).exists():
        sys.exit(f"No encuentro {args.en}; créalo con: python3 tools/mbm.py export ROMFS {args.en}")
    total, hechos = contar(args.en)
    if not args.readme:
        print(tabla(total, hechos, False))
        return
    reemplazar(REPO / "README.md", f"**Etapa actual:** {etapa_actual()}\n\n{tabla(total, hechos, False)}")
    reemplazar(REPO / "traduccion" / "README.md", tabla(total, hechos, True))
    print("README.md y traduccion/README.md actualizados")


if __name__ == "__main__":
    main()
