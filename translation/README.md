# Traducción

Aquí va nuestra traducción, y nada más: ningún texto del juego.

## Cómo se divide

La traducción es la fase 6 del [plan](../PLAN.md) y se hace por secciones, en este orden: datos e interfaz primero, después la historia en orden, las secundarias y las negociaciones por personalidad. Cada archivo de mensajes del juego pertenece a una sola sección, según la carpeta donde está (la lista de carpetas está en `SECTIONS`, en [tools/progress.py](../tools/progress.py)).

<!-- progress: lo actualiza `python3 -I tools/progress.py --readme` en cada commit que toca translation/ -->
| Fase | Sección | Contenido | Traducidos | Total | % |
|---|---|---|---:|---:|---:|
| 6.1 | Interfaz | Menús, sistema, combate, fusión, tiendas, guardado, StreetPass y tutoriales | 690 | 690 | 100,0 % |
| 6.2 | Tablas | Nombres de objetos, demonios, misiones y lugares, y textos cortos de menús (.tbb) | 6.757 | 6.757 | 100,0 % |
| 6.3 | Datos | Descripciones de objetos y habilidades, perfiles de demonios y base de datos de cazadores | 2.599 | 2.599 | 100,0 % |
| 6.4 | Historia | Eventos, combates de la historia, mapas y tu cuarto | 1.722 | 2.734 | 63,0 % |
| 6.5 | Secundarias | Misiones, centro de misiones, personajes de la ciudad y charlas con el compañero | 5 | 1.575 | 0,3 % |
| 6.6 | Negociaciones | Conversaciones con demonios, por personalidad | 0 | 11.516 | 0,0 % |
| 6.7 | Demonios en combate | Frases de demonios y compañeros en combate y en StreetPass | 0 | 4.365 | 0,0 % |
| 6.8 | Contenido descargable | Misiones descargables | 59 | 542 | 10,9 % |
| | **Total** | | **11.832** | **30.778** | **38,4 %** |
<!-- /progress -->

- **Se cuentan textos**, no palabras: un mensaje puede ser un «Sí» o una escena entera, y un texto de tabla suele ser un nombre. Muchos se repiten (de los 24.182 mensajes, 11.490 son distintos; de los 6.757 textos de tablas, 3.306), y una línea repetida se traduce una sola vez.
- **Tablas:** solo cuentan los textos en inglés que ve el jugador. Quedan fuera los nombres internos (4.266: archivos, etiquetas) y 4.587 textos en japonés: marcadores de los desarrolladores («予備枠», «未使用») y la versión japonesa de descripciones que en inglés están en los mensajes.
- **Japonés:** quedan 2825 mensajes en japonés, unos 2000 en *Demonios en combate*. Se cuentan igual hasta saber si el juego los muestra (TECH T-6). De la Interfaz se tradujeron 2 por si acaso.
- **Fuera de la cuenta:** los 7 mensajes de prueba de los desarrolladores (`test/`), 17 de relleno o prueba en japonés de la Interfaz («ダミー» y el silabario), 11 de relleno de Datos («Dummy Text», «ダミー本文»; `EXCLUDED_KEYS` en tools/progress.py) y 414 mensajes sin texto, solo códigos (391 de ellos en Datos).

## Formato

Un JSONL por archivo del juego, con su misma ruta y `.jsonl` al final: la traducción de `saveLoadUI/saveloadUI.mbm` va en `translation/saveLoadUI/saveloadUI.mbm.jsonl`, y la de `title/TitleTable.tbb`, en `translation/title/TitleTable.tbb.jsonl`. Una línea por texto. Estos archivos los escriben `tools/batch.py` y `tools/review.py`, no se editan a mano.

**Mensajes** (`.mbm`):

```json
{"key": "saveLoadUI/saveloadUI.mbm#1", "es": "Sí{F801}No{F801}{FFFF}"}
```

- `key`: el archivo y el número del mensaje, como los escribe `tools/mbm.py export`.
- `es`: el texto en español, en **forma de lectura** ([TECH.md](../TECH.md) T-2), con los mismos códigos `{XXXX}` que el original. `{F801}` es un salto fijo, `{F802}` es cambio de página y `{FFFF}` es el fin del mensaje. Los saltos que solo sirven para que el párrafo quepa los pone el instalador.

**Tablas** (`.tbb`):

```json
{"key": "title/TitleTable.tbb#0.0.0", "es": "Nueva partida"}
```

- `key`: el archivo y `tabla.registro.posición`, como los escribe `tools/tbb.py export`.
- `es`: el texto, sin códigos; el salto de línea es `\n`. Cada campo tiene un largo fijo: `tools/tbb.py export` da su máximo en bytes (`max`). Las letras españolas ocupan 2 bytes y el resto, 1. Si un texto no cabe, el instalador avisa y no lo instala.

Una línea repetida se traduce una sola vez: al guardar, la traducción se copia a las líneas idénticas que no tienen traducción.

El instalador aplica todo lo que haya en esta carpeta. Los textos de [tests/](../tests) solo se aplican con `--test`.
