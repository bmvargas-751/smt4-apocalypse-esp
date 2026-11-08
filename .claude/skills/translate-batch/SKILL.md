---
name: translate-batch
description: Traduce un lote de IVA con el equipo completo (traductor, delicadas, revisor, corrector, editor) y los controles de TEAM.md. Se usa cuando el usuario pide traducir una sección o un grupo de archivos, o seguir con el siguiente lote.
effort: low
---

# Traducir un lote

El método está en [TEAM.md](../../../TEAM.md) («Un lote, paso a paso»). Esta skill solo lo ordena: prepara el lote, llama a cada agente y corre los controles. Las reglas no se repiten aquí; viven en STYLE.md, TECH.md y GLOSSARY.md.

## Antes de empezar

1. Confirma con el usuario la sección (o los archivos) y el tamaño del lote, salvo que ya lo haya dicho. El tamaño por defecto es 250 líneas.
2. **Estima el costo y pide el visto bueno** si el lote es nuevo o más grande que el anterior. Referencia de THL: unos 25.000 tokens leídos y 18.000 escritos cada 250 líneas, por agente. En un lote pasan el traductor, el revisor, el corrector y el editor, más delicadas si hay. [TEAM: uso]
3. Nunca más de unos 3 agentes a la vez. [TEAM: uso]
4. Si la extracción local no está (`../smt4a-local/en.jsonl`, `tbb.jsonl`), créala con `tools/mbm.py export` y `tools/tbb.py export`.

## Pasos

1. `python3 -I tools/batch.py prepare --section SECCIÓN --size N` (o `--prefix RUTA`). Anota el nombre del lote.
2. Agente `translator` con el nombre del lote. El agente guarda y valida solo (`batch.py save`, `check.py`).
3. Si quedó `delicate.jsonl` con claves, agente `delicate`.
4. Agentes `reviewer` y `proofreader`, en paralelo.
5. `python3 -I tools/review.py findings NOMBRE`. Lo sin regla pasa solo a PENDING.md.
6. Agente `editor`, si hay hallazgos aprobados.
7. `python3 -I tools/review.py edits NOMBRE` y `python3 -I tools/check.py NOMBRE`. Si queda algún aviso, vuelve al editor con ese aviso (es un hallazgo con regla).
8. Cierre:
   - Marca el avance en PLAN.md si terminó una sección.
   - Ejecuta `python3 -I tools/progress.py --readme`.
   - Da al usuario un informe corto y sin spoilers: líneas traducidas, copias idénticas, avisos que quedaron, hallazgos por rol y lo nuevo en PENDING.md.
9. Commit y push solo si el usuario lo pidió, sin firma de Claude. Instalar en el juego, solo si el usuario lo pide.

## Si algo falla

- Un agente que no entrega su archivo, o lo entrega incompleto: se le vuelve a pedir con lo que falta. No se completa a mano.
- Un control que rechaza cambios: se informa al usuario. No se fuerza.
