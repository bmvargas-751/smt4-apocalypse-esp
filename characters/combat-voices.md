# Voces de combate (6.7)

Quién habla en los mensajes de demonios en combate y qué ficha aplica. No repite las fichas: solo dice cuál usar y qué cambia aquí. Sin spoilers.

## Cómo se asigna

- **battle/DevilMsg/dMsg_X.mbm** (23 líneas): lo que dice un demonio aliado al aprender una habilidad (#0-2), al llenarse (#3), al cambiar una habilidad (#4-6), al mutar (#7-11), al dar un regalo (#12-14), al enseñar una habilidad por susurro (#15-16) y al presentarse tras la fusión (#17). #18-19 son opciones del menú; #20, frases del jugador entre comillas (*”I'm satisfied.” ”Let me think...”*); #21, Mido (ver abajo); #22, *Dummy* salvo en los Partner (frase de despertar).
- **camp/CecDevilMsg/dMsg_X.mbm** (9 líneas): el demonio que vuelve de StreetPass: crecimiento (#0-2), transformación (#3-5) y recuerdo (#6-8).
- **X es el tono**, el mismo nombre que battle/talk/TalkToneX.mbm: el ejecutable arma las rutas con la misma tabla de nombres (`battle/talk/TalkTone%s.mbm`, `battle/DevilMsg/%s.mbm`; tabla en exefs/code.bin, 0x47a04c-0x47a194: Boy = 0 ... Boss74 = 112, Partner01-03 = 113-115). El demonio que lo usa sale del byte 56 de battle/NKMBaseTable.tbb, como en las fichas *talk-*. Por eso la ficha de cada archivo es la del mismo tono en la negociación.
- **Partner04-09** no están en la tabla de nombres, pero NKMBaseTable asigna los tonos 116-121 a los compañeros y el texto de cada archivo coincide con el tono 112 + N (ver la tabla).
- **Género (E-41):** los tonos de personalidad (Beast, Boy, Gal...) y los compartidos (Boss08, Boss42, HumanMale, Boss68-74...) los usan demonios distintos: sus líneas no marcan el género de quien habla. Donde el inglés lo marca, va en las notas.
- **Columnas battle y camp:** líneas con inglés / líneas del archivo (en battle sin contar #18-21, que son comunes). Las demás son marcadores en japonés (*(仮)…メッセージ*), *Dummy*, *ダミー* o *???*. El PLAN ya anota que hay que ver si el juego los muestra.

## Líneas comunes de battle/DevilMsg

- **#21 (113 de los 124 archivos; en Partner y Skull es *Dummy*):** Mido, con su etiqueta (*...It seems there was an error in your fusion.*). Ficha: [mido.md](mido.md) (usted con el jugador, aprobado). Tres variantes del mismo texto (*than intended*, *than the planned result*, *than planned result*): conviene una sola traducción.
- **#18-20:** opciones del menú y frases del jugador. No son de ningún demonio.

## Tabla

| Tono (`dMsg_…`) | battle | camp | Ficha | Notas |
|---|---|---|---|---|
| Beast | 18/19 | 9/9 | [personalidad-beast.md](personalidad-beast.md) | Mayúsculas y habla rota, como la ficha (*ME ACCEPT.*, #5). |
| Boss01 | 0/19 | 0/9 | [talk-boss01.md](talk-boss01.md) | Solo marcadores (仮). |
| Boss02 | 13/19 | 6/9 | [talk-boss02.md](talk-boss02.md) | Medusa. Se marca en femenino: *The more people look at them, the more beautiful women become.* (camp#1). Risa *\*chuckle\** / *Hehehe*. |
| Boss03 | 0/19 | 0/9 | [talk-boss03.md](talk-boss03.md) | Solo marcadores (仮). |
| Boss04 | 0/19 | 0/9 | [talk-boss04.md](talk-boss04.md) | Solo marcadores (仮). |
| Boss05 | 13/19 | 6/9 | [talk-boss05.md](talk-boss05.md) | Sukuna-Hikona. Aquí usa *thee/thou/thy* (#6, #12-15), que la ficha no registra (E-31: solemne, siempre tú). Los de camp no lo usan. |
| Boss06 | 0/19 | 0/9 | [talk-boss06.md](talk-boss06.md) | Solo marcadores (仮). |
| Boss07 | 0/19 | 0/9 | [talk-boss07.md](talk-boss07.md) | Solo marcadores (仮). |
| Boss08 | 13/19 | 6/9 | [talk-boss08.md](talk-boss08.md) | Adramelech y *Lucifer's Minions* (mismo tono). Ninguna línea marca el género de quien habla. |
| Boss09 | 0/19 | 0/9 | [talk-boss09.md](talk-boss09.md) | Solo marcadores (仮). |
| Boss10 | 0/19 | 0/9 | [talk-boss10.md](talk-boss10.md) | Solo marcadores (仮). |
| Boss11 | 13/19 | 6/9 | [talk-boss11.md](talk-boss11.md) | Odin. *thee/thou* (#12, #13, #15, #16; camp#8), más arcaico que en la negociación (E-31). |
| Boss12 | 0/19 | 0/9 | [talk-boss12.md](talk-boss12.md) | Solo marcadores (仮). |
| Boss13 | 0/19 | 0/9 | [talk-boss13.md](talk-boss13.md) | Solo marcadores (仮). |
| Boss14 | 0/19 | 0/9 | [talk-boss14.md](talk-boss14.md) | Solo marcadores (仮). |
| Boss15 | 13/19 | 6/9 | [talk-boss15.md](talk-boss15.md) | Lucifer. *thee/thou/thine* (#4-6, #12-16), más arcaico que en la negociación (E-31). Llama al jugador *my neighbor* (#13, #17). |
| Boss16 | 13/19 | 6/9 | [talk-boss16.md](talk-boss16.md) | Tenkai. camp#8 tiene el inglés roto (*Ihope you find it Ithought oyu might find use for this...*): errata del original, se traduce el sentido. |
| Boss17 | 0/19 | 0/9 | [talk-boss17.md](talk-boss17.md) | Solo marcadores (仮). |
| Boss18 | 0/19 | 0/9 | [talk-boss18.md](talk-boss18.md) | Solo marcadores (仮). |
| Boss19 | 0/19 | 0/9 | [talk-boss19.md](talk-boss19.md) | Solo marcadores (仮). |
| Boss20 | 0/19 | 0/9 | [talk-boss20.md](talk-boss20.md) | Solo marcadores (仮). |
| Boss21 | 0/19 | 0/9 | [talk-boss21.md](talk-boss21.md) | Solo marcadores (仮). |
| Boss22 | 13/19 | 9/9 | [talk-boss22.md](talk-boss22.md) | Maitreya. camp#0-8 repiten la misma línea. |
| Boss23 | 0/19 | 0/9 | [talk-boss23.md](talk-boss23.md) | Solo marcadores (仮). |
| Boss24 | 13/19 | 6/9 | [talk-boss24.md](talk-boss24.md) | Krishna. |
| Boss25 | 0/19 | 0/9 | [talk-boss25.md](talk-boss25.md) | Solo marcadores (仮). |
| Boss26 | 0/19 | 0/9 | [talk-boss26.md](talk-boss26.md) | Solo marcadores (仮). |
| Boss27 | 0/19 | 0/9 | [talk-boss27.md](talk-boss27.md) | Solo marcadores (仮). |
| Boss28 | 0/19 | 0/9 | [talk-boss28.md](talk-boss28.md) | Solo marcadores (仮). |
| Boss29 | 0/19 | 0/9 | [talk-boss29.md](talk-boss29.md) | Solo marcadores (仮). |
| Boss30 | 13/19 | 6/9 | [talk-boss30.md](talk-boss30.md) | Merkabah. |
| Boss31 | 0/19 | 0/9 | [talk-boss31.md](talk-boss31.md) | Solo marcadores (仮). |
| Boss32 | 0/19 | 0/9 | [talk-boss32.md](talk-boss32.md) | Solo marcadores (仮). |
| Boss33 | 0/19 | 0/9 | [talk-boss33.md](talk-boss33.md) | Solo marcadores (仮). |
| Boss34 | 0/19 | 0/9 | [talk-boss34.md](talk-boss34.md) | Solo marcadores (仮). |
| Boss35 | 0/19 | 0/9 | [talk-boss35.md](talk-boss35.md) | Solo marcadores (仮). |
| Boss36 | 0/19 | 0/9 | [talk-boss36.md](talk-boss36.md) | Solo marcadores (仮). |
| Boss37 | 0/19 | 0/9 | [talk-boss37.md](talk-boss37.md) | Solo marcadores (仮). |
| Boss38 | 13/19 | 6/9 | [talk-boss38.md](talk-boss38.md) | Inanna. Se marca en femenino: *Rest at the feet of your mother.* (#17), *I am the Mother of All* (camp#1-2). Al jugador lo llama *adorable child* (#14). |
| Boss39 | 13/19 | 6/9 | [talk-boss39.md](talk-boss39.md) | Mitra-Buddha. |
| Boss40 | 0/19 | 0/9 | [talk-boss40.md](talk-boss40.md) | Solo marcadores (仮). |
| Boss41 | 0/19 | 0/9 | [talk-boss41.md](talk-boss41.md) | Solo marcadores (仮). |
| Boss42 | 13/19 | 5/9 | [talk-boss42.md](talk-boss42.md) | Metatron y *Metatron Army*. Todo en MAYÚSCULAS (E-56); *'TIS* (#12). |
| Boss43 | 13/19 | 6/9 | [talk-boss43.md](talk-boss43.md) | Satan. |
| Boss44 | 0/19 | 0/9 | [talk-boss44.md](talk-boss44.md) | Solo marcadores (仮). |
| Boss45 | 0/19 | 0/9 | [talk-boss45.md](talk-boss45.md) | Solo marcadores (仮). |
| Boss46 | 0/19 | 0/9 | [talk-boss46.md](talk-boss46.md) | Solo marcadores (仮). |
| Boss47 | 0/19 | 0/9 | [talk-boss47.md](talk-boss47.md) | Solo marcadores (仮). |
| Boss48 | 0/19 | 0/9 | [talk-boss48.md](talk-boss48.md) | Solo marcadores (仮). |
| Boss49 | 0/19 | 0/9 | [talk-boss49.md](talk-boss49.md) | Solo marcadores (仮). |
| Boss50 | 0/19 | 0/9 | [talk-boss50.md](talk-boss50.md) | Solo marcadores (仮). |
| Boss51 | 0/19 | 0/9 | [talk-boss51.md](talk-boss51.md) | Solo marcadores (仮). |
| Boss52 | 0/19 | 0/9 | [talk-boss52.md](talk-boss52.md) | Solo marcadores (仮). |
| Boss53 | 0/19 | 0/9 | [talk-boss53.md](talk-boss53.md) | Solo marcadores (仮). |
| Boss54 | 0/19 | 0/9 | [talk-boss54.md](talk-boss54.md) | Solo marcadores (仮). |
| Boss55 | 0/19 | 0/9 | [talk-boss55.md](talk-boss55.md) | Solo marcadores (仮). |
| Boss56 | 0/19 | 0/9 | [talk-boss56.md](talk-boss56.md) | Solo marcadores (仮). |
| Boss57 | 0/19 | 0/9 | [talk-boss57.md](talk-boss57.md) | Solo marcadores (仮). |
| Boss58 | 0/19 | 0/9 | [talk-boss58.md](talk-boss58.md) | Solo marcadores (仮). |
| Boss59 | 0/19 | 0/9 | [talk-boss59.md](talk-boss59.md) | Solo marcadores (仮). |
| Boss60 | 0/19 | 0/9 | [talk-boss60.md](talk-boss60.md) | Solo marcadores (仮). |
| Boss61 | 0/19 | 0/9 | [talk-boss61.md](talk-boss61.md) | Solo marcadores (仮). |
| Boss62 | 0/19 | 0/9 | [talk-boss62.md](talk-boss62.md) | Solo marcadores (仮). |
| Boss63 | 0/19 | 0/9 | [talk-boss63.md](talk-boss63.md) | Solo marcadores (仮). |
| Boss64 | 13/19 | 0/9 | [talk-boss64.md](talk-boss64.md) | Izanami. Al jugador lo marca en masculino: *What a... wonderful man.* (#17); lo llama *Sweet child* (#1). |
| Boss65 | 0/19 | 0/9 | [talk-boss65.md](talk-boss65.md) | Solo marcadores (仮). |
| Boss66 | 0/19 | 0/9 | [talk-boss66.md](talk-boss66.md) | Solo marcadores (仮). |
| Boss67 | 0/19 | 0/9 | [talk-boss67.md](talk-boss67.md) | Solo marcadores (仮). |
| Boss68 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss69 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss70 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss71 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss72 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss73 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boss74 | 0/19 | 0/9 | [talk-boss68-74.md](talk-boss68-74.md) | Solo marcadores (仮). |
| Boy | 18/19 | 9/9 | [personalidad-boy.md](personalidad-boy.md) |  |
| DlcDummy | — | 0/9 | ninguna (no hace falta) | Solo en camp: las 9 líneas dicen *???*. No habla nadie. |
| Gal | 18/19 | 9/9 | [personalidad-gal.md](personalidad-gal.md) | *raise hell* (#10): igualar la intensidad (E-22). |
| Gentle | 18/19 | 9/9 | [personalidad-gentle.md](personalidad-gentle.md) |  |
| Girl | 18/19 | 9/9 | [personalidad-girl.md](personalidad-girl.md) | Marca a quien habla en femenino: *I fused with a lot of demons and became a bad girl.* (camp#3), igual que en la negociación (ver la ficha y PENDING, «Quién usa la voz Girl»). Al jugador lo marca en masculino: *Were you waiting like a good boy?* (camp#7). Lo llama *Mister* (#1, #8, #15). |
| Heehaw | 18/19 | 9/9 | [personalidad-heehaw.md](personalidad-heehaw.md) | Al jugador lo marca en masculino: *If you're a good boy* (#12). |
| Human03 | 13/19 | 6/9 | [talk-human03.md](talk-human03.md) | Habla de *this country* y de los *Samurai* (#15, #17; camp#1-2): la plantilla no encaja del todo con quien usa el tono, que sigue sin identificar. camp#3-5 están vacías. |
| Human04 | 13/19 | 6/9 | [talk-human04.md](talk-human04.md) | Se llama *this steel shadow* (#17), como en la ficha (*a shadow*). Habla de los *Samurai* (camp#1-2). *the Samurai from his predicament* (camp#1) marca en masculino a un tercero. camp#3-5 están vacías. |
| Human05 | 0/19 | 0/9 | ninguna (no hace falta) | Solo marcadores (仮). El tono no lo usa nadie (NKMBaseTable) y battle/talk/TalkToneHuman05 dice *NOT USED*. |
| HumanFemale | 0/19 | 0/9 | [talk-human-female.md](talk-human-female.md) | Solo marcadores (仮). |
| HumanMale | 0/19 | 0/9 | [talk-human-male.md](talk-human-male.md) | Solo marcadores (仮). |
| Ijin | 18/19 | 9/9 | [personalidad-ijin.md](personalidad-ijin.md) | *thee/thou* como en la ficha (#0, #2, #3, #13-17). Al jugador lo marca en masculino: *What a man of low caliber.* (#6). |
| Info | 18/19 | 9/9 | [personalidad-info.md](personalidad-info.md) |  |
| Lady | 18/19 | 9/9 | [personalidad-lady.md](personalidad-lady.md) |  |
| MajinBlack | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinDavid | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinMat | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinMother | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinPale | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinRed | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinShadow | 13/19 | 6/9 | [talk-majin.md](talk-majin.md) | Tono sin dueño (ver la ficha). |
| MajinTrum | 13/19 | 9/9 | [talk-majin.md](talk-majin.md) |  |
| MajinWhite | 13/19 | 8/9 | [talk-majin.md](talk-majin.md) |  |
| Nakigoe | 18/19 | 9/9 | [personalidad-nakigoe.md](personalidad-nakigoe.md) |  |
| Oldman | 18/19 | 9/9 | [personalidad-old-man.md](personalidad-old-man.md) | *young'un* (#6). |
| Oldwoman | 18/19 | 9/9 | [personalidad-old-woman.md](personalidad-old-woman.md) |  |
| Partner01 | 4/19 | — | [asahi.md](asahi.md) | Por el tono 113 (NKMBaseTable: Asahi) y el texto (*Maybe I can help everyone more, now?*, #0). |
| Partner02 | 4/19 | — | [navarre.md](navarre.md) | Por el tono 114 (Navarre) y el texto (*I'm Super Navarre now!*, #22). |
| Partner03 | 4/19 | — | [nozomi.md](nozomi.md) | Por el tono 115 (Nozomi) y el texto (#0, #22). |
| Partner04 | 4/19 | — | [gaston.md](gaston.md) | Por el tono 116 (Gaston) y el texto (*I will continue to be number one for the people!*, #22). |
| Partner05 | 4/19 | — | [hallelujah.md](hallelujah.md) | Por el tono 117 (Hallelujah). #22 es idéntica a la de Partner07. |
| Partner06 | 4/19 | — | [toki.md](toki.md) | Por el tono 118 (Toki) y el texto (*I must devote myself more.*, #0). |
| Partner07 | 4/19 | — | [hallelujah.md](hallelujah.md) | Por el tono 119 (Hallelujah, otro ID). #22 igual a Partner05: traducirlas igual. |
| Partner08 | 3/19 | — | [isabeau.md](isabeau.md) | Por el tono 120 (Isabeau) y el registro (*sedulous training*, #0). Sin #22. |
| Partner09 | 0/19 | — | ninguna (no hace falta) | Todo *Dummy* o *ダミー*: nada que traducir. Tono 121 = Flynn. |
| Shiki01 | 13/19 | 9/9 | [talk-shiki01.md](talk-shiki01.md) | Alice. *Mister* (#15; camp#0-2) y la frase fija *Will you die for me?* (#17), que la ficha pide repetir igual. |
| Shiki02 | 0/19 | 0/9 | [talk-shiki02.md](talk-shiki02.md) | Solo marcadores (仮). |
| Shiki03 | 13/19 | 9/9 | [talk-shiki03.md](talk-shiki03.md) | Habla cortada con puntos suspensivos, como la ficha. |
| Shiki04 | 0/19 | 0/9 | [talk-shiki04.md](talk-shiki04.md) | Solo marcadores (仮). |
| Shiki05 | 17/19 | 9/9 | [talk-shiki05.md](talk-shiki05.md) | *Dammit* (#0-3, #9): igualar la intensidad (E-22). |
| Shiki06 | 13/19 | 9/9 | [talk-shiki06.md](talk-shiki06.md) | *patriot*, *comrade* (#12-14). |
| Shiki07 | 0/19 | 0/9 | ninguna (no hace falta) | Solo marcadores (仮). El tono no lo usa nadie y no tiene ficha; no hace falta mientras no haya texto. |
| Shiki08 | 13/19 | 6/9 | [talk-shiki08-09.md](talk-shiki08-09.md) | Mismo texto que Shiki09 con *order* en vez de *chaos*. *thee* (camp#8). Habla de *Samurai* (camp#1). |
| Shiki09 | 13/19 | 6/9 | [talk-shiki08-09.md](talk-shiki08-09.md) | Ver Shiki08. *thee* (camp#8). |
| Shiki10 | 13/19 | 6/9 | [talk-shiki10.md](talk-shiki10.md) | Se llama *a Fiend* (#12, #15). Al jugador lo llama *samurai* (#14, #17): la plantilla parece escrita para otro protagonista; se traduce lo que dice. |
| SkullMan | 0/19 | — | ninguna (no hace falta) | Todo *Dummy*; el tono no aparece en la tabla del ejecutable. |
| SkullWoman | 0/19 | — | ninguna (no hace falta) | Todo *Dummy*; el tono no aparece en la tabla del ejecutable. |
| Unarigoe | 18/19 | 9/9 | [personalidad-unarigoe.md](personalidad-unarigoe.md) |  |
| Unknown | 18/19 | 9/9 | [personalidad-unknown.md](personalidad-unknown.md) |  |
| Young | 18/19 | 9/9 | [personalidad-young.md](personalidad-young.md) | Groserías: *You bastard!* (#6), *My ass totally froze over there.* (camp#8). |

## battle/PartnerAttack.mbm

Frases de los ataques en equipo de los compañeros (294 textos, #1-295; no hay #258). No tienen etiqueta: la atribución es por contenido y las fichas de los compañeros ya la recogen.

| Tramo | Quién habla | Ficha | Cómo se sabe |
|---|---|---|---|
| #1-51 | Asahi | [asahi.md](asahi.md) | *I'm ready, Nanashi!* (#1), *This is what a Hunter can do!* (#41); ya en la ficha. |
| #52-80 | Navarre | [navarre.md](navarre.md) | *Hehehe... It's Navarre time!* (#55); ya en la ficha. |
| #81-111 | Nozomi | [nozomi.md](nozomi.md) | *For the fairies!* (#82), *Never understimate a queen.* (#94); ya en la ficha. |
| #112-158 | Hallelujah | [hallelujah.md](hallelujah.md) | *Hey! Chiro, keep it down!* (#113), *Let's do it, Leader!* (#147); ya en la ficha. |
| #159-175 | **sin confirmar** | probablemente [gaston.md](gaston.md) | *I shall show you the pride of a Samurai!* (#166) y *I shall show you the power of the goddess!* (#167) repiten las ideas de #211 y #214, del tramo de Gaston; *God has chosen me...* (#161) va con *the chosen people* (#207). Pero *Hurry up and let me have my time in the sun!* (#162) suena a Navarre (#53). La ficha de Gaston no lo usó. |
| #176-215 | Gaston | [gaston.md](gaston.md) | *Hmph... You soiled my spear.* (#206); ya en la ficha. |
| #216-257 | Toki | [toki.md](toki.md) | *Om vajra ratna om trah svaha...* (#238), *Don't touch my Master!* (#242); ya en la ficha. |
| #259-265 | **sin confirmar** | — | Alguien leal a Flynn que trata al jugador por su nombre: *For Flynn!* (#260), *I do this for you, {nombre}!* (#264). |
| #266-272 | **probablemente Flynn** | [flynn.md](flynn.md) | *Are you ready, Burroughs?* (#269, #272): solo Flynn le habla a Burroughs en el juego. La ficha de Flynn lo deja sin confirmar. |
| #273-287 | **probablemente Isabeau** | [isabeau.md](isabeau.md) | Voz cortés de Samurai que marca su género como mujer frente a los hombres: *Men are so careless.* (#283), *It's the Samurai's turn!* (#284), *Pardon me!* (#277). La ficha de Isabeau no las usó. |
| #288-293 | **sin identificar** | — | *Leave it to me, Master!* (#289), *Glory be to the Master!* (#290), *This is the power of a Godslayer...* (#291), *I won't let you hurt my friend!* (#293). Por *Master* podría ser Toki, pero su tramo termina en #257. Falta ficha si no es de nadie con ficha. |
| #294-295 | **sin identificar** | — | *Don't you have any more?*, *Is that it?*, con un código de voz `{F81B}` delante. Nada indica quién. |

Los compañeros invitados (tonos 120-126 de NKMBaseTable: Isabeau, Flynn y dos más sin ficha) son los candidatos para #259-295. Si el usuario puede probarlo en el juego, se confirma de una vez.

## battle/Legion/LegionMsg.mbm

Voces de las legiones (grupos de demonios). Cada bloque de cuatro textos (#N0 encuentro, #N1 conversación, #N2 pelea, #N3 daño) trae cinco frases cortas separadas por salto de línea; las dicen demonios distintos del grupo. La legión de cada bloque sale de battle/Legion/LegionMsgTable.tbb (ID de demonio → primer mensaje) y el nombre, de battle/NKMSortIndex.tbb.

- **Género:** no se marca (E-41): son grupos de demonios distintos. Al jugador sí lo marcan en masculino: *He's teasing us.* (#43), *I'll have his arm.* (#140), *Is he mine?* (#430).
- **Trato:** propuesta, pendiente de aprobación (E-30): **tú** con el jugador (*Human?*, *My turn, sonny.*, #20; *A child like you...*, #223; *Insolent brat!*, #243). Si una frase se dirige a todo el grupo del jugador, **ustedes** (E-11); las ambiguas (*You wanna go?*, #20; *Come at us!*, #273) quedan a criterio de quien traduce. Hablan de sí mismos en plural: *We are Tengu!* (#100), *Our hearts are one* (#181), *You oppose us?* (#63).
- **Registro:** una frase de cada voz: casual, de época, en MAYÚSCULAS de bestia, con *ho* de los Frost... Cada frase se traduce con la ficha de su estilo (abajo), no con una voz común.
- **Groserías:** *The hell?* (#53), *Damn you, human.* (#243), *Damn you.* (#452); igualar la intensidad (E-22).
- **Sin texto:** #0-3 (*(provisional)*), #11-13, #191-193, #201-203 vacías; #301-383, #440-443, #460-463, #480-483, #491-492 y varias #N3 dicen *(provisional) ...*: son marcadores.

| Mensajes | Legión (NKMSortIndex) | Fichas que orientan el estilo |
|---|---|---|
| #10 | Lucifer's Minions | (solo encuentro) amenazas casuales |
| #20-23 | Innocent Horde | [personalidad-old-man.md](personalidad-old-man.md) (*sonny*, *Young'un*) y casual |
| #30-33 | Oni Horde | casual |
| #40-43 | Pirate Horde | casual |
| #50-53 | Dragon Horde | casual y [personalidad-beast.md](personalidad-beast.md) (*ME EAT YOU!*, *YOU LOOK TASTY!*) |
| #60-63 | Dead Horde | solemne y casual |
| #70-73 | Jack Union | [personalidad-heehaw.md](personalidad-heehaw.md) (*ho*, *Hee-ho-ho!*) |
| #80-83 | Blizzard Horde | [personalidad-beast.md](personalidad-beast.md) (*ME TAKE NIBBLE*) y [personalidad-lady.md](personalidad-lady.md) (*You lack elegance.*) |
| #90-93 | Inferno Horde | gemidos y gruñidos (*Braaaains...*, *Gyegyuh!*) |
| #100-103 | Tengu Horde | de época (*Nay!*, *Training this is.*, E-31) |
| #110-113 | Demon Horde | casual |
| #120-123 | Frosts | [personalidad-heehaw.md](personalidad-heehaw.md) (*King ho!*) |
| #130-133 | Azteca Force | solemne (*Offer your life to my kingdom.*) |
| #140-143 | Jaki Horde | casual y glotón (*I'll eat your foot.*, *Is there a woman?*) |
| #150-153 | Fallen Horde | solemne y burlón (*You brat...*) |
| #160-163 | Greek Force | solemne y casual |
| #170-173 | Wildfire Horde | [personalidad-beast.md](personalidad-beast.md) (todo en mayúsculas) |
| #180-183, #190, #200 | Angel Army (tres IDs) | solemne y religioso (*Praise the Lord*, *Let there be light*); ver *Angel* en [generic-speakers.md](generic-speakers.md) |
| #210-213 | Defiant Horde | solemne |
| #220-223 | Demon Army | solemne de mando (*I am in command.*) |
| #230-233 | Freezing Horde | solemne y coqueto (*On my chest?*, *No charm...*) |
| #240-243 | Gale Horde | solemne |
| #250-253 | Thunder Horde | mezcla, con mayúsculas de bestia (*ME THROW DOWN!*) |
| #260-263 | Blazing Horde | solemne con gritos |
| #270-273 | Indian Force | solemne y casual |
| #280-283 | Norse Force | solemne, con *SWALLOW YOU.* |
| #290-293 | *Not Used* (ID 702) | mezcla con [personalidad-beast.md](personalidad-beast.md) (*ME EAT HEART!*); la tabla dice que no se usa |
| #300 | (sin ID en la tabla) | casual furioso (*You traitor!*, *You human enemy.*) |
| #390-392 | Itsumade Horde | el pájaro *Itsumade* («¿hasta cuándo?»): *How long?*, *Cacaw?*; frase delicada (E-23) |
| #400-402 | Strix Horde | coqueto y cruel (*Entertain me with your body.*) |
| #410-412 | Demonstrators | humanos alterados, voces quebradas (*yOuR HoNoR...*) |
| #420-422 | Obsessed Horde | pandilla callejera (*Get off our turf.*) |
| #430-432 | Greedy Horde | casual y posesivo (*Is he mine?*, *My child...*) |
| #450-452 | Zaccoum Horde | infantil y repetitivo (*Hey hey hey!*, *Talk, talk!*) |
| #470-472 | Yomi Army | devoto de *Master* (*All is for Master.*) |
| #490, #493 | Metatron Army | máquina militar (*Target sighted. Eliminating enemy.*); ver [talk-boss42.md](talk-boss42.md) |
| #500-503 | Angel Army (ID 717) | solemne (*Judgment...*, *Repent.*) |
| #510-513 | Itsumade Horde (ID 951) | casual y risueño |

## Fuente

- battle/DevilMsg/dMsg_*.mbm (124 archivos) y camp/CecDevilMsg/dMsg_*.mbm (114): leídas completas las líneas con inglés de Boss02, 05, 08, 11, 15, 16, 22, 24, 30, 38, 39, 42, 43, 64, Shiki01-10, Human03-05 y Partner01-09, con las de camp. Las de las personalidades (Beast...Young) y los Fiends (Majin) solo se rastrearon por palabras de género, trato, groserías y arcaísmos (*man*, *boy*, *girl*, *mister*, *he/she*, *thee/thou*, *damn*, *hell*, *ass*, *bastard*...), más Beast completo; conviene una lectura completa al traducirlas. Los marcadores solo se contaron.
- battle/PartnerAttack.mbm#1-295 completo; battle/Legion/LegionMsg.mbm completo, con battle/Legion/LegionMsgTable.tbb.
- Tonos: exefs/code.bin (tabla de nombres) y battle/NKMBaseTable.tbb (byte 56).
