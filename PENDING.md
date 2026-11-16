# Pendientes

La cola del usuario: lo que ninguna regla cubre, las líneas delicadas con su solución provisional y los términos por decidir. Nada de esto cambia el texto hasta que el usuario lo decide. La decisión se anota en [DECISIONS.md](DECISIONS.md) y, si es una regla, en su documento.

Formato: `- [ ] \`clave\` (rol, motivo): «fragmento» → «propuesta». Por qué.` `tools/review.py` agrega aquí, solo, los hallazgos sin regla de cada lote.

## Para la prueba en el juego

Se deciden al ver la pantalla (DECISIONS 2026-11-16).

- [ ] `Attack` del tutorial (terminólogo): «Choose ”Attack” from the list of commands.» (BtlEvent001#4, BtlEventSub150#4) → «Atacar». Si el menú de combate es una textura y queda en inglés, el tutorial tiene que citar «Attack». Se ve en el juego.
- [ ] `addon/testdata/content24/tbl/SkillName.tbb#0.5.2` (terminólogo, sentido dudoso): *Forfeit* → «Confiscación» (provisional). Puede ser quitarle algo al rival o renunciar a algo; el contenido descargable no trae la descripción. Alternativa: «Renuncia». Se ve en el juego.
- [ ] *A. [nombre]* (*A. Lucifer*, *A. Demon Army*, *A. Angel*; 26 entradas) (terminólogo, duda): el inglés no dice qué es la *A.* Propuesta: se deja «A. Lucifer», «Ejército de demonios A.»... hasta verlo en el juego.
- [ ] Lote historia-009 (orquestador): no se quitó el espacio de «{F801} {F801}» en BtlEventSub131#11 y BtlEventSub147#6 (viene del inglés: es una página con un solo espacio). Ver en el juego si esa página en blanco hace falta.
- [ ] `map/m026/m026.mbm#2` (reviewer, sin regla): «First» → «Primero». Sin contexto de qué lista abre; ver en el juego.
- [ ] `battle/Legion/LegionMsg.mbm#212` (orquestador, T-2): el inglés tiene *You make me sick{F801}Oh dear...* sin punto, y check.py lo lee como un salto blando (4 frases en vez de 5). Queda «Me das asco. Ay, cielos...» en un solo fragmento, como lo cuenta la herramienta. Si en el juego cada {F801} es una frase suelta de la horda, se separa.
