# Pendientes

La cola del usuario: lo que ninguna regla cubre, las líneas delicadas con su solución provisional y los términos por decidir. Nada de esto cambia el texto hasta que el usuario lo decide. La decisión se anota en [DECISIONS.md](DECISIONS.md) y, si es una regla, en su documento.

Formato: `- [ ] \`clave\` (rol, motivo): «fragmento» → «propuesta». Por qué.` `tools/review.py` agrega aquí, solo, los hallazgos sin regla de cada lote.

## Decisiones generales

- [ ] **Registro de época** (STYLE E-31): dioses y demonios que hablan a la antigua. En THL quedó «de época, sin *vosotros*». ¿Se mantiene? Se decide al llegar a la Historia (DECISIONS 2026-11-08).
- [ ] **«¡Demonios!» y «¡Diablos!»**: en este juego se vuelven ambiguas. ¿Se evitan? (PLAN, notas de IVA)
- [ ] **El texto original del encargo de 11 secciones**: los roles parten del resumen fiel de THL ([TEAM.md](TEAM.md#el-encargo)) hasta que aparezca.

## Términos

Candidatos de SMT V que en IVA tienen otro sentido (G-2). No salen en la Interfaz: se deciden al llegar a su sección (DECISIONS 2026-11-08).

- [ ] `Divine` (terminólogo, otro sentido): la raza *Divine* (battle/NKMSortIndex.tbb#0) → «Divino», como SMT V; casi siempre va dentro de *Divine Powers* («Poderes Divinos»), así que no se fija hasta las Tablas.
- [ ] `Man` (terminólogo, otro sentido): «Huh? You don’t have it? Man, this sucks.» (battle/talk/TalkToneBoss51.mbm#60; 41 veces) → no se fija como término. En SMT V es una etiqueta de quien habla (*Hombre*); en IVA casi siempre es la interjección (*vaya*, *qué mala suerte*, según el tono) o parte de otra etiqueta (*Man’s voice*).
- [ ] `Human` (terminólogo, otro sentido): «Human, I shall purge your soul!» (battle/talk/TalkToneBoss13.mbm#18; 40 veces) → «Humano» para la raza (battle/NKMSortIndex.tbb#0) y para llamar a alguien; como adjetivo (*Human souls*, *Human kids*) va *humano/humana* según el sustantivo. Si se fija *Human → Humano*, el validador avisaría en cada adjetivo femenino.
- [ ] `Lady` (terminólogo, otro sentido): «Lady Amaterasu» (battle/event/BtlEventSub132/BtlEventSub132.mbm#1; 22 veces) → «Dama» para la raza (como SMT V); delante de un nombre es un tratamiento y se decide aparte (propuesta: *la señora Amaterasu*, o *lady* si se quiere conservar). La mayoría de las veces en IVA es el tratamiento.
- [ ] `Chaos` (terminólogo, otro sentido): «Strong vs. Chaos demons» (battle/SkillHelpMess.mbm#43); «Chaos is the essence of evolution.» (battle/DevilMsg/dMsg_Boss15.mbm#2; 18 veces) → «Caos» en todos los sentidos. En SMT V es una raza; en IVA es también la raza, pero sobre todo la tendencia (*Law*, *Neutral*, *Chaos*) y la idea.
- [ ] `Holy` (terminólogo, otro sentido): «Holy hell! What is that!?» (event/e050/e050.mbm#41; también *Four Holy Beasts*, status/profile.mbm#49) → «Sacra» para la raza (como SMT V); en las exclamaciones va un equivalente según la intensidad (E-22) y en las descripciones, *sagrado/sagrada*.
- [ ] `Night` (terminólogo, otro sentido): «And returned as Night Mokoi!» (battle/talk/TalkSystem.mbm#91); «’Night.» (ones_room/onesRoom.mbm#9) → «Nocturno» para la raza (como SMT V); *’Night* es *buenas noches* y *A Midsummer Night’s Dream* (status/profile.mbm#234) es el título de la obra (*El sueño de una noche de verano*).
- [ ] `Counter` (terminólogo, otro sentido): «Effect: Counter when attacked» (item/ItemHelpMess.mbm#673); «the Counter- Demon Force» (map/m003/m003.mbm#0) → «Contraataque» para el efecto (como la habilidad de SMT V); *Counter-Demon Force* es el nombre de un grupo y se decide aparte.
- [ ] `Grimoire` (terminólogo, otro sentido): «Light Grimoire», «Heavy Grimoire», «Friend Grimoire» (item/ItemTable.tbb#1.10.0, #1.11.0, #6.3.0) → «Grimorio» (*Grimorio ligero*...). En SMT V es un objeto; en IVA solo va dentro de otros objetos. Los nombres completos se deciden con las Tablas.
- [ ] `Seal` (terminólogo, otro sentido): «Seal of Delusion», «Seal of Rejection» (item/ItemTable.tbb#0.33.0, #0.34.0) → «Sello» (*Sello de la ilusión*...). En SMT V es un estado alterado que IVA no tiene; aquí es parte del nombre de objetos.
- [ ] `Four Heavenly Kings` (terminólogo, otro sentido): «one of the Four Heavenly Kings in Buddhist lore» (status/profile.mbm#396) → «Cuatro Reyes Celestiales». En SMT V es una habilidad; en IVA, el grupo de deidades budistas.
- [ ] `Gungnir` (terminólogo, otro sentido): «I will give you my spear, Gungnir.» (battle/event/BtlEvent041/BtlEvent041.mbm#102) → «Gungnir». En SMT V es una habilidad; en IVA, la lanza de Odín.
- [ ] `Gae Bolg` (terminólogo, otro sentido): «Gae Bolg» (item/ItemTable.tbb#2.92.0; también status/profile.mbm#37) → «Gae Bolg». En SMT V es una habilidad; en IVA, un arma (objeto) y la lanza del mito.
- [ ] `Ragnarok` (terminólogo, otro sentido): «It is said that it will live through Ragnarok.» (status/profile.mbm#60; 11 veces) → «Ragnarok» (*el Ragnarok*). En SMT V es una habilidad; en IVA, el fin del mundo de la mitología nórdica.
- [ ] `Universe Ring` (terminólogo, otro sentido): «Qiankun Quan (Universe Ring)» (status/profile.mbm#225) → «Anillo universal», como SMT V. En SMT V es una habilidad; en IVA, el arma de un mito.
- [ ] `Walpurgisnacht` (terminólogo, otro sentido): «Bilwis appears on Walpurgisnacht» (status/profile.mbm#444) → «la noche de Walpurgis». En SMT V es una habilidad (*Noche de Walpurgis*); en IVA, la fiesta.
- [ ] `Mother Earth` (terminólogo, otro sentido): «A Mother Earth goddess of Japanese lore» (status/profile.mbm#43) → «diosa madre de la tierra». En SMT V es una habilidad; en IVA, una descripción.
- [ ] `Purgatorium` (terminólogo, otro sentido): «Go to the Purgatorium Terminal.» (camp/SortMenuTable.tbb#0.66.24) → «Purgatorium». En SMT V es una habilidad (*Purgatorio*); en IVA, un lugar, que se decide con los demás lugares. Alternativa: «Purgatorio».
- [ ] `Ruler of Chaos` (terminólogo, otro sentido): «Ruler of Chaos» (camp/CampCecTable.tbb#0.77.0) → «Regente del caos», como SMT V. En SMT V es una habilidad; en IVA, un título de la tarjeta de StreetPass. Ojo con el género: el título lo elige el jugador (E-40).
- [ ] `Researcher` (terminólogo, otro sentido): «Researcher» (camp/CampCecTable.tbb#0.26.0) → «Investigador». En SMT V es una etiqueta de quien habla; en IVA, un título de la tarjeta de StreetPass (mismo caso de género que el anterior).
- [ ] `Teacher` (terminólogo, otro sentido): «Teacher...? You’re alright, you know?» (battle/talk/TalkToneBoy.mbm#313) → no se fija: *profesor* o *maestro* según la línea. En SMT V es una etiqueta de quien habla.
- [ ] `Worker` (terminólogo, otro sentido): «Excavation Worker Quarters» (map/all/MapNextPointTable.tbb#0.35.8) → no se fija; es parte del nombre de un lugar (Tablas). En SMT V es una etiqueta de quien habla.
- [ ] `Yoko` (terminólogo, otro sentido): «Yoko Jewelry» (map/all/ms_search_Table.tbb#0.10.0) → no se fija; es el nombre de una tienda (Tablas). En SMT V es un personaje.
- [ ] `Maria` (terminólogo, otro sentido): «Black Maria» (battle/NKMSortIndex.tbb#1.367.0) → «Black Maria». En SMT V es el demonio *María*; en IVA solo va en el nombre de otro demonio, *Black Maria*, que SMT V no tiene. Alternativa: «María Negra».
- [ ] `Concentrate` (terminólogo, otro sentido): «Concentrate your fire!» (battle/PartnerAttack.mbm#90) → no se fija; es el verbo común. En SMT V es una habilidad.
- [ ] `Fortune` (terminólogo, otro sentido): «she turns the Wheel of Fortune» (status/profile.mbm#40; también *Seven Gods of Fortune*, #395) → no se fija; *fortuna* (*la Rueda de la Fortuna*, *los Siete Dioses de la Fortuna*). En SMT V es un objeto (*Predicción*).
- [ ] `Soda` (terminólogo, otro sentido): «Soda Bottle» (item/ItemTable.tbb#4.104.0) → no se fija. En SMT V es un objeto (*Refresco*); en IVA solo va dentro de *Amrita Soda* (oficial) y de *Soda Bottle*, otro objeto que se decide con las Tablas.
- [ ] `Confusion` (terminólogo, otro sentido): «Confusion and uncertainty is written across your friends’ faces.» (event/e063/e063.mbm#23) → no se fija; es la palabra común. En SMT V es un estado alterado que IVA no tiene (IVA usa *Panic*).
- [ ] `Resist Fire` (terminólogo, otro sentido): «Resist Fire/Ice/Elec/Force Weak against Phys/Gun/Light/Dark» (item/ItemHelpMess.mbm#467) → «Resiste fuego/hielo/electricidad/choque». En SMT V es el nombre de una habilidad; en IVA, la descripción de las afinidades de un equipo. *Force* ⇒ *Choque* sale de SMT V.

## De los lotes
