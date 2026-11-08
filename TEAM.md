# Equipo de traducción

Cómo se reparten la traducción y la revisión. El método es general y sirve para cualquier juego; lo propio de IVA está en sus documentos: [STYLE.md](STYLE.md), [TECH.md](TECH.md), [GLOSSARY.md](GLOSSARY.md) y [characters/](characters).

## El encargo

Resumen fiel de las 11 secciones del encargo del usuario (de The Hundred Line). Es la fuente del método de todos los roles. Cada línea de un prompt cita su sección (§N) o una regla de los documentos.

1. Naturalidad sobre literalidad; fidelidad sin añadir ni quitar; calidad literaria (ritmo, sin repeticiones ni sinónimos artificiales).
2. Localización: modismos, juegos de palabras, humor, sarcasmo, referencias culturales, insultos: buscar el equivalente natural, no conservar lo literal por fidelidad a las palabras.
3. Diálogos y personalidad: formalidad, vocabulario, humor, trato, peculiaridades; no todos hablan igual; sonar espontáneo, no a texto traducido ni demasiado formal.
4. Género y concordancia (máxima prioridad): artículos, adjetivos, pronombres, participios; no deducir por el nombre; no masculino por defecto; si hay duda, marcar pendiente; revisión específica independiente al final.
5. Gramática, ortografía, puntuación, mayúsculas, signos, tiempos, preposiciones; convenciones actuales; evitar construcciones posibles pero poco naturales.
6. Consistencia terminológica: respetar el glosario, los nombres y las habilidades; no traducir lo que debe quedar; ante una inconsistencia, señalarla, no cambiarla arbitrariamente.
7. Contexto: quién habla, a quién, qué pasó; ironía; ante la ambigüedad, señalarla, nunca inventar contexto.
8. Técnico: preservar variables, placeholders, etiquetas, códigos y saltos necesarios; la corrección nunca rompe el archivo.
9. Metodología: siete pasadas (fidelidad, naturalidad, localización, gramática, género, consistencia, lectura final).
10. Cambiar solo con motivo (error, literal, artificial, fluidez, intención, localización, inconsistencia, género); si ya está bien, dejarlo; no reescribir todo el juego.
11. Formato de entrega: el original, la traducción, la versión corregida, el motivo (solo si hay cambio) y la categoría. No inventar errores para justificar cambios; con dudas, explicar la duda.

Objetivo: un videojuego que se sienta escrito originalmente en español.

## Principios

- **Cada regla vive en un solo lugar:** la guía de estilo, el glosario, las fichas o las reglas técnicas. Los prompts de los roles traen solo el método, y a cada lote se le adjuntan las reglas que le tocan. En THL las reglas estaban copiadas en varios archivos y las copias terminaron contradiciéndose.
- **No se inventan reglas.** Solo valen los documentos y las decisiones registradas ([DECISIONS.md](DECISIONS.md)). Un hallazgo sin regla va a [PENDING.md](PENDING.md), no al texto.
- **Se cambia solo con motivo.** Lo que está bien se deja, y no se agregan palabras que el original no dice.
- **Quien revisa no edita.** El revisor y el corrector entregan hallazgos; solo el editor cambia el texto.
- **Informe honesto:** cada rol dice qué leyó completo y qué no.
- **Lo mecánico va en scripts**, que no se cansan, no inventan y no gastan cupo. Más esfuerzo no reemplaza un chequeo.

## Roles

| Rol | Agente | Modelo | Esfuerzo | Ve | Entrega |
|---|---|---|---|---|---|
| Terminólogo | `terminologist` + `tools/smt5v.py` | Opus | high | Los candidatos de SMT V e IVA | Filas del glosario: *oficial* o *por decidir* |
| Perfilador | `profiler` | Opus | high | Muestras del inglés de cada personaje o personalidad | Fichas en [characters/](characters) |
| Traductor | `translator` | Sonnet | medium | El lote, con contexto, glosario y fichas | La traducción, en forma de lectura |
| Delicadas | `delicate` | Opus | xhigh | Juegos de palabras, acertijos, referencias | Una solución provisional y su entrada en PENDING.md |
| Validador | `tools/check.py` | — | — | Todo | Avisos con su regla |
| Revisor | `reviewer` | Sonnet | high | Inglés y español | Hallazgos |
| Corrector | `proofreader` | Sonnet | medium | Solo el español | Hallazgos |
| Editor | `editor` | Sonnet | low | La traducción y los hallazgos aprobados | Cambios `{key, old, es, hallazgos}` |
| Orquestador | skill `translate-batch` | sesión | low | El lote | Los pasos en orden, el informe y la cola |
| Dirección | El usuario | | | Lo que haga falta | Decisiones, PENDING.md, piloto, prueba en el juego |

