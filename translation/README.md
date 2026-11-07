# Traducción

Aquí va nuestra traducción, y nada más: ningún texto del juego.

## Cómo se divide

La traducción es la fase 6 del [plan](../PLAN.md) y se hace por secciones, en este orden: datos e interfaz primero, después la historia en orden, las secundarias y las negociaciones por personalidad. Cada archivo de mensajes del juego pertenece a una sola sección, según la carpeta donde está (la lista de carpetas está en `SECTIONS`, en [tools/progress.py](../tools/progress.py)).

<!-- progress: lo actualiza `python3 -I tools/progress.py --readme` en cada commit que toca translation/ -->
| Fase | Sección | Contenido | Traducidos | Total | % |
|---|---|---|---:|---:|---:|
| 6.1 | Interfaz | Menús, sistema, combate, fusión, tiendas, guardado, StreetPass y tutoriales | 0 | 707 | 0,0 % |
| 6.2 | Tablas | Nombres de objetos, demonios, misiones y lugares, y textos cortos de menús (.tbb) | — | por medir | — |
| 6.3 | Datos | Descripciones de objetos y habilidades, perfiles de demonios y base de datos de cazadores | 0 | 3.001 | 0,0 % |
| 6.4 | Historia | Eventos, combates de la historia, mapas y tu cuarto | 0 | 2.773 | 0,0 % |
| 6.5 | Secundarias | Misiones, centro de misiones, personajes de la ciudad y charlas con el compañero | 0 | 1.578 | 0,0 % |
| 6.6 | Negociaciones | Conversaciones con demonios, por personalidad | 0 | 11.518 | 0,0 % |
| 6.7 | Demonios en combate | Frases de demonios y compañeros en combate y en StreetPass | 0 | 4.380 | 0,0 % |
| 6.8 | Contenido descargable | Misiones descargables | 0 | 225 | 0,0 % |
| | **Total** | | **0** | **24.182** | **0,0 %** |
<!-- /progress -->

- **Se cuentan mensajes**, no palabras: un mensaje puede ser un «Sí» o una escena entera. Muchos se repiten (de los 24.182, 11.490 son distintos), y una línea repetida se traduce una sola vez.
- **Tablas:** los nombres y los textos cortos de las tablas se cuentan cuando esté la herramienta para leerlas.
- **Japonés:** quedan 2844 mensajes en japonés, unos 2000 en *Demonios en combate*. Se cuentan igual hasta saber si el juego los muestra.
- **Fuera de la cuenta:** los 7 mensajes de prueba de los desarrolladores (`test/`).

## Formato

Un JSONL por archivo de mensajes del juego, con su misma ruta: la traducción de `saveLoadUI/saveloadUI.mbm` va en `translation/saveLoadUI/saveloadUI.jsonl`. Una línea por mensaje:

```json
{"key": "saveLoadUI/saveloadUI.mbm#1", "es": "Sí{F801}No{F801}{FFFF}"}
```

- `key`: el archivo y el número del mensaje, como los escribe `tools/mbm.py export`.
- `es`: el texto en español, con los mismos códigos `{XXXX}` que el original. `{F801}` es salto de línea, `{F802}` es cambio de página y `{FFFF}` es el fin del mensaje.

El instalador aplica todo lo que haya en esta carpeta. Los textos de [tests/](../tests) solo se aplican con `--test`.
