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

## De los lotes

### Lote ejecutable-001 (2026-11-16)

- [ ] `exefs/code.bin#0x3CE760` (delicadas, nombre de lugar): «Spring of Healing» → «Manantial curativo». Con adjetivo, como «manantial curativo» de fountain/mes_data.mbm#1 y «Manantial vital» de SMT V; «de curación» suena a calco. Alternativa: «Manantial de curación».
- [ ] `exefs/code.bin#0x45CFD0` (delicadas, sufijo tras el nombre): «[nombre]’s demon information» → «[nombre]: información del demonio». Es de las tarjetas DDS (StreetPass), que llevan un solo demonio; como el orden no cambia, los dos puntos lo dejan como título. Alternativa: « - información del demonio».
- [ ] `exefs/code.bin#0x45CFF9` (delicadas, sufijo tras el nombre): «[X] encounter list» → «[X]: lista de encuentros», con el mismo separador que la anterior y «encuentros» como *StreetPass tags* (camp/PlayLogTable.tbb). Alternativa: « - lista de encuentros».
- [ ] `exefs/code.bin#0x45D4B1` (delicadas, referencia): «Sunshine 60» → «Sunshine 60» (sin cambio). Es el edificio de Ikebukuro (el mapa tiene *Sunshine Front*), un nombre propio. Alternativa: «Edificio Sunshine 60», que agrega una palabra (E-3).
- [ ] `exefs/code.bin#0x45D54B` (delicadas, habilidad): «Die for Me!» → «¡Muere por mí!» (sin cambio). Es el nombre oficial de SMT V (G-1) y retoma el «¿Morirías por mí?» de Alice. Alternativa: «¡Muérete por mí!».
- [ ] `exefs/code.bin#0x45D562` (delicadas, humor): «Watch Us, Maruo!» → «¡Míranos, Maruo!» (sin cambio). Los seguidores a su líder, con tú (ficha). Alternativa: «¡Mírenos, Maruo!», con usted, si se marca la veneración.
- [ ] `exefs/code.bin#0x45D583` (delicadas, humor): «Gaze Upon Maruo!» → «¡Contemplen a Maruo!» (sin cambio). Maruo habla de sí en tercera persona (ficha); «contemplen» conserva lo grandilocuente de *gaze upon* y no repite el «Míranos» anterior. Alternativa: «¡Admiren a Maruo!».
- [ ] `exefs/code.bin#0x45D711` (delicadas, habilidad): «King Bufula» → «Rey Bufula» (antes «Bufula del Rey»). Es el nombre oficial de SMT V (G-1), como «Jack Bufula». Alternativa: «Bufula del Rey».
- [ ] `exefs/code.bin#0x45D8C6` (delicadas, sentido dudoso): «High Poly Pleroma» → «Pleroma superior múltiple» (sin cambio). *Poly* es «muchos»; no se sabe de qué (quizá la magia de varios elementos, battle/SkillHelpMess.mbm#497) y no se agrega. Sigue la serie del lote. Alternativa: «Pléroma múltiple alto», si la serie pasa a la forma de SMT V («Pléroma de fuego alto»).
- [ ] `exefs/code.bin#0x430B3C` (delicadas, hablante desconocido): «Dagger... heavy... How shall I show my power!?» → «Daga... pesada... ¡¿Cómo mostraré mi poder?!» (sin cambio). No se sabe quién habla (va antes de «The Jade Dagger has lost its power...»); no marca género, y el futuro conserva el tono de *shall*. Alternativa: «¡¿Cómo voy a demostrar mi poder?!». Se ve en el juego.
- [ ] `exefs/code.bin#0x3B1DB8` (delicadas, bytes): «End» → «Fin» (sin cambio). «Terminar», el del menú de fusión (GLOSSARY), ocupa 8 bytes y caben 7; «Fin» sirve de botón y de etiqueta, como los otros dos *End* del ejecutable. Alternativa: «Acabar» (6). Se ve en el juego.
- [ ] `exefs/code.bin#0x245924` (delicadas, ambiguo): «Engage» → «Combatir» (sin cambio). Va con «Please touch the icon.» en el fondo del menú (CommonBg); en un juego, *engage* suele ser entrar en combate. Alternativa: «Activar», si enciende algo. Se ve en el juego.
- [ ] `exefs/code.bin#0x45BC40` y #0x45BC45, #0x45BC4A, #0x45BC4F, #0x45BC54 (delicadas, siglas desconocidas): «MA», «DF», «PR», «AT», «HT» → sin cambio. Están junto a nombres de shader y de animaciones (*shadowmap*, *TIRED*, *ANGRY*): pueden ser internas (T-7). Alternativa: si no se ven en el juego, sacarlas de la cuenta; si se ven, traducirlas según lo que muestren (caben 2 letras).
