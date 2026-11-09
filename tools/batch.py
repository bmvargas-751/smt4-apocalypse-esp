#!/usr/bin/env python3
"""Lotes de traducción: preparar y guardar.

    python3 tools/batch.py prepare (--section NOMBRE | --prefix RUTA) [--size N] [--name NOMBRE]
    python3 tools/batch.py save NOMBRE [ARCHIVO.jsonl]
    python3 tools/batch.py fill --section NOMBRE [--dry-run]

prepare  elige las siguientes N líneas sin traducir (en el orden del juego) y
         escribe build/work/batches/NOMBRE/batch.json. Cada línea trae el
         inglés en forma de lectura, su máximo en bytes (tablas), el contexto
         (los mensajes anteriores del mismo archivo, con su traducción si la
         hay) y los términos del glosario que aparecen. Se saltan las líneas
         en japonés (TECH.md T-6), salvo con --japanese, y las repetidas: una línea se traduce una vez.
save     guarda en translation/ lo que escribió el traductor
         (build/work/batches/NOMBRE/translation.jsonl, {key, es}) y lo copia a
         las líneas idénticas que todavía no tienen traducción.
fill     completa, sin agentes, los textos de tabla que son exactamente un
         término del glosario (G-1, G-3), si caben en sus bytes (T-4) y en el ancho de su
         columna (T-3). Lo que
         no cabe queda para los lotes.
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
import tbb  # noqa: E402
from progress import EXCLUDED_KEYS, SECTIONS, section_of  # noqa: E402

WORK = corpus.REPO / "build" / "work" / "batches"
JAPANESE = re.compile("[぀-ヿ一-鿿]")
CONTEXT = 3


def batch_dir(name):
    return WORK / name


def load_batch(name):
    path = batch_dir(name) / "batch.json"
    if not path.exists():
        sys.exit(f"No existe el lote {name} ({path})")
    return json.loads(path.read_text(encoding="utf-8"))


def glossary_hits(text, terms):
    return [{"en": en, "es": es} for en, es in terms
            if re.search(rf"(?<![A-Za-z]){re.escape(en)}(?![A-Za-z])", text)]


def prepare(section=None, prefix=None, size=250, name=None, japanese=False):
    eng = corpus.english()
    done = corpus.translations()
    done_en = {eng[k]["en"] for k in done if k in eng}
    terms = corpus.glossary()
    keys = list(eng)
    position = {k: i for i, k in enumerate(keys)}
    chosen, seen = [], set()
    for k in keys:
        rel = corpus.rel_of(k)
        if section and section_of(rel) != section:
            continue
        if prefix and not rel.startswith(prefix):
            continue
        en = eng[k]["en"]
        if k in done or en in done_en or en in seen or k in EXCLUDED_KEYS or (JAPANESE.search(en) and not japanese):
            continue
        seen.add(en)
        chosen.append(k)
        if len(chosen) >= size:
            break
    if not chosen:
        sys.exit("No quedan líneas sin traducir con ese criterio.")
    items = []
    for k in chosen:
        item = {"key": k, "kind": corpus.kind_of(k), "en": corpus.reading_en(k)}
        if item["kind"] == "tbb":
            item["max"] = eng[k]["max"]
        else:
            rel = corpus.rel_of(k)
            prev = [p for p in keys[max(0, position[k] - CONTEXT):position[k]] if corpus.rel_of(p) == rel]
            item["context"] = [{"key": p, "en": corpus.reading_en(p), "es": done.get(p)} for p in prev]
        hits = glossary_hits(item["en"], terms)
        if hits:
            item["glossary"] = hits
        items.append(item)
    if not name:
        slug = re.sub(r"[^a-z0-9]+", "-", (section or prefix).lower()).strip("-")
        n = 1 + sum(1 for p in WORK.glob(f"{slug}-*")) if WORK.exists() else 1
        name = f"{slug}-{n:03d}"
    d = batch_dir(name)
    d.mkdir(parents=True, exist_ok=True)
    (d / "batch.json").write_text(json.dumps({
        "name": name, "section": section, "prefix": prefix,
        "created": datetime.datetime.now().isoformat(timespec="seconds"),
        "items": items,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Lote {name}: {len(items)} líneas en {d / 'batch.json'}")
    return name


def save(name, path=None):
    batch = load_batch(name)
    path = Path(path) if path else batch_dir(name) / "translation.jsonl"
    allowed = {it["key"]: it for it in batch["items"]}
    changes = {}
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip():
            continue
        d = json.loads(line)
        if d["key"] not in allowed:
            sys.exit(f"{path}:{n}: {d['key']} no es de este lote")
        if not d.get("es", "").strip():
            sys.exit(f"{path}:{n}: texto vacío")
        en = allowed[d["key"]]["en"]
        if en.endswith("{FFFF}") and not d["es"].endswith("{FFFF}"):
            sys.exit(f"{path}:{n}: el texto debe terminar en {{FFFF}}, como el inglés")
        changes[d["key"]] = d["es"]
    # memoria de traducción: las líneas idénticas sin traducir reciben la misma traducción,
    # y las que eran copia de la versión anterior de la línea se actualizan con ella
    eng = corpus.english()
    done = corpus.translations()
    by_en = {}
    for k, v in eng.items():
        by_en.setdefault((corpus.kind_of(k), v["en"]), []).append(k)
    copies = 0
    for k, es in list(changes.items()):
        for other in by_en[(corpus.kind_of(k), eng[k]["en"])]:
            stale = k in done and done.get(other) == done[k]
            if other != k and other not in changes and (other not in done or stale):
                changes[other] = es
                copies += 1
    corpus.save(changes)
    print(f"Guardadas {len(changes) - copies} líneas y {copies} copias idénticas en translation/")


def fill(section, dry_run=False):
    eng = corpus.english()
    done = corpus.translations()
    terms = {}
    for en, es in corpus.glossary():
        terms.setdefault(en, es)
    changes, too_long = {}, []
    meter = corpus.meter()
    for k, v in eng.items():
        if k in done or k in EXCLUDED_KEYS or corpus.kind_of(k) != "tbb":
            continue
        if section_of(corpus.rel_of(k)) != section:
            continue
        en = v["en"].strip()
        if en not in terms:
            continue
        es = terms[en]
        if en[:1].isupper():
            es = es[:1].upper() + es[1:]  # una etiqueta empieza con mayúscula, como el inglés
        if len(tbb.encode(es)) > v["max"]:
            too_long.append((k, en, es, f"{len(tbb.encode(es))} bytes, máximo {v['max']}"))
            continue
        _, tb, _, col = re.match(r"(.*)#(\d+)\.(\d+)\.(\d+)$", k).groups()
        cw = corpus.column_width(corpus.rel_of(k), int(tb), int(col))
        if meter.width(es) > cw:  # T-3: más ancho que el inglés más largo de su columna
            too_long.append((k, en, es, f"{meter.width(es)} px, el inglés llega a {cw}"))
            continue
        changes[k] = es
    if changes and not dry_run:
        corpus.save(changes)
    print(f"{len(changes)} textos completados con el glosario{' (prueba, sin guardar)' if dry_run else ''}; "
          f"{len(too_long)} no caben (quedan para los lotes)")
    for k, en, es, why in too_long:
        print(f"  {k}: {en} → {es} ({why})")


def main():
    a = argparse.ArgumentParser()
    sub = a.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--section", choices=[s[1] for s in SECTIONS])
    p.add_argument("--prefix")
    p.add_argument("--size", type=int, default=250)
    p.add_argument("--name")
    p.add_argument("--japanese", action="store_true", help="incluir las líneas con japonés (se saltan por defecto)")
    f = sub.add_parser("fill")
    f.add_argument("--section", required=True, choices=[s[1] for s in SECTIONS])
    f.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("save")
    s.add_argument("name")
    s.add_argument("path", nargs="?")
    args = a.parse_args()
    if args.cmd == "prepare":
        if not (args.section or args.prefix):
            sys.exit("Indica --section o --prefix")
        prepare(args.section, args.prefix, args.size, args.name, args.japanese)
    elif args.cmd == "fill":
        fill(args.section, args.dry_run)
    else:
        save(args.name, args.path)


if __name__ == "__main__":
    main()
