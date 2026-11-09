#!/usr/bin/env python3
"""Avance de la traducción por sección.

    python3 tools/progress.py [--en EN.jsonl] [--tbb TBB.jsonl] [--readme]

Cuenta los textos del juego (los mensajes de `mbm.py export` y los de las
tablas de `tbb.py export`; por defecto ../smt4a-local/en.jsonl y
../smt4a-local/tbb.jsonl) y los traducidos en translation/. Con --readme
reescribe las tablas entre <!-- progress --> y <!-- /progress --> en README.md
y en translation/README.md, y la etapa actual (lo primero pendiente de PLAN.md).
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Fase 6 del plan, en orden. Cada archivo de mensajes va a la sección del
# prefijo más largo que le corresponda.
SECTIONS = [
    ("6.1", "Interfaz", "Menús, sistema, combate, fusión, tiendas, guardado, StreetPass y tutoriales", [
        "title/", "saveLoadER/", "saveLoadUI/", "clear_save/", "camp/", "unite/", "shop/", "npc_shop/",
        "terminal/", "cec/", "bible/", "fountain/", "name/", "battle/BattleUI.mbm", "battle/Common/",
        "battle/ResultMsg.mbm", "battle/SkillInfoMess.mbm", "event/HowTo/", "addon/aoc_", "map/all/"]),
    ("6.2", "Tablas", "Nombres de objetos, demonios, misiones y lugares, y textos cortos de menús (.tbb)", []),
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
TABLES, DLC = "Tablas", "Contenido descargable"
EXCLUDED = ["test/"]           # mensajes de prueba de los desarrolladores
# Mensajes sueltos de relleno o de prueba, en japonés, que no son texto del juego
# (DECISIONS 2026-11-08): «ダミー» de la lista de StreetPass y el silabario de prueba.
EXCLUDED_KEYS = {f"camp/CecEdit_one_msg.mbm#{n}" for n in range(100, 116)} | {"camp/partypanel.mbm#10"}
UNASSIGNED = "Sin asignar"


def section_of(path):
    if any(path.startswith(p) for p in EXCLUDED):
        return None
    if path.endswith(".tbb"):
        return DLC if path.startswith("addon/testdata/") else TABLES
    best = (0, UNASSIGNED)
    for _, name, _, prefixes in SECTIONS:
        for p in prefixes or []:
            if path.startswith(p) and len(p) > best[0]:
                best = (len(p), name)
    return best[1]


def count(sources):
    total, done, keys = {}, {}, {}
    for src in sources:
        for line in open(src, encoding="utf-8"):
            k = json.loads(line)["key"]
            s = None if k in EXCLUDED_KEYS else section_of(k.split("#")[0])
            if s:
                keys[k] = s
                total[s] = total.get(s, 0) + 1
    for jsonl in sorted((REPO / "translation").rglob("*.jsonl")):
        for line in open(jsonl, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                if d.get("es") and d["key"] in keys:
                    s = keys[d["key"]]
                    done[s] = done.get(s, 0) + 1
    return total, done


def num(n):
    return f"{n:,}".replace(",", ".")


def pct(a, b):
    return f"{100 * a / b:.1f} %".replace(".", ",") if b else "—"


def table(total, done, with_content):
    blank = " |" if with_content else ""
    rows = ["| Fase | Sección |" + (" Contenido |" if with_content else "") + " Traducidos | Total | % |",
            "|---|---|" + ("---|" if with_content else "") + "---:|---:|---:|"]
    for phase, name, content, prefixes in SECTIONS:
        extra = f" {content} |" if with_content else ""
        t, d = total.get(name, 0), done.get(name, 0)
        rows.append(f"| {phase} | {name} |{extra} {num(d)} | {num(t)} | {pct(d, t)} |")
    if total.get(UNASSIGNED):
        rows.append(f"| | {UNASSIGNED} |{blank} {num(done.get(UNASSIGNED, 0))} | {num(total[UNASSIGNED])} | |")
    t, d = sum(total.values()), sum(done.values())
    rows.append(f"| | **Total** |{blank} **{num(d)}** | **{num(t)}** | **{pct(d, t)}** |")
    return "\n".join(rows)


def current_stage():
    phase = None
    for line in (REPO / "PLAN.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            phase = line[4:].strip()
        elif line.startswith("- [ ] ") and phase:
            return f"{phase}: {re.sub(r'\s+', ' ', line[6:]).strip()}"
    return "todas las fases del plan están terminadas"


def replace_block(path, block):
    s = path.read_text(encoding="utf-8")
    new, n = re.subn(r"(<!-- progress[^>]*-->\n).*?(<!-- /progress -->)",
                     lambda m: m.group(1) + block + "\n" + m.group(2), s, flags=re.S)
    if not n:
        sys.exit(f"{path}: faltan las marcas <!-- progress --> y <!-- /progress -->")
    path.write_text(new, encoding="utf-8")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--en", default=str(REPO.parent / "smt4a-local" / "en.jsonl"))
    a.add_argument("--tbb", default=str(REPO.parent / "smt4a-local" / "tbb.jsonl"))
    a.add_argument("--readme", action="store_true")
    args = a.parse_args()
    for path, tool in ((args.en, "mbm"), (args.tbb, "tbb")):
        if not Path(path).exists():
            sys.exit(f"No encuentro {path}; créalo con: python3 tools/{tool}.py export ROMFS {path}")
    total, done = count([args.en, args.tbb])
    if not args.readme:
        print(table(total, done, False))
        return
    replace_block(REPO / "README.md", f"**Etapa actual:** {current_stage()}\n\n{table(total, done, False)}")
    replace_block(REPO / "translation" / "README.md", table(total, done, True))
    print("README.md y translation/README.md actualizados")


if __name__ == "__main__":
    main()
