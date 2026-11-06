# Equipo de traducción

Cómo se reparten la traducción y la revisión. Es general: sirve para cualquier juego, y lo propio de cada uno va en sus documentos. Vive aquí mientras se decide si va en un repo propio ([PLAN.md](PLAN.md), pendiente 2).

## Principios

- **Cada regla vive en un solo lugar:** la guía de estilo, el glosario, las fichas de personajes o las reglas técnicas del juego. Los prompts de los roles traen solo el método, y el orquestador adjunta a cada lote las reglas que le tocan. En THL las reglas estaban copiadas en varios archivos y las copias terminaron contradiciéndose.
- **No se inventan reglas.** Solo valen los documentos y las decisiones registradas. Un hallazgo sin regla va a la cola de pendientes, no al texto.
- **Se cambia solo con motivo.** Lo que está bien se deja, y no se agregan palabras que el original no dice.
- **Quien revisa no edita.** El revisor y el corrector entregan hallazgos; solo el editor cambia el texto.
- **Informe honesto:** cada rol dice qué leyó completo y qué no.
- **Lo mecánico va en scripts**, que no se cansan, no inventan y no gastan cupo.

## Roles

| Rol | Quién | Ve | Entrega |
|---|---|---|---|
| Terminólogo | Script y LLM | Las tablas del juego y la referencia oficial | Candidatos al glosario (oficial, propuesto o por decidir), con género |
| Perfilador | LLM | Muestras de cada personaje | Fichas: género, trato con cada uno, muletillas, groserías |
| Traductor | LLM | El lote en inglés, con contexto, glosario y fichas | La traducción, sin saltos de línea |
| Delicadas | LLM | Juegos de palabras, muletillas, acertijos, referencias | Una solución provisional, a la cola de pendientes |
| Validador | Script | Todo | Avisos: códigos, ancho, bytes, glifos, glosario, léxico, signos, género |
| Revisor | LLM | Inglés y español | Hallazgos |
| Corrector | LLM | Solo español | Hallazgos |
| Editor | LLM | La traducción y los hallazgos | Cambios `{key, old, es}` |
| Dirección | Persona | Lo que haga falta | Decisiones, piloto, cola de pendientes, prueba en el juego |

El revisor y el corrector trabajan en paralelo sobre la misma traducción. El editor junta los dos informes en una sola pasada, con esta prioridad: técnico, glosario, fidelidad, estilo. Sus cambios usan el formato de `thl.py apply`, el mismo que usa translation-reviewer.

## Las siete pasadas, repartidas

| Pasada | Quién |
|---|---|
| 1. Fidelidad | Revisor |
| 2. Naturalidad | Corrector |
| 3. Localización | Revisor (qué hace el inglés) y corrector (si funciona en español) |
| 4. Gramática | Validador (y → e, o → u, signos, comillas, %) y corrector |
| 5. Género y concordancia | Validador (con el género de las fichas) y revisor |
| 6. Consistencia | Validador (memoria de traducción y glosario) |
| 7. Lectura final | Corrector |

## Un hallazgo

Una línea JSON por hallazgo, con estos campos:

- `key`: la línea.
- `pasada`: una de las siete.
- `gravedad`: crítica, mayor o menor.
- `regla`: el ID de la regla en la guía o el glosario, o `sin regla`.
- `fragmento`: lo que está mal.
- `arreglo`: el cambio mínimo.
- `motivo`: una frase.

## Forma de cada rol

```
Rol:      <nombre>
Recibe:   el lote (JSON) y las partes de la guía, el glosario, las fichas y las reglas técnicas que le tocan
Devuelve: traducción | hallazgos | cambios {key, old, es}, más el informe honesto
Método:   las pasadas que le tocan
Reglas:   solo las adjuntas; si falta una, «sin regla» y a la cola de pendientes
No hace:  reescribir, inventar contexto, usar git, salirse del lote
```

## Un lote, paso a paso

1. **Preparar** (script): proteger los códigos, juntar el contexto (la escena anterior en inglés y en español), filtrar el glosario y las fichas del lote, y aplicar la memoria de traducción.
2. **Traducir.**
3. **Validar.**
4. **Revisar y corregir**, en paralelo.
5. **Editar.**
6. **Partir renglones** (si el motor no lo hace) y validar otra vez.
7. **A la cola de pendientes:** las delicadas y los hallazgos sin regla.
