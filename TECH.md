# Reglas técnicas

Lo que el juego necesita para que el texto no se rompa. Cada regla tiene un número para citarla, y la mayoría la controla `tools/check.py` (el chequeo va entre paréntesis). Salen de cómo está hecho el juego, de [tools/](tools) y de la sección 8 del encargo: preservar los códigos, porque una traducción nunca puede romper el archivo.

## Mensajes (`.mbm`)

- **T-1** Los códigos `{XXXX}` quedan intactos y en el mismo orden que en el inglés, y el mensaje termina en `{FFFF}` como el original. En las tablas pasa lo mismo con `%d` y `%s`. (`codigos`)
  - `{F804}{0500}` ... `{F804}{0000}`: color.
  - `{F843}{0000}` y otros: insertan un nombre.
  - `{F812}Nombre{0000}`: el nombre de quien habla. Va en su propia etiqueta, fuera de la caja: no cuenta para el ancho (T-3) y el instalador no lo parte. Se escribe como diga el glosario (G-3).
  - `{F802}`: página nueva.
  - `{FFFF}`: fin del mensaje.
- **T-2** Saltos de línea:
  - El traductor ve el inglés en **forma de lectura**: sin los saltos que solo servían para que el párrafo cupiera, y con los fijos (opciones de una lista, una frase en su propio renglón) marcados `{F801}`.
  - La traducción lleva exactamente esos `{F801}`, ni más ni menos. Los demás saltos los pone el instalador según el ancho. (`saltos`)
- **T-3** La caja:
  - **Mensajes:** el instalador parte cada renglón por palabras para que ninguno pase del renglón más ancho del inglés en el mismo archivo, medido en píxeles con la fuente del juego. Así, una página no puede tener más renglones que la página más larga del inglés en ese archivo. (`caja`)
  - **Tablas:** ningún renglón puede ser más ancho que el más ancho del inglés en la misma columna, ni tener más renglones que el inglés. (`ancho`, `renglones`)

## Tablas (`.tbb`)

- **T-4** Cada texto de tabla tiene un largo máximo en bytes (`max` en el lote). Las letras españolas ocupan 2 bytes y el resto, 1. Si no cabe, se acorta; el instalador no instala un texto que no cabe. (`bytes`)
- **T-7** En las tablas solo se traducen los textos que ve el jugador. Los nombres internos (archivos, etiquetas) no se exportan y no se tocan.

## Caracteres

- **T-5** Solo se usan caracteres que tiene la fuente del juego. (`caracteres`)
  - Las letras españolas son 16: á é í ó ú ü ñ, sus mayúsculas, ¿ y ¡ ([tools/letters.py](tools/letters.py)).
  - Comillas y apóstrofo: `“ ” ’`, los del inglés. Las rectas `" '` no existen en los mensajes.
  - Lo que la fuente no tiene, como `« »` o `—`, el validador lo avisa.

## Qué se traduce

- **T-6** El japonés que quedó en los archivos no se traduce hasta saber si el juego lo muestra. Los lotes lo saltan solos. [PLAN]
- **T-8** Toda línea del lote se traduce completa: ninguna queda vacía, igual al inglés ni con frases en inglés mezcladas. (`vacia`, `sin_traducir`, `ingles_mezclado`)
