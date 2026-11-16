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
- [ ] **Ejecutable** (orquestador): sus textos van en letras de un byte, no en el ancho completo del inglés; revisar en el juego que se vean bien (con tildes) y que quepan en su lugar (elementos, estados, menús).
- [ ] `exefs/code.bin#0x430B3C` (delicadas, hablante desconocido): «Dagger... heavy... How shall I show my power!?» → «Daga... pesada... ¡¿Cómo mostraré mi poder?!» (sin cambio). No se sabe quién habla (va antes de «The Jade Dagger has lost its power...»); no marca género, y el futuro conserva el tono de *shall*. Alternativa: «¡¿Cómo voy a demostrar mi poder?!». Se ve en el juego.
- [ ] `exefs/code.bin#0x245924` (delicadas, ambiguo): «Engage» → «Combatir» (sin cambio). Va con «Please touch the icon.» en el fondo del menú (CommonBg); en un juego, *engage* suele ser entrar en combate. Alternativa: «Activar», si enciende algo. Se ve en el juego.
- [ ] `exefs/code.bin#0x45BC40` y #0x45BC45, #0x45BC4A, #0x45BC4F, #0x45BC54 (delicadas, siglas desconocidas): «MA», «DF», «PR», «AT», «HT» → sin cambio. Están junto a nombres de shader y de animaciones (*shadowmap*, *TIRED*, *ANGRY*): pueden ser internas (T-7). Alternativa: si no se ven en el juego, sacarlas de la cuenta; si se ven, traducirlas según lo que muestren (caben 2 letras).
- [ ] `exefs/code.bin#0x45E527` (delicadas, glosario y bytes): «Endure» → «Últ.aliento» (12/12; antes «Aguante»). «Último aliento» (SMT V) da 15 bytes y «Últ. aliento», 14; sin el espacio cabe y coincide con «Otorga Último aliento» (SkillHelpMess#232). Alternativa: excepción al glosario, «Aguante», con #232 → «Otorga Aguante». Aprobado «Últ.aliento»; si en pantalla se ve muy apretado, se cambia.
- [ ] `exefs/code.bin#0x487746` y #0x487768 (delicadas, siglas desconocidas): «L Tokyo», «C Tokyo» → «Tokio L», «Tokio C» (sin cambio). El inglés no dice qué son la L y la C; están junto a «Test» y «Underground», en lo que parece una lista de prueba. Se dejan las letras, detrás del nombre como en «Distrito subterráneo A». Si en el juego se ve qué son, va el nombre completo (caben 17 y 15 bytes). Alternativa: «L Tokio», «C Tokio», en el orden del inglés.

## De los lotes
