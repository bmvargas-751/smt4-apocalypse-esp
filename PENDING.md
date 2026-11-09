# Pendientes

La cola del usuario: lo que ninguna regla cubre, las líneas delicadas con su solución provisional y los términos por decidir. Nada de esto cambia el texto hasta que el usuario lo decide. La decisión se anota en [DECISIONS.md](DECISIONS.md) y, si es una regla, en su documento.

Formato: `- [ ] \`clave\` (rol, motivo): «fragmento» → «propuesta». Por qué.` `tools/review.py` agrega aquí, solo, los hallazgos sin regla de cada lote.

## Decisiones generales

- [ ] **Registro de época** (STYLE E-31): dioses y demonios que hablan a la antigua. En THL quedó «de época, sin *vosotros*». ¿Se mantiene? Se decide al llegar a la Historia (DECISIONS 2026-11-08).
- [ ] **«¡Demonios!» y «¡Diablos!»**: en este juego se vuelven ambiguas. ¿Se evitan? (PLAN, notas de IVA)
- [ ] **El texto original del encargo de 11 secciones**: los roles parten del resumen fiel de THL ([TEAM.md](TEAM.md#el-encargo)) hasta que aparezca.

## Términos

Candidatos de SMT V que en IVA tienen otro sentido (G-2). No salen en la Interfaz: se deciden al llegar a su sección (DECISIONS 2026-11-08).

- [ ] `Man` (terminólogo, otro sentido): «Huh? You don’t have it? Man, this sucks.» (battle/talk/TalkToneBoss51.mbm#60; 41 veces) → no se fija como término. En SMT V es una etiqueta de quien habla (*Hombre*); en IVA casi siempre es la interjección (*vaya*, *qué mala suerte*, según el tono) o parte de otra etiqueta (*Man’s voice*).
- [ ] `Four Heavenly Kings` (terminólogo, otro sentido): «one of the Four Heavenly Kings in Buddhist lore» (status/profile.mbm#396) → «Cuatro Reyes Celestiales». En SMT V es una habilidad; en IVA, el grupo de deidades budistas.
- [ ] `Gungnir` (terminólogo, otro sentido): «I will give you my spear, Gungnir.» (battle/event/BtlEvent041/BtlEvent041.mbm#102) → «Gungnir». En SMT V es una habilidad; en IVA, la lanza de Odín.
- [ ] `Ragnarok` (terminólogo, otro sentido): «It is said that it will live through Ragnarok.» (status/profile.mbm#60; 11 veces) → «Ragnarok» (*el Ragnarok*). En SMT V es una habilidad; en IVA, el fin del mundo de la mitología nórdica.
- [ ] `Universe Ring` (terminólogo, otro sentido): «Qiankun Quan (Universe Ring)» (status/profile.mbm#225) → «Anillo universal», como SMT V. En SMT V es una habilidad; en IVA, el arma de un mito.
- [ ] `Walpurgisnacht` (terminólogo, otro sentido): «Bilwis appears on Walpurgisnacht» (status/profile.mbm#444) → «la noche de Walpurgis». En SMT V es una habilidad (*Noche de Walpurgis*); en IVA, la fiesta.
- [ ] `Mother Earth` (terminólogo, otro sentido): «A Mother Earth goddess of Japanese lore» (status/profile.mbm#43) → «diosa madre de la tierra». En SMT V es una habilidad; en IVA, una descripción.
- [ ] `Teacher` (terminólogo, otro sentido): «Teacher...? You’re alright, you know?» (battle/talk/TalkToneBoy.mbm#313) → no se fija: *profesor* o *maestro* según la línea. En SMT V es una etiqueta de quien habla.
- [ ] `Concentrate` (terminólogo, otro sentido): «Concentrate your fire!» (battle/PartnerAttack.mbm#90) → no se fija; es el verbo común. En SMT V es una habilidad.
- [ ] `Fortune` (terminólogo, otro sentido): «she turns the Wheel of Fortune» (status/profile.mbm#40; también *Seven Gods of Fortune*, #395) → no se fija; *fortuna* (*la Rueda de la Fortuna*, *los Siete Dioses de la Fortuna*). En SMT V es un objeto (*Predicción*).
- [ ] `Confusion` (terminólogo, otro sentido): «Confusion and uncertainty is written across your friends’ faces.» (event/e063/e063.mbm#23) → no se fija; es la palabra común. En SMT V es un estado alterado que IVA no tiene (IVA usa *Panic*).
- [ ] `Resist Fire` (terminólogo, otro sentido): «Resist Fire/Ice/Elec/Force Weak against Phys/Gun/Light/Dark» (item/ItemHelpMess.mbm#467) → «Resiste fuego/hielo/electricidad/choque». En SMT V es el nombre de una habilidad; en IVA, la descripción de las afinidades de un equipo. *Force* ⇒ *Choque* sale de SMT V.

## De los lotes

- [ ] `battle/ResultMsg.mbm#17` (delicadas, registro de época): «Ye gods, are you broke!? I’ll come again when you have more money.» → «¡Por los dioses! ¡¿Estás en la ruina?! Volveré cuando tengas más dinero.» Provisional hasta decidir E-31. *¡Por los dioses!* es una exclamación hecha en español con el mismo sabor antiguo que *Ye gods*, y conserva los dioses en plural, que van con Caronte. Como no lleva verbo, sirve para cualquier registro de época que se decida, sin *vosotros*. No es grosería, igual que en el inglés (ficha), y no usa *¡Demonios!* ni *¡Diablos!*, que siguen pendientes. Alternativas: «¡Dioses!», más corta; «¡Válganme los dioses!», si E-31 pide un tono más marcado.

### Lote interfaz-001 (2026-11-08)

- [ ] `battle/Common/common.mbm#54` (reviewer, sin regla): «gracias a Ánimo perdurable» → «(decidir en el glosario)». «Enduring Cheer» no está en el glosario; «Enduring Soul» es «Alma inmortal». Falta decidir si «Enduring» va igual (inmortal) o distinto (perdurable).

### Lote interfaz-003 (2026-11-08)

### Tablas (2026-11-08)

- [ ] **Clases de Mikado** (mikado/MikadoTable.tbb#2.0.0, #2.2.0): *Luxurors* y *Casualries* son palabras inventadas (*luxury*, *casual*). Propuesta: se dejan, «los Luxurors», «los Casualries» (*Residencias de los Luxurors*, 27/31). Alternativa con el sentido: «Aristócratas», «Plebeyos». Si se quiere un juego de palabras en español, va a delicadas (E-23).
- [ ] `Bartender`, `New bartender` (terminólogo, quien habla; 280 y 44 veces como etiqueta) (quest_center/common/NpcHaichiTable.tbb#0.22.0, #0.90.0) → «Tabernero», «Nuevo tabernero», por *K's Tavern* → «Taberna de K». Alternativa: «Cantinero». El género sigue pendiente (E-40): si alguno es mujer, «Tabernera».
- [ ] *Jack Union* (battle/NKMSortIndex.tbb#1.706.0) (terminólogo, juego de palabras): juega con *Union Jack*. Va a delicadas (E-23). Provisional: «Unión de los Jack» (18/31).
- [ ] *A. [nombre]* (*A. Lucifer*, *A. Demon Army*, *A. Angel*; 26 entradas) (terminólogo, duda): el inglés no dice qué es la *A.* Propuesta: se deja «A. Lucifer», «Ejército de demonios A.»... hasta verlo en el juego.
- [ ] **Categorías de misiones** (event/quest/QuestData.tbb, SubQuestData.tbb, columna 8, max 55) (terminólogo, duda): *[Ast]* → «[Apo]», *[Esc]* → «[Esc]», *[Grd]* → «[Def]», *[Int]* → «[Inf]», *[Inv]* → «[Inv]», *[Otr]* → «[Otr]», *[Rsc]* → «[Res]», *[Spc]* → «[Esp]», *[Tgt]* → «[Obj]». El juego no dice qué abrevian; leído de las misiones: apoyo, escolta, defensa, infiltración, investigación, otros, rescate, especial, objetivo. *Exam (Easy/Hard): X* → «Examen (fácil/difícil): X».

### Lote tablas-001 (2026-11-08)

Títulos de la tarjeta DDS (camp/CampCecTable.tbb, max 31): el ancho de la columna es 121 px, el de *Nurturer of Bonds*, y eso deja unos 16 caracteres. Las versiones largas («Licenciado en demonios», «Condenado al error», «Anfitrión de fantasmas») no caben (T-3). Cada título lleva en la tabla un contador y una meta. Los de cada contador se leen como una serie.

- [ ] `battle/NKMSortIndex.tbb#1.706.0` (delicadas, juego de palabras): «Jack Union» → «Unión Jack» (11 bytes, 73/200 px). Invierte el orden de *Union Jack*, la bandera británica, para nombrar un grupo de demonios Jack. En español, la bandera también se llama *Union Jack*, así que «Unión Jack» se reconoce y además se lee como «la unión de los Jack». Alternativa: «Unión de los Jack» (18, 119 px), más clara pero sin el chiste.
- [ ] `camp/CampCecTable.tbb#0.72.0` (delicadas, juego de palabras): «Ghost Host» → «Alojafantasmas» (14, 101 px). La rima nombra al que hospeda a un fantasma. «Alojafantasmas» dice eso mismo con un compuesto juguetón, como «Rompedominios» o «Cazademonios» de la misma lista, y suena a *Cazafantasmas*. El actual «Huésped fantasma» y «Anfitrión fantasma» (122 px, no cabe) se leen como *X fantasma*, igual que *pueblo fantasma*: un huésped que no existe o que es un fantasma. Alternativa: «Casa embrujada» (108 px), que convierte al jugador en la casa encantada.
- [ ] `camp/CampCecTable.tbb#0.27.0`, `#0.28.0`, `#0.29.0` (delicadas, parodia): «Demon B.A.», «Demon M.S.», «Demon PhD» → «Lic. en demonios» (114 px), «M. en demonios» (106), «Dr. en demonios» (110). Son tres metas del mismo contador, una serie de títulos académicos. Se cambia solo el del medio. «Máster demonios» no lleva preposición, y «Mtro. en demonios» (126) y «Mag. en demonios» (122) no caben. *M.* es la abreviatura de *Maestro* en México (*M. en C.*), y en la serie Lic. → M. → Dr. cada lector la completa con su palabra (maestro, magíster, máster). Alternativa: «Mg. en demonios» (114), la abreviatura de *magíster* en Sudamérica.
- [ ] `camp/CampCecTable.tbb#0.35.0` (delicadas, palabra inventada): «Slowbie» → «Novatortuga» (11, 83 px). Junta *slow* y *newbie*. «Novatortuga» hace lo mismo con *novato*, que es el título #0.1.0 de la misma lista (*Rookie*), y *tortuga*, la burla común para el lento. El actual «Lentito» pierde al novato. Alternativa: «Novato tortuga» (102 px), sin palabra inventada.
- [ ] `camp/CampCecTable.tbb#0.41.0` (delicadas, sentido dudoso): «Friend Blaster» → «Fuego amigo» (11, 86 px). El inglés dice «el que les dispara a los amigos». *Fuego amigo*, la frase hecha de *friendly fire*, junta los mismos dos elementos y sirve de apodo. La tabla no dice qué cuenta su contador (meta 10). Si en el juego resulta otra cosa, se revisa. Alternativa: «Mataamigos» (80 px), en una sola palabra; el actual «Mata amigos» está mal separado.
- [ ] `camp/CampCecTable.tbb#0.55.0` (delicadas, sentido dudoso): «Sighted» → «Vidente» (7, 50 px), sin cambio. Comparte contador con *Disciple!* (#0.56.0), y los títulos #0.53–64 van de dos en dos, uno por acompañante. *Vidente* es «que ve» y también «el que ve lo que otros no», justo el chiste. *Avistado* sería el sentido contrario.
- [ ] `camp/CampCecTable.tbb#0.25.0` (delicadas, palabra inventada): «Errorbound» → «Esclavo del error» (17, 114 px). *-bound* como en *hellbound* o *spellbound*: atado o condenado a algo. Su meta es 1, así que se gana con un solo error. «Esclavo del error» es una frase hecha (como *esclavo de la moda*) con el mismo tono épico en broma. El actual «Atado al error» es literal, y «Condenado al error» (132 px) no cabe. Alternativas: «Preso del error» (104), «Rumbo al error» (104).

### Lote tablas-001 (2026-11-08)

- [ ] `camp/ConfigTable.tbb#0.0.66` (reviewer, sin regla): «Guerra» → «(ninguna propuesta cabe)». «Guerra» mide 46 px y el límite es 26 (lo que mide «War»); ninguna palabra que signifique guerra cabe, «Gue.» da 30. Decide el usuario si la medida de la columna manda aquí: cada dificultad está en su propia columna y «Apocalipsis» llega justo a 75/75.
- [ ] `battle/NKMSortIndex.tbb#0.61.0` (reviewer, sin regla): «Posthumano» → «(ninguna propuesta natural cabe)». 83 px; el límite es 74 (lo que mide «Posthuman»). «Poshumano» da 78 y «Posthum.» 62. El término está fijado en GLOSSARY (razas); decide el usuario.
- [ ] `battle/NKMSortIndex.tbb#0.61.16` (reviewer, sin regla): «Sobrehumano» → «(ninguna propuesta natural cabe)». 94 px; el límite es 83. «Ultrahumano» da 85 y «Sobrehum.» 73. El término está fijado en GLOSSARY (razas); decide el usuario.
- [ ] `camp/ConfigTable.tbb#0.0.42`, `#0.0.54` (reviewer, T-3 frente a GLOSSARY): «Escaramuza» (78 px) y «Conflicto» (59 px) pasan el ancho de su columna (57 y 50). Propuestas que caben: «Refriega» (55) y «Disputa» (49). Cada dificultad está sola en su columna, así que el límite medido es el ancho de su propio inglés y puede ser más estricto que la pantalla real.
- [ ] `camp/CampCecSample.tbb#0.0.14`, `#0.1.14`, `#0.2.14` (reviewer, E-40 y T-3): «Cazador Yamato/Kaizuka/Yuki»: el género de estos cazadores de ejemplo no se sabe y «Cazador» no cabe en el ancho (111 px de 100). Propuesta: «Caz. Yamato», «Caz. Kaizuka», «Caz. Yuki» (84 px), sin género.
- [ ] `battle/NKMSortIndex.tbb` (reviewer, glosario): *Awakened* → «Despertado» (glosario) mide 76 px de 74; el traductor puso «Despierto». ¿Se cambia el glosario?