- **El revisor y el corrector** trabajan en paralelo sobre la misma traducción. El editor junta los dos informes en una sola pasada, con esta prioridad: técnico, glosario, fidelidad, estilo.
- **Por qué estos modelos:** Opus va solo donde decide mucho con poco volumen. El traductor, el revisor y el corrector pasan por cada línea y se llevan casi todo el uso, por eso van en Sonnet. Haiku no escribe español. max, solo si lo pide el usuario.
- **Se ajustan con el piloto:** cada rol se prueba contra el set de oro. Si un esfuerzo menor rinde igual, se baja; si a Sonnet se le escapan errores que Opus atrapa, se sube. Cada cambio va a [DECISIONS.md](DECISIONS.md).
- **Uso:** nunca más de unos 3 agentes a la vez, y antes de un lote grande se estima el costo y se pide el visto bueno.

Los agentes están en [.claude/agents/](.claude/agents) y el orquestador, en [.claude/skills/translate-batch/](.claude/skills/translate-batch).

## Controles

1. **Los prompts no agregan nada propio.** Cada línea del prompt de un rol cita su fuente: una sección del encargo (§N) o una regla (E-12, T-3, G-1). Lo que no tiene fuente no entra, y el usuario aprueba cada prompt antes de usarlo.
2. **Cada hallazgo cita su regla.** `tools/review.py findings` comprueba que la regla exista en STYLE.md, TECH.md o GLOSSARY.md. Un hallazgo «sin regla», o con una regla que no existe, no llega al texto: va a PENDING.md.
3. **El editor no cambia por su cuenta.** `tools/review.py edits` solo aplica los cambios que responden a un hallazgo aprobado de esa misma línea. Los demás se rechazan.
4. **Lo mecánico lo revisa un script** (`tools/check.py`), que siempre aplica lo mismo.
5. **Set de oro:** líneas con su traducción buena y sus trampas, armadas en el piloto. Un cambio de prompt que empeora el set no entra.

## Las siete pasadas, repartidas

| Pasada | Quién |
|---|---|
| 1. Fidelidad | Revisor |
| 2. Naturalidad | Corrector |
| 3. Localización | Revisor (qué hace el inglés) y corrector (si funciona en español) |
| 4. Gramática | Validador (y → e, o → u, signos, comillas, %) y corrector |
| 5. Género y concordancia | Revisor, con el género de las fichas |
| 6. Consistencia | Validador (glosario y memoria de traducción) |
| 7. Lectura final | Corrector |

## Un lote, paso a paso

Todo el trabajo de un lote queda en `build/work/batches/NOMBRE/` (fuera del repo).

1. **Preparar** (script): `python3 -I tools/batch.py prepare --section Interfaz --size 250`. Elige las siguientes líneas sin traducir y salta las repetidas y las que están en japonés. Cada línea trae el inglés en forma de lectura, su máximo en bytes (tablas), el contexto y los términos del glosario.
2. **Traducir:** el traductor escribe `translation.jsonl` (`{key, es}`). Las líneas delicadas las resuelve el agente de delicadas.
3. **Guardar** (script): `python3 -I tools/batch.py save NOMBRE`. Pasa la traducción a `translation/` y la copia a las líneas idénticas.
4. **Validar** (script): `python3 -I tools/check.py NOMBRE`. El traductor corrige los avisos.
5. **Revisar y corregir**, en paralelo: `findings-reviewer.jsonl` y `findings-proofreader.jsonl`.
6. **Controlar los hallazgos** (script): `python3 -I tools/review.py findings NOMBRE`. Los aprobados van a `approved.jsonl`; los sin regla, a PENDING.md.
7. **Editar:** el editor escribe `edits.jsonl` con los cambios mínimos.
8. **Controlar y aplicar los cambios** (script): `python3 -I tools/review.py edits NOMBRE`, y después validar otra vez.
9. **Cerrar:** marcar el avance en el PLAN, `python3 -I tools/progress.py --readme` y un informe corto, sin spoilers.

## Un hallazgo

Una línea JSON por hallazgo:

```json
{"id": "R-12", "key": "saveLoadUI/saveloadUI.mbm#3", "pasada": "fidelidad", "gravedad": "mayor",
 "regla": "E-2", "fragmento": "lo que está mal", "arreglo": "el cambio mínimo", "motivo": "una frase"}
```

- `id`: R-n para el revisor, C-n para el corrector.
- `pasada`: una de las siete.
- `gravedad`: crítica, mayor o menor.
- `regla`: el número de la regla (E-, T- o G-), o `sin regla`.

## Un cambio del editor

```json
{"key": "saveLoadUI/saveloadUI.mbm#3", "old": "texto actual exacto", "es": "texto nuevo", "hallazgos": ["R-12"]}
```

## Forma de cada rol

```
Rol:      <nombre>
Modelo:   <modelo> · esfuerzo <nivel>
Recibe:   el lote y las reglas que le tocan
Devuelve: traducción | hallazgos | cambios, más el informe honesto
Método:   las pasadas que le tocan, cada línea con su fuente (§N o regla)
Reglas:   solo las de los documentos; si falta una, «sin regla» y a PENDING.md
No hace:  reescribir, inventar contexto, usar git, salirse del lote
```
