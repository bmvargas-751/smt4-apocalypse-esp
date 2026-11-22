# Reglas del repo

Traducción de *Shin Megami Tensei IV: Apocalypse* al español con el kit de traducción de juegos (`~/.claude/loc-kit`: METHOD.md y REPO.md).

- Empezar o retomar el proyecto: skill `loc-start`. Traducir un lote: skill `loc-batch`.
- `main` está protegido: todo cambio va en una rama y un pull request, sin firma de Claude. El usuario fusiona; Claude nunca fusiona.
- Al cerrar un lote o una fase: casillas del PLAN, `loc.py progress --readme`, commit, push y pull request, sin pedir permiso.
- Sin spoilers en los documentos, los commits, los pull requests y el chat: se nombran zonas o archivos, nunca hechos de la historia.
- En el repo nunca van archivos del juego: lo extraído vive fuera, en una carpeta hermana (`../NOMBRE-local/`).
- No se inventan reglas: solo valen STYLE.md, TECH.md, GLOSSARY.md, las fichas de `characters/` y DECISIONS.md. Lo que no cubren va a PENDING.md.
- Antes de lanzar agentes, estimar el costo y pedir el visto bueno; nunca más de unos 3 a la vez.

## Lo propio de este repo

- IVA es anterior al kit: el kit salió de aquí. Lo adoptó la skill `loc-adopt` (2026-11-22).
  - El original se exporta con `python3 tools/kit_adapter.py export`, a `../smt4a-local/kit-source.jsonl`, en forma de lectura (TECH T-2).
  - `tools/hooks.py` usa las secciones y exclusiones de `tools/progress.py`, y la caja y la fuente de `tools/check.py`.
- El README tiene la forma común del kit (REPO.md). «Instalar» y «Avance» los escribe `loc.py progress --readme`: los pasos de instalación se cambian en `project.json`, no en el README. `tools/progress.py --readme` solo actualiza `translation/README.md`.
- `.claude/agents/` y la skill `translate-batch` son el equipo de IVA de antes del kit: no se usan. Las correcciones van con la skill `loc-batch` del kit, que pide armar antes el set de oro (skill `loc-start`, fase 4).
- El instalador es `install.py` (y `install.bat`); el `.exe` de Windows se arma con `tools\build_exe.bat`.
