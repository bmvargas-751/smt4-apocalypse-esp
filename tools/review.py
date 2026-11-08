#!/usr/bin/env python3
"""Controles del revisor, el corrector y el editor (TEAM.md, «Controles»).

    python3 tools/review.py findings NOMBRE_DE_LOTE
    python3 tools/review.py edits NOMBRE_DE_LOTE

findings  lee build/work/batches/NOMBRE/findings-*.jsonl y comprueba cada
          hallazgo: campos completos, la línea es del lote y la regla citada
          existe en STYLE.md, TECH.md o GLOSSARY.md. Los válidos van a
          approved.jsonl. Los «sin regla» y los que citan una regla que no
          existe no llegan al texto: se agregan a PENDING.md.
edits     lee edits.jsonl del editor ({key, old, es, hallazgos}) y aplica solo
          los cambios que responden a un hallazgo aprobado de esa misma línea y
          cuyo «old» es el texto actual. Los demás se rechazan. El cambio se copia
          a las líneas idénticas que tenían el mismo texto.
"""
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
from batch import batch_dir, load_batch  # noqa: E402

FIELDS = ("id", "key", "pasada", "gravedad", "regla", "fragmento", "arreglo", "motivo")
PASSES = {"1", "2", "3", "4", "5", "6", "7", "fidelidad", "naturalidad", "localización", "gramática",
          "género", "consistencia", "lectura final"}
SEVERITY = {"crítica", "mayor", "menor"}
NO_RULE = "sin regla"


def read_jsonl(path):
    return [json.loads(x) for x in open(path, encoding="utf-8") if x.strip()] if path.exists() else []


def findings(name):
    batch = load_batch(name)
    keys = {it["key"] for it in batch["items"]}
    rules = corpus.rule_ids()
    d = batch_dir(name)
    approved, pending, rejected = [], [], []
    for path in sorted(d.glob("findings-*.jsonl")):
        role = path.stem.split("-", 1)[1]
        for f in read_jsonl(path):
            f["rol"] = role
            problem = None
            if any(not str(f.get(k, "")).strip() for k in FIELDS):
                problem = "faltan campos"
            elif f["key"] not in keys:
                problem = "la línea no es del lote"
            elif str(f["pasada"]).lower() not in PASSES:
                problem = f"pasada desconocida: {f['pasada']}"
            elif f["gravedad"] not in SEVERITY:
                problem = f"gravedad desconocida: {f['gravedad']}"
            if problem:
                rejected.append((f, problem))
            elif f["regla"] == NO_RULE:
                pending.append((f, "sin regla"))
            elif f["regla"] not in rules:
                pending.append((f, f"cita {f['regla']}, que no existe"))
            else:
                approved.append(f)
    with open(d / "approved.jsonl", "w", encoding="utf-8") as w:
        for f in approved:
            w.write(json.dumps(f, ensure_ascii=False) + "\n")
    if pending:
        add_pending(name, pending)
    for f, why in rejected:
        print(f"RECHAZADO {f.get('id', '?')} ({f.get('rol')}): {why}")
    print(f"{len(approved)} hallazgos aprobados, {len(pending)} a PENDING.md, {len(rejected)} rechazados")


def add_pending(name, items):
    path = corpus.REPO / "PENDING.md"
    lines = [f"\n### Lote {name} ({datetime.date.today().isoformat()})\n"]
    for f, why in items:
        lines.append(f"- [ ] `{f['key']}` ({f['rol']}, {why}): «{f['fragmento']}» → «{f['arreglo']}». {f['motivo']}")
    with open(path, "a", encoding="utf-8") as w:
        w.write("\n".join(lines) + "\n")


def edits(name):
    d = batch_dir(name)
    approved = {f["id"]: f for f in read_jsonl(d / "approved.jsonl")}
    done = corpus.translations()
    eng = corpus.english()
    changes, rejected = {}, []
    for e in read_jsonl(d / "edits.jsonl"):
        ids = e.get("hallazgos") or []
        backing = [approved.get(i) for i in ids]
        if not ids or any(f is None or f["key"] != e["key"] for f in backing):
            rejected.append((e, "no responde a un hallazgo aprobado de esta línea"))
        elif done.get(e["key"]) != e.get("old"):
            rejected.append((e, "«old» no es el texto actual"))
        elif not e.get("es", "").strip():
            rejected.append((e, "texto vacío"))
        else:
            changes[e["key"]] = e["es"]
    copies = 0
    for k, es in list(changes.items()):
        for other, v in eng.items():
            if other != k and other not in changes and v["en"] == eng[k]["en"] and done.get(other) == done.get(k):
                changes[other] = es
                copies += 1
    if changes:
        corpus.save(changes)
    for e, why in rejected:
        print(f"RECHAZADO {e.get('key')}: {why}")
    print(f"{len(changes) - copies} cambios aplicados ({copies} copias idénticas), {len(rejected)} rechazados")


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "findings":
        findings(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == "edits":
        edits(sys.argv[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
