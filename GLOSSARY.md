# Glosario

Términos fijos de la traducción. La guía de estilo está en [STYLE.md](STYLE.md).

## Reglas

- **G-1** Los términos que IVA comparte con *SMT V: Vengeance* (demonios, habilidades, razas, estados, objetos, y los términos de sistema y de menú, como *Demon Compendium* o *Save Data*) llevan el de la traducción oficial de SMT V al español. Se toma solo el término; el registro es siempre el de esta traducción: español neutro, natural y nunca literal (E-10). [PLAN]
- **G-2** Lo propio de IV e IVA se decide aquí. Hasta que esté decidido, el término va a [PENDING.md](PENDING.md) con una propuesta. [PLAN]
- **G-3** Un término de esta tabla se usa igual en todo el juego. `tools/check.py` avisa cuando el inglés lo tiene y el español no (`glosario`). [Encargo §6]

## Cómo se arma

1. `tools/smt5v.py candidates` empareja los nombres de SMT V en inglés y en español y busca cada uno en IVA. El resultado queda fuera del repo (`../smt4a-local/glossary-candidates.tsv`), porque es texto de otro juego.
   Antes de cada sección, `tools/smt5v.py terms --section SECCIÓN` saca sus términos de sistema (lo que IVA escribe con mayúscula y las etiquetas de los menús de SMT V que IVA usa), con el español de SMT V si lo tiene (`../smt4a-local/system-terms.tsv`).
2. El terminólogo revisa los candidatos y propone las filas: *oficial* si es el mismo término en los dos juegos, o *por decidir* si el término inglés significa otra cosa en IVA.
3. Las filas *oficial* entran a la tabla. Las *por decidir* van a [PENDING.md](PENDING.md) para que las decida el usuario.

## Términos

Por sección. *Oficial* (SMT V, G-1) o *decidido* por el usuario (G-2), con fecha. *Provisional* es decidido, pero se comprueba en el juego. En el texto, los términos de sistema van en minúscula a media frase (E-59); la mayúscula de la tabla es la de los menús. Lo que falta decidir está en [PENDING.md](PENDING.md).

### Interfaz

#### Nombres de quien habla (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Suspicious man | Hombre sospechoso | SMT V (personaje: *Suspicious Man*) | Etiqueta de quien habla (unite/unite.mbm#79-80). SMT V la escribe con *Man* en mayúscula. |

#### Decididos por el usuario: nombres de quien habla

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Mido | Mido | Decidido 2026-11-08 (G-2) | Nombre propio; se deja igual. |
| Napaea | Napaea | Decidido 2026-11-08 (G-2) | Nombre propio; se deja igual. |
| Saint Germain | Saint Germain | Decidido 2026-11-08 (G-2) | Nombre propio; se deja igual. Las tablas del contenido descargable lo escriben *St. Germain*: se decide al llegar a ellas. |
| System voice | Voz del sistema | Decidido 2026-11-08 (G-2) | La voz automática de las terminales. |
| Hooded man | Hombre encapuchado | Decidido 2026-11-08 (G-2) | Como *Hombre sospechoso*. |
| Spirit of the Spring | Espíritu del Manantial | Decidido 2026-11-08 (G-2) | El ser de la fuente que cura al grupo. |
| Shopkeeper | Dependiente | Decidido 2026-11-08 (G-2) | No marca género, que sigue pendiente en la ficha. |
| Charon | Caronte | Decidido 2026-11-08 (G-2) | El barquero de la mitología griega. |

La etiqueta *System* (unite/unite.mbm#111) va como «Sistema». No está en la tabla porque *System* también va en *System Settings* y el validador avisaría de más.

#### Términos de sistema (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Cancel | Cancelar | SMT V (etiqueta) | Opción de menú. |
| Yes | Sí | SMT V (etiqueta) | Opción de menú. |
| Save | Guardar | SMT V (etiqueta) | Opción y verbo de guardar la partida. |
| Load | Cargar | SMT V (etiqueta) | Cargar una partida. |
| Save Data | Datos de guardado | SMT V (etiqueta) | IVA lo escribe casi siempre *save data* o *Save data*. En frases, SMT V también usa *datos guardados* (ver el informe). |
| Clear Data | Partida terminada | SMT V (etiqueta; ejemplo: *Saving Clear Data* ⇒ *Guardando partida terminada*) | Los datos de una partida completada. IVA lo escribe en minúscula (*clear data*). |
| New Game Plus | Nueva partida + | SMT V (ejemplo: *start a new game plus* ⇒ *empezar una Nueva partida +*) | Modo de juego. |
| Menu | Menú | SMT V (etiqueta) | *Title Menu* y *title screen*: menú de título y pantalla de título (SMT V). |
| Difficulty | Dificultad | SMT V (etiqueta) | Opción del menú de sistema. |
| Add-On Content | Complemento | SMT V (etiqueta) | Contenido descargable (addon/aoc_msg.mbm#3). |
| Button | Botón | SMT V (etiqueta) | *A Button* → botón A. |
| Talk | Hablar | SMT V (etiqueta) | Opción del menú de la fusión (unite/unite.mbm#83, #92). |
| Buy | Comprar | SMT V (etiqueta) | Opción de tienda. |
| UNKNOWN | DESCONOCIDO | SMT V (etiqueta) | Etiqueta de lista en mayúsculas. |
| Macca | Macca | SMT V (etiqueta) | Moneda. SMT V la escribe en minúscula a media frase (*macca*, E-59). |
| Summon | Invocar | SMT V (etiqueta) | Invocar un demonio. |
| Party | Grupo | SMT V (etiqueta) | Los que combaten junto al jugador. |
| Stock | Hueste | SMT V (etiqueta: *Huestes*; ejemplo: *returning to the stock* ⇒ *regresar a tu hueste*) | Los demonios que lleva el jugador. IVA lo escribe en minúscula. |
| Skills | Habilidades | SMT V (etiqueta) | En singular, *skill* → habilidad. |
| skill slots | espacios de habilidades | SMT V (ejemplo: *The skill slots are full* ⇒ *Espacios de habilidades llenos*) | Agregado. |
| Stats | Estadísticas | SMT V (etiqueta) | IVA lo escribe sobre todo en minúscula. |
| Strength | Fuerza | SMT V (etiqueta) | Estadística. |
| Magic | Magia | SMT V (etiqueta) | Estadística y tipo de habilidad. |
| Agility | Agilidad | SMT V (etiqueta) | Estadística. |
| Luck | Suerte | SMT V (etiqueta) | Estadística. |
| HP | PS | SMT V (ejemplo: *MAX HP* ⇒ *PS MÁX.*) | Puntos de salud. |
| MP | PM | SMT V (ejemplo: *MAX MP* ⇒ *PM MÁX.*) | Puntos de magia. |
| Healing | Curativa | SMT V (etiqueta; ejemplo: *: Healing* ⇒ *: Curativa*) | Tipo de habilidad (*healing skills* → habilidades curativas). |
| Support | Apoyo | SMT V (etiqueta; ejemplo: *: Support* ⇒ *: Apoyo*) | Tipo de habilidad. |
| Phys | Físico | SMT V (*Physical* ⇒ *Físico*; ejemplo: *Repel Phys* ⇒ *Repeler físico*) | Elemento de ataque. Concuerda con el sustantivo (*habilidades físicas*). |
| Fire | Fuego | SMT V (tabla de elementos) | Elemento. Agregado (unite/unite.mbm#48). |
| Ice | Hielo | SMT V (etiqueta) | Elemento. |
| Elec | Electricidad | SMT V (*Electric* ⇒ *Electricidad*; ejemplo: *Elec Potential* ⇒ *Potencial eléctrico*) | Elemento. Como adjetivo, *eléctrico* (SMT V). |
| Almighty | Todopoderoso | SMT V (etiqueta) | Elemento. Concuerda con el sustantivo. |
| Resist | Resistir | SMT V (ejemplo: *: Resist* ⇒ *: Resistir*) | Afinidad. Agregado (unite/unite.mbm#48). |
| Null | Anular | SMT V (ejemplo: *: Null* ⇒ *: Anular*) | Afinidad. |
| Repel | Repeler | SMT V (ejemplo: *: Repel* ⇒ *: Repeler*) | Afinidad. |
| Drain | Absorber | SMT V (ejemplo: *: Drain* ⇒ *: Absorber*) | Afinidad. Agregado (unite/unite.mbm#48). |
| Affinities | Afinidades | SMT V (etiqueta) | IVA lo escribe en minúscula. |
| Status Ailments | Estados alterados | SMT V (etiqueta) | IVA lo escribe en minúscula. |
| Ailment | Estado alterado | SMT V (ejemplo: *: Status ailment* ⇒ *: Estado alterado*) | La etiqueta corta de SMT V es *Estado*; aquí se usa la forma larga para no confundirla con *Status*. |
| Press Turn Icon | Icono de acción | SMT V (ejemplo: *Press Turn Icon count restored!* ⇒ *¡Se han restablecido los iconos de acción!*) | Sistema de combate. |
| Press Turn Icons | Iconos de acción | SMT V (ejemplo) | Sistema de combate. |
| Auto-Battle | Combate automático | SMT V (ejemplo: *Activate Auto-Battle?* ⇒ *¿Activar el combate automático?*) | Agregado (battle/Common/common.mbm#6). |
| Fusion | Fusión | SMT V (ejemplos: *Fusion Level* ⇒ *Nivel de fusión*; *Fusion Accidents* ⇒ *Accidentes de fusión*) | Agregado: opción de menú (*select Fusion*) y sustantivo en minúscula (84 líneas de la sección). |
| Fuse | Fusionar | SMT V (etiqueta) | Verbo; IVA lo escribe sobre todo en minúscula. |
| Demon Fusion | Fusión de demonios | SMT V (etiqueta) | |
| Special Fusion | Fusión especial | SMT V (etiqueta) | Plural *Special Fusions* → fusiones especiales. IVA lo escribe también en minúscula. |
| Skill Inheritance | Herencia de habilidades | SMT V (etiqueta) | IVA lo escribe en minúscula (*skill inheritance*). |
| Fusion Accidents | Accidentes de fusión | SMT V (etiqueta) | IVA lo escribe en minúscula. |
| Compendium | Compendio | SMT V (ejemplo: *View Compendium* ⇒ *Ver el compendio*) | El compendio de demonios. Minúscula a media frase (E-59). |
| Demon Compendium | Compendio de demonios | SMT V (etiqueta) | |
| register | registrar | SMT V (ejemplo: *Register to Compendium* ⇒ *Registrar en el compendio*) | Agregado: registrar un demonio en el compendio. |
| race | raza | SMT V (ejemplo: *Sort by race* ⇒ *Ordena por raza*) | Agregado: la raza de un demonio. |
| Elements | Elementales | SMT V (raza *Element* ⇒ *Elemental*; ejemplo: *Fusion Using Elements* ⇒ *Fusión mediante Elementales*) | Los demonios de la raza Element. En minúscula (*elements*) son los elementos de ataque (fuego, hielo). Ver el informe: SMT V tiene también *Fusion using elements* ⇒ *Fusión mediante elementos*. |
| Relics | Reliquias | SMT V (etiqueta) | Objetos que se venden en las tiendas. |
| quest | misión | SMT V (ejemplo: *Main Quests* ⇒ *Misiones principales*) | Agregado (unite/unite.mbm#107-111, camp/config.mbm#2). |

#### Decididos por el usuario: términos de sistema

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Cathedral of Shadows | Catedral de las Sombras | Decidido 2026-11-08 (G-2) | La app de fusión. |
| Terminal | Terminal | Decidido 2026-11-08 (G-2) | En femenino: *la Terminal*, *las Terminales*. Son los puntos de viaje. En *your smartphone acts as a terminal* es palabra común. |
| Ueno Terminal | Terminal de Ueno | Decidido 2026-11-08 (G-2) | Y así: Kasumigaseki, Shinjuku, Ikebukuro, Shibuya, Ginza, Yoyogi, Toyosu, Tennozu. |
| Kasumigaseki Terminal | Terminal de Kasumigaseki | Decidido 2026-11-08 (G-2) | |
| Shinjuku Terminal | Terminal de Shinjuku | Decidido 2026-11-08 (G-2) | |
| Ikebukuro Terminal | Terminal de Ikebukuro | Decidido 2026-11-08 (G-2) | |
| Shibuya Terminal | Terminal de Shibuya | Decidido 2026-11-08 (G-2) | |
| Ginza Terminal | Terminal de Ginza | Decidido 2026-11-08 (G-2) | |
| Yoyogi Terminal | Terminal de Yoyogi | Decidido 2026-11-08 (G-2) | |
| Toyosu Terminal | Terminal de Toyosu | Decidido 2026-11-08 (G-2) | |
| Tennozu Terminal | Terminal de Tennozu | Decidido 2026-11-08 (G-2) | |
| Mikado Terminal | Terminal de Mikado | Provisional 2026-11-08 (G-2) | Se revisa con los nombres de lugares (Tablas). |
| Sky Terminal | Terminal del Cielo | Provisional 2026-11-08 (G-2) | Se revisa con los nombres de lugares (Tablas). |
| StreetPass | StreetPass | Decidido 2026-11-08 (G-2) | Marca; no se traduce. |
| Nintendo 3DS | Nintendo 3DS | Decidido 2026-11-08 (G-2) | Marca; *la consola Nintendo 3DS*. |
| SD Card | tarjeta SD | Decidido 2026-11-08 (G-2) | También *SD card*. |
| SD card | tarjeta SD | Decidido 2026-11-08 (G-2) | |
| Game Card | tarjeta de juego | Decidido 2026-11-08 (G-2) | |
| System Settings | Configuración de la consola | Provisional 2026-11-08 (G-2) | Menús de la consola: tienen que coincidir con los que muestra la consola en español; se comprueban en el juego. |
| Internet Settings | Configuración de Internet | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| Other Information | Otros ajustes | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| Service User Agreement | Contrato de uso de los servicios de Nintendo 3DS | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| User Agreement | Contrato de uso | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| Parental Controls | Control parental | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| StreetPass Management | Administración de StreetPass | Provisional 2026-11-08 (G-2) | Menú de la consola. |
| Shin Megami Tensei IV: Apocalypse | Shin Megami Tensei IV: Apocalypse | Decidido 2026-11-08 (G-2) | Título; no se traduce. *the Shin Megami Tensei franchise* → «la saga Shin Megami Tensei». |
| Shin Megami Tensei IV | Shin Megami Tensei IV | Decidido 2026-11-08 (G-2) | Título; no se traduce. |
| extra data | datos adicionales | Decidido 2026-11-08 (G-2) | Datos de la consola en la tarjeta SD. También *Extra data*. |
| Extra data | datos adicionales | Decidido 2026-11-08 (G-2) | |
| save data bonus | bonificación por datos guardados | Decidido 2026-11-08 (G-2) | Plural: *bonificaciones por datos guardados*. |
| DDS Card | tarjeta DDS | Decidido 2026-11-08 (G-2) | *DDS* (*Digital Demon Service*) se deja como sigla. |
| DDS | DDS | Decidido 2026-11-08 (G-2) | Sigla; se deja igual. |
| Brane | Brana | Decidido 2026-11-08 (G-2) | *2nd Brane* → «Brana 2»: la fuente no tiene «ª». |
| anomaly | anomalía | Decidido 2026-11-08 (G-2) | |
| Legion Skill | Habilidad de legión | Decidido 2026-11-08 (G-2) | Plural: *Habilidades de legión*. |
| Horde Compendium | Compendio de hordas | Decidido 2026-11-08 (G-2) | |
| Fusion Search | Búsqueda de fusión | Decidido 2026-11-08 (G-2) | Función de la app de fusión. |
| Basic Fusion | Fusión básica | Decidido 2026-11-08 (G-2) | Función de la app de fusión. |
| normal fusion | fusión normal | Decidido 2026-11-08 (G-2) | La fusión que no es especial. |
| Recommended Fusions | Fusiones recomendadas | Decidido 2026-11-08 (G-2) | Función de la app de fusión. |
| component demons | demonios componentes | Decidido 2026-11-08 (G-2) | *components* solo → «componentes». También *Component demons*. |
| Component demons | demonios componentes | Decidido 2026-11-08 (G-2) | |
| resulting demon | demonio resultante | Decidido 2026-11-08 (G-2) | *fusion result* → «resultado de la fusión» (SMT V). |
| fusion limit | límite de fusión | Decidido 2026-11-08 (G-2) | |
| fusion conditions | condiciones de fusión | Decidido 2026-11-08 (G-2) | |
| laws of fusion | leyes de la fusión | Decidido 2026-11-08 (G-2) | |
| Rank | Rango | Decidido 2026-11-08 (G-2) | El puesto de un demonio dentro de su raza. También *rank* → «rango». |
| Compendium Ticket | Vale del compendio | Decidido 2026-11-08 (G-2) | Plural: *Vales del compendio*. |
| Book | Libro | Provisional 2026-11-08 (G-2) | Opción del menú del compendio, con *View* → «Ver» y *Overwrite* → «Sobrescribir». Tiene que coincidir con el menú; se comprueba en el juego. |
| Demon Summoning Program | Programa de invocación de demonios | Decidido 2026-11-08 (G-2) | |
| Demon Analyze | Análisis de demonios | Decidido 2026-11-08 (G-2) | Una app. *demon analysis info* → «datos del análisis de demonios». |
| Demon Fusion Lite | Fusión de demonios Lite | Decidido 2026-11-08 (G-2) | Nombre de una app. |
| Hunter Apps | apps de cazador | Decidido 2026-11-08 (G-2) | *app* → «app». Los nombres de cada app tienen que coincidir con item/GauntletAppTable.tbb. |
| App Points | puntos de app | Decidido 2026-11-08 (G-2) | Sigla *AP* → «PA». |
| Auto-Pinpoint | Combate automático dirigido | Decidido 2026-11-08 (G-2) | Una app; variante de *Auto-Battle*. |
| Relic of Revival | Reliquia de resurrección | Decidido 2026-11-08 (G-2) | |
| Main Partner | Acompañante principal | Decidido 2026-11-08 (G-2) | *Acompañante* no marca el género del compañero (E-40). |
| Reincarnation Restart | Reinicio por reencarnación | Decidido 2026-11-08 (G-2) | |
| New Life Restart | Reinicio desde cero | Decidido 2026-11-08 (G-2) | El inglés también dice *New Life Start*: va igual. |
| New Life Start | Reinicio desde cero | Decidido 2026-11-08 (G-2) | |
| Dexterity | Destreza | Decidido 2026-11-08 (G-2) | Abreviaturas de las estadísticas: *St, Dx, Ma, Ag, Lu* → «Fu, De, Ma, Ag, Su». |
| Gun | Disparo | Decidido 2026-11-08 (G-2) | Elemento de ataque. |
| Hit/evade rate | Precisión/evasión | Decidido 2026-11-08 (G-2) | También *hit/evasion rate*. |
| preemptive attack | ataque preventivo | Decidido 2026-11-08 (G-2) | No es *surprise attack*, que IVA usa aparte. |
| smirk | sonríe con malicia | Decidido 2026-11-08 (G-2) | Estado de combate; el sustantivo *Smirk* → «Sonrisa maliciosa». |
| Smirk | Sonrisa maliciosa | Decidido 2026-11-08 (G-2) | |
| whispered skill | habilidad susurrada | Decidido 2026-11-08 (G-2) | *whisper* → «susurrar». |
| Demon Market | Mercado de demonios | Decidido 2026-11-08 (G-2) | |
| Godslayer | Matadioses | Decidido 2026-11-08 (G-2) | Título del jugador. |
| Champion | Campeón | Decidido 2026-11-08 (G-2) | Título del jugador. |
| Gauntlet | Guantelete | Decidido 2026-11-08 (G-2) | El aparato del brazo del jugador. |
| smartphone | teléfono | Decidido 2026-11-08 (G-2) | |
| domain | dominio | Decidido 2026-11-08 (G-2) | Zona de un demonio. |
| DNA | ADN | Decidido 2026-11-08 (G-2) | *datos de ADN*. |
| ON/OFF | ACTIVAR/DESACTIVAR | Provisional 2026-11-08 (G-2) | Tiene que coincidir con la etiqueta del menú; se comprueba en el juego. |
| Challenge Quest | Misión de desafío | Decidido 2026-11-08 (G-2) | |
| K’s Tavern | Taberna de K | Decidido 2026-11-08 (G-2) | |
| Navarre | Navarre | Decidido 2026-11-08 (G-2) | Nombre propio. |
| Nanashi | Nanashi | Decidido 2026-11-08 (G-2) | Nombre del protagonista. |
| Merkabah | Merkabah | Decidido 2026-11-08 (G-2) | Nombre propio. |
| Divine Powers | Poderes Divinos | Decidido 2026-11-08 (G-2) | Un grupo de dioses, no la raza *Divine* (que se decide en Tablas). |
| Mitra-Buddha | Mitra-Buda | Decidido 2026-11-08 (G-2) | |
| performance | capacidades | Decidido 2026-11-08 (G-2) | Las de un demonio, en la búsqueda de fusión. |

Opciones del menú de fusión (provisional, se comprueban en el juego): *Search* → «Buscar», *Special* → «Especial», *End* → «Terminar». No van en la tabla porque son palabras comunes en otras frases.

Pisos del ascensor (provisional, se comprueba en el juego): *1F, 2F...* → «P1, P2...»; *B1, B2...* → «S1, S2...». No van en la tabla porque son opciones sueltas.

*Power*, *Attack* y *Legion* no son términos fijos: llevan su nombre oficial solo cuando son el demonio (Potestad, Legión). *Attack* como estadística → «Ataque».

#### Candidatos de SMT V que aparecen en la Interfaz

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Demon | Demonio | SMT V (personaje) | Demonio en general; en IVA va en *Demon Compendium*, *Demon Fusion*, *Demon Market* y como etiqueta de quien habla. |
| Demons | Demonios | SMT V (personaje) | |
| Lucifer | Lucifer | SMT V (personaje) | Demonio. |
| Megami | Megami | SMT V (raza) | Raza. También va en el título *Shin Megami Tensei*, que no se traduce. |
| Element | Elemental | SMT V (raza) | Raza (unite/unite.mbm#63-66). |
| Foul | Fétido | SMT V (raza) | Raza (*Foul Slime*, unite/unite.mbm#62). |
| Slime | Limo | SMT V (personaje) | Demonio. |
| Mitra | Mitra | SMT V (personaje) | Deidad. IVA también usa *Mitra-Buddha* (por decidir). |
| Enduring Soul | Alma inmortal | SMT V (habilidad) | Habilidad. |
| Diamond | Diamante | SMT V (objeto) | Joya. En el contenido descargable va también en *Diamond Realm*, un lugar. |
| Emerald | Esmeralda | SMT V (objeto) | Joya. |
| Garnet | Granate | SMT V (objeto) | Joya. |

### Resto de los candidatos

Candidatos de `glossary-candidates.tsv` que no aparecen en archivos de la Interfaz, en el orden del TSV (más frecuentes primero).

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Dagda | Dagda | SMT V (personaje) | Personaje y demonio. |
| Fiend | Oscuro | SMT V (raza) | Raza. |
| Angel | Ángel | SMT V (personaje) | Demonio; también etiqueta de quien habla (*Angel*) y en *Angel forces*. |
| Odin | Odín | SMT V (personaje) | Demonio. |
| Adramelech | Adramelec | SMT V (personaje) | Demonio. |
| Mara | Mara | SMT V (personaje) | Demonio. |
| Arahabaki | Arahabaki | SMT V (personaje) | Demonio. |
| Inanna | Inanna | SMT V (personaje) | Personaje y demonio. |
| Danu | Danu | SMT V (personaje) | Personaje y demonio. |
| Fairy | Hada | SMT V (personaje) | Raza. *Fairy Forest*, un lugar, se decide con los lugares. |
| Poison | Veneno | SMT V (estado) | Estado alterado. |
| Charm | Encanto | SMT V (estado) | Estado alterado. |
| Life Stone | Piedra vital | SMT V (objeto) | Objeto. |
| Sleep | Sueño | SMT V (estado) | Estado alterado. |
| Dormarth | Dormarth | SMT V (personaje) | Demonio. |
| Yamata-no-Orochi | Yamata-no-Orochi | SMT V (personaje) | Demonio. |
| Mitama | Mitama | SMT V (raza) | Raza. También en nombres de demonios (*Ara Mitama*, *Ukano Mitama*). |
| Vishnu | Vishnu | SMT V (personaje) | Deidad; IVA también tiene la forma *Vishnu-Flynn*, que se decide aparte. |
| Quetzalcoatl | Quetzalcóatl | SMT V (personaje) | Demonio. |
| Loki | Loki | SMT V (personaje) | Demonio. |
| Mother Harlot | Ramera babilónica | SMT V (personaje) | Demonio. |
| Satan | Satán | SMT V (personaje) | Demonio. |
| Dionysus | Dioniso | SMT V (personaje) | Demonio. |
| King Frost | Rey Frost | SMT V (personaje) | Demonio. |
| Shiva | Shiva | SMT V (personaje) | Demonio. |
| Voice | Voz | SMT V (personaje) | Etiqueta de quien habla cuando no se ve quién es (*Voice from the monitor* → *Voz del monitor*). |
| Baal | Baal | SMT V (personaje) | Demonio. |
| Masakado | Masakado | SMT V (personaje) | Figura histórica y demonio (*Masakado (Giant)*, *Taira Masakado*). |
| Mephisto | Mefisto | SMT V (personaje) | Demonio. |
| Michael | Miguel | SMT V (personaje) | Arcángel; en IVA va en *Spear of Michael* (*Lanza de Miguel*). |
| Sukuna-Hikona | Sukuna-Hikona | SMT V (personaje) | Demonio. |
| Jack Frost | Jack Frost | SMT V (personaje) | Demonio. |
| Jikokuten | Jikokuten | SMT V (personaje) | Demonio. |
| Koumokuten | Koumokuten | SMT V (personaje) | Demonio. |
| Medicine | Medicina | SMT V (objeto) | Objeto. En las descripciones de otros objetos es la palabra común (*medicina*). |
| Zouchouten | Zouchouten | SMT V (personaje) | Demonio. |
| Angels | Ángeles | SMT V (personaje) | Plural de *Angel*. |
| Anubis | Anubis | SMT V (personaje) | Demonio. |
| Bishamonten | Bishamonten | SMT V (personaje) | Demonio. |
| Black Frost | Frost oscuro | SMT V (personaje) | Demonio. |
| Cu Chulainn | Cú Chulainn | SMT V (personaje) | Demonio. |
| Okuninushi | Okuninushi | SMT V (personaje) | Demonio. |
| Skadi | Skadi | SMT V (personaje) | Demonio. |
| Tiamat | Tiamat | SMT V (personaje) | Demonio. |
| Woman | Mujer | SMT V (personaje) | Etiqueta de quien habla y de personajes de la ciudad (*Gaea Woman*). |
| Black Rider | Jinete negro | SMT V (personaje) | Demonio. |
| Cleopatra | Cleopatra | SMT V (personaje) | Personaje y demonio. |
| Dragon | Dragón | SMT V (raza) | Raza. También en descripciones (*Dragon King*, *Golden Dragon*). |
| Fallen | Caído | SMT V (raza) | Raza. También en *Fallen angel* (*ángel caído*). |
| Matador | Matador | SMT V (personaje) | Demonio. |
| Metatron | Metatrón | SMT V (personaje) | Demonio. |
| Ongyo-Ki | Ongyo-Ki | SMT V (personaje) | Demonio. |
| Pale Rider | Jinete pálido | SMT V (personaje) | Demonio. |
| Red Rider | Jinete rojo | SMT V (personaje) | Demonio. |
| Scathach | Scáthach | SMT V (personaje) | Demonio. |
| Setanta | Setanta | SMT V (personaje) | Demonio. |
| Siegfried | Sigfrido | SMT V (personaje) | Demonio. |
| Throne | Trono | SMT V (personaje) | Demonio. También en *Throne of God*, un lugar. |
| Trumpeter | Trompetista | SMT V (personaje) | Demonio. |
| Tyrant | Tirano | SMT V (raza) | Raza. |
| White Rider | Jinete blanco | SMT V (personaje) | Demonio. |
| Aquans | Aquans | SMT V (personaje) | Demonio. |
| Avatar | Avatar | SMT V (raza) | Raza. También en el objeto *Avatar's Hat*. |
| Belial | Belial | SMT V (personaje) | Demonio. |
| Erthys | Erthys | SMT V (personaje) | Demonio. |
| Isis | Isis | SMT V (personaje) | Demonio. |
| Nue | Nue | SMT V (personaje) | Demonio. |
| Oberon | Oberón | SMT V (personaje) | Demonio. |
| Ose | Ose | SMT V (personaje) | Demonio. |
| Parvati | Parvati | SMT V (personaje) | Demonio. |
| Zeus | Zeus | SMT V (personaje) | Dios mencionado en perfiles; también en *Zeus Rounds*. |
| Aeros | Aeros | SMT V (personaje) | Demonio. |
| Anzu | Anzu | SMT V (personaje) | Demonio. *Toyo Anzu* (ms_search_Table.tbb) es otro nombre. |
| Azazel | Azazel | SMT V (personaje) | Demonio. |
| Bead | Abalorio | SMT V (objeto) | Objeto. |
| Deity | Deidad | SMT V (raza) | Raza. También en *Deity's Puppet* y *Powerful Deity*. |
| Demi-fiend | Semioscuro | SMT V (personaje) | Personaje del contenido descargable. |
| Dominion | Dominio | SMT V (personaje) | Demonio. |
| Drake | Drake | SMT V (raza) | Raza. |
| Enigma | Enigma | SMT V (raza) | Raza. |
| Flaemis | Flaemis | SMT V (personaje) | Demonio. |
| Fury | Furia | SMT V (raza) | Raza. También en *Fury Earring* y en la habilidad *Deadly Fury*. |
| Herald | Heraldo | SMT V (raza) | Raza. |
| Kali | Kali | SMT V (personaje) | Demonio. |
| Kresnik | Kresnik | SMT V (personaje) | Demonio. |
| Kunitsu | Kunitsu | SMT V (raza) | Raza (*Kunitsu-kami* en el texto). |
| Mot | Mot | SMT V (personaje) | Demonio. |
| Rakshasa | Ráksasa | SMT V (personaje) | Demonio. |
| Seth | Set | SMT V (personaje) | Demonio. |
| Vasuki | Vasuki | SMT V (personaje) | Demonio. |
| Abaddon | Abadón | SMT V (personaje) | Demonio. |
| Agathion | Agathion | SMT V (personaje) | Demonio. |
| Asura | Asura | SMT V (personaje) | Demonio y figura mitológica (*the Asuras*). |
| Azumi | Azumi | SMT V (personaje) | Demonio. En un perfil, *the Azumi* es una tribu. |
| Baihu | Baihu | SMT V (personaje) | Demonio. |
| Beelzebub | Belcebú | SMT V (personaje) | Demonio. |
| Cherub | Querubín | SMT V (personaje) | Demonio. |
| Chimera | Quimera | SMT V (personaje) | Demonio. |
| Cybele | Cibeles | SMT V (personaje) | Diosa mencionada en perfiles. |
| Fafnir | Fafnir | SMT V (personaje) | Demonio. |
| Fenrir | Fenrir | SMT V (personaje) | Demonio. |
| Fortuna | Fortuna | SMT V (personaje) | Demonio. |
| Ishtar | Ishtar | SMT V (personaje) | Demonio. |
| Jaki | Jaki | SMT V (raza) | Raza. |
| Kinmamon | Kinmamon | SMT V (personaje) | Demonio. |
| Kudlak | Kudlak | SMT V (personaje) | Demonio. |
| Mishaguji | Mishaguji | SMT V (personaje) | Demonio. |
| Pixie | Pixie | SMT V (personaje) | Demonio. También en el objeto *Pixie Knife*. |
| Principality | Principado | SMT V (personaje) | Demonio. |
| Surt | Surt | SMT V (personaje) | Demonio. |
| Take-Minakata | Take-Minakata | SMT V (personaje) | Demonio. |
| Titania | Titania | SMT V (personaje) | Demonio. |
| Valkyrie | Valquiria | SMT V (personaje) | Demonio. |
| Agi | Agi | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Agi Stone*. |
| Ara Mitama | Ara Mitama | SMT V (personaje) | Demonio. |
| Archangel | Arcángel | SMT V (personaje) | Demonio. |
| Attis | Atis | SMT V (personaje) | Demonio. |
| Avian | Aviar | SMT V (raza) | Raza. |
| Barong | Barong | SMT V (personaje) | Demonio. |
| Beast | Bestia | SMT V (raza) | Raza. |
| Brute | Bruto | SMT V (raza) | Raza. |
| Chernobog | Chernobog | SMT V (personaje) | Demonio. |
| Chi You | Chi You | SMT V (personaje) | Demonio. |
| Dakini | Dakini | SMT V (personaje) | Demonio. |
| Decarabia | Decarabia | SMT V (personaje) | Demonio. |
| Dekaja | Dekaja | SMT V (habilidad) | Habilidad; también el objeto *Dekaja Stone*. |
| Femme | Fémina | SMT V (raza) | Raza. |
| Feng Huang | Feng Huang | SMT V (personaje) | Demonio. |
| Ganesha | Ganesha | SMT V (personaje) | Demonio. |
| Garuda | Garuda | SMT V (personaje) | Demonio. |
| Genma | Genma | SMT V (raza) | Raza. |
| Goddess | Diosa | SMT V (personaje) | Etiqueta de quien habla (*Goddess of Tokyo*) y objeto *Goddess Feather*. |
| Hare of Inaba | Liebre de Inaba | SMT V (personaje) | Demonio. |
| Horus | Horus | SMT V (personaje) | Dios mencionado en perfiles. |
| Incubus | Íncubo | SMT V (personaje) | Demonio. |
| Ippon-Datara | Ippon-Datara | SMT V (personaje) | Demonio. |
| Jirae | Jirae | SMT V (raza) | Raza. |
| Kaiwan | Kaiwan | SMT V (personaje) | Demonio. |
| Karasu Tengu | Karasu Tengu | SMT V (personaje) | Demonio. |
| Kin-Ki | Kin-Ki | SMT V (personaje) | Demonio. |
| Kishin | Kishin | SMT V (raza) | Raza. |
| Koppa Tengu | Koppa Tengu | SMT V (personaje) | Demonio. |
| Kurama Tengu | Kurama Tengu | SMT V (personaje) | Demonio. |
| Kushi Mitama | Kushi Mitama | SMT V (personaje) | Demonio. |
| Mad Gasser | Gasero loco | SMT V (personaje) | Demonio. |
| Mandrake | Mandrágora | SMT V (personaje) | Demonio. |
| Megido | Megido | SMT V (habilidad) | Habilidad; también en los objetos *Megido Stone* y *Megido Fire*. |
| Meta | Meta | SMT V (raza) | Raza. |
| Mokoi | Mokoi | SMT V (personaje) | Demonio. |
| Mothman | Hombre polilla | SMT V (personaje) | Demonio. |
| Naga | Naga | SMT V (personaje) | Demonio. |
| Nebiros | Naberius | SMT V (personaje) | Demonio. SMT V lo llama *Naberius* en todas sus tablas (también *Nebiros's Essence* ⇒ *Esencia de Naberius*). |
| Nigi Mitama | Nigi Mitama | SMT V (personaje) | Demonio. |
| Oni | Oni | SMT V (personaje) | Demonio. |
| Orthrus | Ortro | SMT V (personaje) | Demonio. |
| Patra | Patra | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Patra Stone*. |
| Peallaidh | Peallaidh | SMT V (personaje) | Demonio. |
| Poltergeist | Poltergeist | SMT V (personaje) | Demonio. |
| Primal | Primario | SMT V (raza) | Raza. |
| Rangda | Rangda | SMT V (personaje) | Demonio. |
| Raptor | Rapaz | SMT V (raza) | Raza. |
| Saki Mitama | Saki Mitama | SMT V (personaje) | Demonio. |
| Samael | Samael | SMT V (personaje) | Demonio. |
| Sarasvati | Sarasvati | SMT V (personaje) | Demonio. |
| Senri | Senri | SMT V (personaje) | Demonio. |
| Silky | Silky | SMT V (personaje) | Demonio. |
| Snake | Serpiente | SMT V (raza) | Raza. |
| Soma | Soma | SMT V (objeto) | Objeto. |
| Sraosha | Sraosha | SMT V (personaje) | Demonio. |
| Thor | Thor | SMT V (personaje) | Demonio. |
| Tzitzimitl | Tzitzimitl | SMT V (personaje) | Demonio. |
| Vile | Vil | SMT V (raza) | Raza. |
| Wilder | Salvaje | SMT V (raza) | Raza. |
| Yatagarasu | Yatagarasu | SMT V (personaje) | Demonio. |
| Yoma | Yoma | SMT V (raza) | Raza. |
| Zhen | Zhen | SMT V (personaje) | Demonio. |
| Agilao | Agilao | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Agilao Stone*. |
| Alice | Alicia | SMT V (personaje) | Demonio. |
| Alilat | Alilat | SMT V (personaje) | Demonio. |
| Amrita Shower | Lluvia de amrita | SMT V (objeto) | Objeto. |
| Amrita Soda | Refresco de amrita | SMT V (objeto) | Objeto. |
| Apsaras | Apsará | SMT V (personaje) | Demonio. |
| Artemis | Artemisa | SMT V (personaje) | Diosa mencionada en un perfil. |
| Atropos | Átropos | SMT V (personaje) | Demonio. |
| Attack Mirror | Espejo ofensivo | SMT V (objeto) | Objeto. |
| Baphomet | Baphomet | SMT V (personaje) | Demonio. |
| Basilisk | Basilisco | SMT V (personaje) | Demonio. |
| Bead Chain | Cadena de abalorios | SMT V (objeto) | Objeto. |
| Belphegor | Belfegor | SMT V (personaje) | Demonio mencionado en un perfil. |
| Berith | Berith | SMT V (personaje) | Demonio mencionado en un perfil. |
| Bufu | Bufu | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Bufu Stone*. |
| Bufula | Bufula | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Bufula Stone*. |
| Cerberus | Cerbero | SMT V (personaje) | Demonio. |
| Chakra Drop | Gota de chakra | SMT V (objeto) | Objeto. |
| Chakra Elixir | Elixir de chakra | SMT V (objeto) | Objeto. |
| Chakra Pot | Bote de chakra | SMT V (objeto) | Objeto. |
| Clotho | Cloto | SMT V (personaje) | Demonio. |
| Deadly Fury | Furia mortal | SMT V (habilidad) | Habilidad del contenido descargable. |
| Dekunda | Dekunda | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Dekunda Stone*. |
| Endure | Último aliento | SMT V (habilidad) | Habilidad (*Grants targets Endure*, SkillHelpMess). |
| Freikugel | Freikugel | SMT V (habilidad) | Habilidad del contenido descargable. |
| Fuu-Ki | Fuu-Ki | SMT V (personaje) | Demonio. |
| Gabriel | Gabriel | SMT V (personaje) | Arcángel (*Gabriel (Giant)*). |
| Gaea Rage | Ira de Gea | SMT V (habilidad) | Habilidad del contenido descargable. |
| Gogmagog | Gogmagog | SMT V (personaje) | Demonio. |
| Gremlin | Gremlin | SMT V (personaje) | Demonio. |
| Halphas | Halphas | SMT V (personaje) | Demonio. |
| Hama | Hama | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Hama Stone*. |
| Hamaon | Hamaon | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Hamaon Stone*. |
| Hanuman | Hánuman | SMT V (personaje) | Demonio. |
| Hariti | Hariti | SMT V (personaje) | Demonio. |
| High Pixie | Gran Pixie | SMT V (personaje) | Demonio. |
| Hua Po | Hua Po | SMT V (personaje) | Demonio. |
| Huang Long | Huang Long | SMT V (personaje) | Demonio. |
| Inugami | Inugami | SMT V (personaje) | Demonio. |
| Kelpie | Kelpie | SMT V (personaje) | Demonio. |
| Kikuri-Hime | Kikuri-Hime | SMT V (personaje) | Demonio. |
| Lachesis | Láquesis | SMT V (personaje) | Demonio. |
| Lakshmi | Laksmí | SMT V (personaje) | Demonio. |
| Leanan Sidhe | Leanan Sidhe | SMT V (personaje) | Demonio. |
| Lilim | Lilim | SMT V (personaje) | Demonio. |
| Lilith | Lilit | SMT V (personaje) | Figura mitológica mencionada en un perfil. |
| Mabufu | Mabufu | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mabufu Stone*. |
| Macabre | Macabro | SMT V (personaje) | Demonio. |
| Magic Mirror | Espejo mágico | SMT V (objeto) | Objeto. |
| Magma Axis | Explosión de magma | SMT V (habilidad) | Habilidad del contenido descargable. |
| Mahama | Mahama | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mahama Stone*. |
| Makami | Makami | SMT V (personaje) | Demonio. |
| Makarakarn | Makarakarn | SMT V (habilidad) | Habilidad. |
| Mamudo | Mamudo | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mamudo Stone*. |
| Maragi | Maragi | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Maragi Stone*. |
| Mastema | Mastema | SMT V (personaje) | Demonio. |
| Mazan | Mazan | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mazan Stone*. |
| Mazio | Mazio | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mazio Stone*. |
| Me Patra | Me Patra | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Me Patra Stone*. |
| Megidola | Megidola | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Megidola Stone*. |
| Mermaid | Sirena | SMT V (personaje) | Demonio. |
| Mithras | Mitras | SMT V (personaje) | Demonio. |
| Mudo | Mudo | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mudo Stone*. |
| Mudoon | Mudoon | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Mudoon Stone*. |
| Narcissus | Narciso | SMT V (personaje) | Demonio. |
| Nekomata | Nekomata | SMT V (personaje) | Demonio. |
| Nezha Taizi | Nezha Taizi | SMT V (personaje) | Deidad mencionada en un perfil. |
| Norn | Norna | SMT V (personaje) | Demonio. |
| Nozuchi | Nozuchi | SMT V (personaje) | Demonio. |
| Obariyon | Obariyon | SMT V (personaje) | Demonio. |
| Onmoraki | Onmoraki | SMT V (personaje) | Demonio. |
| Ox Bezoar | Bezoar de buey | SMT V (objeto) | Objeto. |
| Pisaca | Pisaca | SMT V (personaje) | Demonio. |
| Preta | Preta | SMT V (personaje) | Demonio. |
| Professor | Profesor | SMT V (personaje) | Título (*Professor Matsuda* → *el profesor Matsuda*). |
| Raphael | Rafael | SMT V (personaje) | Arcángel (*Raphael (Giant)*). |
| Revival Bead | Abalorio de resurrección | SMT V (habilidad) | Objeto (en SMT V está en la tabla de habilidades). |
| Sandman | Sandman | SMT V (personaje) | Demonio. |
| Shiisaa | Shiisaa | SMT V (personaje) | Demonio. |
| Soma Drop | Gota de soma | SMT V (objeto) | Objeto. |
| Sophia | Sofía | SMT V (personaje) | Figura mitológica; en IVA va en el objeto *Sophia's Sword*. |
| Succubus | Súcubo | SMT V (personaje) | Demonio. |
| Sudama | Sudama | SMT V (personaje) | Demonio. |
| Sui-Ki | Sui-Ki | SMT V (personaje) | Demonio. |
| Tetrakarn | Tetrakarn | SMT V (habilidad) | Habilidad. |
| Thoth | Tot | SMT V (personaje) | Demonio. |
| Thunderbird | Ave del trueno | SMT V (personaje) | Demonio. |
| Tsuchigumo | Tsuchigumo | SMT V (personaje) | Demonio. |
| Uriel | Uriel | SMT V (personaje) | Arcángel (*Uriel (Giant)*). |
| Vouivre | Vouivre | SMT V (personaje) | Demonio. |
| Yoshitsune | Yoshitsune | SMT V (personaje) | Demonio. |
| Yurlungur | Yurlungur | SMT V (personaje) | Demonio. |
| Zan | Zan | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Zan Stone*. |
| Zanma | Zanma | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Zanma Stone*. |
| Zhu Tun She | Zhu Tun She | SMT V (personaje) | Demonio. |
| Zio | Zio | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Zio Stone*. |
| Zionga | Zionga | SMT V (habilidad) | Habilidad; en IVA va en el objeto *Zionga Stone*. |
