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
| Sky Terminal | Terminal de Sky Tower | Decidido 2026-11-08 (G-2) | *Sky* es Sky Tower (camp/SortMenuTable.tbb). |
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

### Tablas

Filas *oficial* (G-1) que salen de `system-terms-tablas.tsv` y de las tablas .tbb del juego base. No repiten las 437 filas que GLOSSARY.md ya tiene. Los bytes son los de T-4 (las letras con tilde ocupan 2) contra el `max` del campo.

#### Términos de sistema (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Sort | Ordenar | SMT V (etiqueta; ejemplo: *Sort by cost.* ⇒ *Ordena por coste.*) | Menú de orden: 48 textos *Sort by race/level/HP...* (camp/SortMenuTable.tbb, columna 24). Se toma solo el término: *costo*, no *coste* (E-10). |
| ascending | ascendente | SMT V (etiqueta *Ascending* ⇒ *Ascendente*) | Orden de una lista. IVA lo escribe en minúscula: *switch between ascending and descending*, 50 textos de camp/SortMenuTable.tbb. |
| descending | descendente | SMT V (etiqueta *Descending* ⇒ *Descendente*) | Igual que *ascending*. |
| Default | Predeterminado | SMT V (etiqueta; ejemplo: *Revert all settings to default?* ⇒ *¿Revertir a los valores predeterminados?*) | Orden predeterminado (camp/SortMenuTable.tbb#0.0.2: 14/21 bytes). Concuerda: *orden predeterminado*. |
| Status | Estado | SMT V (etiqueta) | *View the party's status* (camp/CampComTable.tbb#0.14.4). Con *Ailment* → «Estado alterado», que ya está en la tabla. |
| key items | objetos clave | SMT V (ejemplo: *Key Items* ⇒ *Objetos clave*) | *View key items in your inventory.* (camp/CampComTable.tbb#0.13.4). |
| Hide | Ocultar | SMT V (etiqueta; ejemplo: *Hide names* ⇒ *Ocultar nombres*) | *View/Hide detailed search options* (unite/SearchTable.tbb#0.2.68), con *View* → «Ver» (provisional en la tabla). |
| Options | Opciones | SMT V (etiqueta *OPTIONS* ⇒ *Opciones*) | *Additional Options* y *search options* (unite/SearchTable.tbb#0.12.8, #0.2.68). |
| Name | Nombre | SMT V (etiqueta) | *Skill Name* (unite/SearchTable.tbb#0.10.8) y *the name shown on the DDS Card* (camp/CampComTable.tbb#0.56.4). |
| Sell | Vender | SMT V (etiqueta de tienda; ejemplo: *Sell all* ⇒ *Vender todos*) | Opción de tienda (*Sell Possessions*, shop/ShopTable.tbb#0.3.0), como *Buy* → «Comprar». |
| Light | Luz | SMT V (etiqueta; ejemplo: *: Light* ⇒ *: Luz*) | Elemento (*Light Type*, camp/SortMenuTable.tbb#0.47.2). En nombres de objetos es adjetivo (*Light Grimoire*, *Light Gun*): el validador avisará ahí, como ya pasa con *Fire*. |
| Dark | Oscuridad | SMT V (etiqueta; ejemplo: *: Dark* ⇒ *: Oscuridad*) | Elemento (*Dark Type*, camp/SortMenuTable.tbb#0.48.2). Mismo aviso en objetos (*Dark Earring*, *Dark Goth*). |
| Force | Choque | SMT V (etiqueta; ejemplo: *: Force* ⇒ *: Choque*) | Elemento (*Force Type*, camp/SortMenuTable.tbb#0.46.2). En *Azteca Force*, *Greek Force* (hordas) y *Counter-Demon Force* (un grupo) es otra palabra: ver pending.md. |
| EXP | EXP | SMT V (ejemplo: *EXP and Macca earned greatly increased...* ⇒ *Aumenta mucho la EXP y los macca...*) | Experiencia; en femenino: *la EXP*. *Talk EXP Boost*, *Increases EXP gained* (item/GauntletAppTable.tbb, GauntletAppHelpMessage.tbb). |
| Your Room | Tu habitación | SMT V (etiqueta) | Destino del mapa (map/all/MapNextPointTable.tbb#0.1.8: 14/35 bytes). |
| New Game | Nueva partida | SMT V (etiqueta *NEW GAME* ⇒ *NUEVA PARTIDA*) | Menú de título (title/TitleTable.tbb#0.0.0: 13/19 bytes). Agregado: no está en el TSV porque sale una sola vez en la sección. |
| Load Game | Cargar partida | SMT V (etiqueta *Load Game* ⇒ *CARGAR PARTIDA*) | Menú de título (title/TitleTable.tbb#0.1.0: 14/19 bytes). Agregado, igual que *New Game*. |
| Use a skill. | Usa una habilidad. | SMT V (etiqueta) | Ayuda del comando de combate (battle/UI/BattleComTable.tbb#0.1.3, #1.1.3). |
| Use an item. | Usa un objeto. | SMT V (etiqueta) | Ayuda del comando de combate (battle/UI/BattleComTable.tbb#0.2.3, #1.2.3). |
| Vending Machine | Máquina expendedora | SMT V (ejemplo: *Relics acquired from vending machines* ⇒ *las reliquias que consigas en las máquinas expendedoras*) | Punto de búsqueda del mapa (map/all/ms_search_Table.tbb#0.74.0 y 5 más: 20/31 bytes). |

#### Lugares (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Tokyo | Tokio | SMT V (ejemplos: *Tokyo Conception* ⇒ *Concepción de Tokio*; *as you move about in Tokyo* ⇒ *mientras exploras Tokio*) | La ciudad (287 veces en IVA). Los lugares que la llevan (*Tokyo Station*, *Blasted Tokyo*...) están en pending.md. |
| Mt. | monte | SMT V (ejemplo: *Mt. Kurama in Kyoto* ⇒ *el monte Kurama, en Kioto*) | *Mt. Haku* → «Monte Haku» en la etiqueta del mapa (map/all/MapYukaTable.tbb#2.10.0: 10/31 bytes); en minúscula a media frase (E-59). |
| Shinobazu Pond | estanque de Shinobazu | SMT V (ejemplo: *in Shinobazu Pond* ⇒ *en el estanque de Shinobazu*) | El estanque de Ueno (event/quest/SubQuestData.tbb#0.43.116, event/quest/quest145.mbm#0). Al inicio de una etiqueta, *Estanque de Shinobazu*. |

#### Demonios y figuras mitológicas (oficiales)

No están en las tablas de nombres de SMT V, pero SMT V los nombra en sus perfiles con el mismo sentido (la misma figura). Todos están en battle/NKMSortIndex.tbb y casi todos, también en los mensajes.

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Maitreya | Maitreya | SMT V (ejemplo: *a fusion of Buddha, Guanyin, and Maitreya* ⇒ *una fusión de Buda, Guanyin y Maitreya*) | Personaje y demonio (51 veces en IVA). |
| Izanami | Izanami | SMT V (ejemplo: *who relayed Izanami's words* ⇒ *que difundía la palabra de Izanami*) | Demonio. |
| Take-Mikazuchi | Take-Mikazuchi | SMT V (ejemplo: *He fought Take-Mikazuchi* ⇒ *Luchó contra Take-Mikazuchi*) | Demonio (49 veces en IVA). |
| Yggdrasil | Yggdrasil | SMT V (ejemplo: *below the roots of Yggdrasil* ⇒ *bajo las raíces de Yggdrasil*) | Demonio. |
| Amaterasu | Amaterasu | SMT V (ejemplo: *the goddess Amaterasu* ⇒ *la diosa Amaterasu*) | Demonio. *Lady Amaterasu* es otro caso (PENDING, *Lady*). |
| Osiris | Osiris | SMT V (ejemplo: *sides with Osiris and Isis* ⇒ *al lado de Osiris e Isis*) | Demonio. |
| Anat | Anat | SMT V (ejemplo: *the goddess Anat* ⇒ *la diosa Anat*) | Demonio. |
| Baldur | Baldur | SMT V (ejemplo: *Odin's child Baldur* ⇒ *Baldur, hijo de Odín*) | Demonio. |
| Huang Di | Huang Di | SMT V (ejemplo: *the Yellow Emperor Huang Di* ⇒ *el Emperador Amarillo Huang Di*) | Demonio. |
| YHVH | YHVH | SMT V (ejemplo: *Yahweh (YHVH)* ⇒ *Yahweh (YHVH)*) | Personaje (36 veces en IVA). *YHVH's Universe* está en pending.md. |
| Kama | Kama | SMT V (ejemplo: *Kama's mother* ⇒ *la madre de Kama*) | Demonio. |
| Diana | Diana | SMT V (ejemplo: *the Roman goddess Diana* ⇒ *la diosa romana Diana*) | Demonio. |
| Fuxi | Fuxi | SMT V (ejemplo: *Fuxi, also of the three sovereigns* ⇒ *A su compañero Fuxi*) | Demonio. |
| Apsu | Apsu | SMT V (ejemplo: *Born from Apsu and Tiamat* ⇒ *Nacido de Apsu y Tiamat*) | Demonio. |
| Sleipnir | Sleipnir | SMT V (ejemplo: *his eight-legged horse Sleipnir* ⇒ *su caballo de ocho patas, Sleipnir*) | Demonio. |
| Hagen | Hagen | SMT V (ejemplo: *the treacherous Hagen* ⇒ *el pérfido Hagen*) | Demonio (21 veces en IVA). |
| Susano-o | Susanoo | SMT V (ejemplo: *the storm god Susano-o* ⇒ *Susanoo, el dios de la tormenta*) | Demonio. SMT V lo escribe sin guion. |
| Kushinada-hime | Kushinada-Hime | SMT V (ejemplo: *Kushinada-Hime is a goddess* ⇒ *Kushinada-Hime es una diosa*) | Demonio. SMT V escribe *Hime* con mayúscula, como *Kikuri-Hime* (ya en la tabla). |

#### Decididos por el usuario: Tablas

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Human | Humano | Decidido 2026-11-08 (G-2) | La raza, el estado del jugador y *Human Army* → «Ejército humano». |
| Divine | Divino | Decidido 2026-11-08 (G-2) | La raza; *Divine Powers* → «Poderes Divinos». |
| Chaos | Caos | Decidido 2026-11-08 (G-2) | La raza, *Chaos Sword* → «Espada del Caos», *Chaos Realm* → «Reino del Caos». |
| Hunter | Cazador | Decidido 2026-11-08 (G-2) | *Hunters* → «Cazadores». En minúscula a media frase. |
| Hunter Association | Asociación de Cazadores | Decidido 2026-11-08 (G-2) | Por sede: «Asociación de Cazadores de Ueno». Si no cabe en sus bytes, ver los patrones. |
| Samurai | samurái | Decidido 2026-11-08 (G-2) | Plural «samuráis» (RAE); invariable en género. |
| Ashura-kai | Ashura-kai | Decidido 2026-11-08 (G-2) | *el Ashura-kai*; *Ashura-kai member* → «Miembro del Ashura-kai». |
| Ring of Gaea | Anillo de Gea | Decidido 2026-11-08 (G-2) | Como SMT V (*Gaea* ⇒ *Gea*). |
| Seraph | Serafín | Decidido 2026-11-08 (G-2) | Como SMT V con los coros de ángeles. |
| Virtue | Virtud | Decidido 2026-11-08 (G-2) | Como SMT V con los coros de ángeles. |
| partner | acompañante | Decidido 2026-11-08 (G-2) | Como *Main Partner*. |
| Laws of Fusion | leyes de la fusión | Decidido 2026-11-08 (G-2) | Variante con mayúscula de *laws of fusion* (unite/SearchTable.tbb). |
| K's Tavern | Taberna de K | Decidido 2026-11-08 (G-2) | Variante con apóstrofo recto de *K’s Tavern*. |

**Raza + nombre** (decidido 2026-11-08): el juego inserta la raza y el nombre con dos códigos seguidos, la raza primero (`{F875}{0100} {F873}{0100}`), y T-1 no deja cambiar el orden. Por eso va siempre raza + nombre, también en el texto escrito: «Fétido Limo», «Hada Napaea».

#### Patrones de Tablas (decididos 2026-11-08)

Propuestas del terminólogo aprobadas por el usuario. Los bytes son los de T-4 contra el `max` del campo.

#### Pendientes anteriores que aparecen en Tablas

- `Divine` (terminólogo, otro sentido) → «Divino», como SMT V, y se puede fijar ya. En Tablas solo es la raza (battle/NKMSortIndex.tbb#0.5.0). En los mensajes, las 21 veces que aparece sola son *Divine{F801}Powers* partido por un salto. El validador acepta *Divinos* en *Poderes Divinos* (term_rx en tools/check.py quita la terminación), así que no avisaría de más.
- `Human` (terminólogo, otro sentido) → «Humano», y se puede fijar. Es la raza (battle/NKMSortIndex.tbb#0.52.0), el estado del jugador (status/status.tbb#0.0.0, 6/15 bytes) y *Human Army* (→ «Ejército humano»). Corrección a lo que dice PENDING: el validador **no** avisaría en los adjetivos femeninos, porque term_rx reduce *Humano* a *Human\w\** y acepta *humana*, *humanos*.
- `Lady` (terminólogo, otro sentido): en Tablas solo es la raza (battle/NKMSortIndex.tbb#0.25.0) → «Dama». No se puede fijar: en los mensajes es casi siempre un tratamiento (*Lady Yuriko* 6, *Lady Mii* 5, *Lady Kei* 5, *Lady Amaterasu*), y ahí el validador pediría *Dama*. Lo mismo para *Miss Isabeau* (event/HunterDataBase) y *Lord Nandou* (battle/NKMSortIndex.tbb): se deciden juntos como tratamientos.
- `Holy`, `Night` (terminólogo, otro sentido): las razas (#0.14.0, #0.31.0) → «Sacra», «Nocturno», como SMT V. No se fijan: *Holy Fruit* (item/ItemTable.tbb#1.20.0) → «Fruta sagrada», *Night Stalker* (un demonio, abajo) y *’Night* son otra cosa.
- `Chaos` (terminólogo, otro sentido) → «Caos» en todo, y se puede fijar: la raza (#0.53.0), *Chaos Sword* (item/ItemTable.tbb#2.80.0) → «Espada del Caos», *Chaos Realm* (map/all/MapSystemTable.tbb) → «Reino del Caos», *Horns of Chaos* → «Cuernos del Caos», los títulos *Bearer of Chaos* y *Ruler of Chaos*.
- `Ruler of Chaos`, `Researcher` (terminólogo, género): los títulos de la tarjeta DDS (camp/CampCecTable.tbb) describen al jugador, que es masculino (DECISIONS 2026-11-08; ficha de Napaea), y la misma lista trae *Lucky Boy*, *Younger Boy* y *Cute Lil' Bro*. Propuesta: masculino en todos los títulos (*Regente del caos*, *Investigador*), sin marcar el género con dudas.
- `Grimoire`, `Seal`, `Soda` (terminólogo, otro sentido): se confirman con las Tablas: «Grimorio ligero», «Grimorio pesado» (item/ItemTable.tbb#1.10.0, #1.11.0), «Sello de la ilusión», «Sello del rechazo» (#0.33.0, #0.34.0), «Botella de refresco» (#4.104.0, 19/31 bytes).
- `Gae Bolg` (terminólogo, otro sentido) → «Gae Bolg» (item/ItemTable.tbb#2.92.0). Va con los nombres propios de armas (abajo).
- `Purgatorium` (terminólogo, otro sentido): la etiqueta de la Terminal (camp/SortMenuTable.tbb#0.66.2, max 21) → «Purgatorium» (11 bytes), porque el inglés también usa la forma latina. Alternativa: «Purgatorio» (11).
- `Worker`, `Yoko` (terminólogo, otro sentido): *Excavation Worker Quarters* (map/all/MapNextPointTable.tbb#0.35.8) → «Alojamiento de los excavadores» (30/35); *Yoko Jewelry* (map/all/ms_search_Table.tbb#0.10.0) → «Joyería Yoko».
- `Maria` (terminólogo, otro sentido): *Black Maria* (battle/NKMSortIndex.tbb#1.367.0) → «María Negra». SMT V traduce el *Black* de los demonios (*Black Rider* ⇒ *Jinete negro*, *Black Frost* ⇒ *Frost oscuro*) y escribe *María*. Alternativa: «Black Maria».
- `Counter` (terminólogo, otro sentido): *Counter-Demon Force* (event/HunterDataBase/HunterDataTable.tbb) → «Fuerza Antidemonios» (19/37). El glosario fijaría *Force* → «Choque» (rows.md): el validador avisará en este nombre.
- **St. Germain** (orquestador, nombres): en el juego base solo sale *St. Germain Hole* (battle/NKMSortIndex.tbb#1.1072.0) → «Agujero de Saint Germain» (24/31), con el nombre decidido. Las tablas del contenido descargable (addon/testdata) son otra sección: propuesta, «Saint Germain» también ahí.
- **Mikado Terminal, Sky Terminal** (provisionales): en la lista de Terminales (camp/SortMenuTable.tbb#0.53-77) cada etiqueta es el nombre del lugar (*Shinjuku*, *Midtown*, *Ichigaya*), y la de Mikado está vacía («0», #0.62.2). *Sky* (#0.65.2) sería entonces un lugar, probablemente *Sky Tower* (13 veces en los mensajes), y «Terminal del Cielo» lo traduciría como palabra común. Propuesta: *Sky* → «Sky Tower» (9/21) y *Sky Terminal* → «Terminal de Sky Tower», o «Terminal de Sky» si se quiere corto; *Mikado Terminal* → «Terminal de Mikado» se mantiene. Se confirma en el juego.

#### Razas propias de IVA

- **Razas que SMT V no tiene** (battle/NKMSortIndex.tbb#0.N.0, max 15; la columna #0.N.16, max 31, repite lo mismo salvo *Posthuman*/*Superhuman*): *Tree* → «Árbol», *Flight* → «Volador», *Wood* → «Silvano» (alt. «Madera»), *Nymph* → «Ninfa», *Reaper* → «Segador», *Vermin* → «Alimaña», *Spirit* → «Espíritu», *Ghost* → «Fantasma» (sale dos veces, #0.36 y #0.56), *Food* → «Comida», *Zealot* → «Fanático», *Archaic* → «Arcaico», *Cyber* → «Ciber», *King* → «Rey», *Godly* → «Divinal» (alt. «Deífico»; tiene que distinguirse de *Divine* → «Divino» y *Deity* → «Deidad»), *Entity* → «Entidad», *Amatsu* → «Amatsu» (como SMT V deja *Kunitsu*), *Famed* → «Célebre», *Undead* → «No muerto», *Horde* → «Horda», *Samurai* → «Samurái», *Hybrid* → «Híbrido», *Awakened* → «Despertado», *Posthuman* → «Posthumano», *Superhuman* → «Sobrehumano», *Astral* → «Astral», *Godslayer* → «Matadioses» (decidido), *Replicant* → «Replicante». Todas caben en 15 bytes (la más larga, 11). Como etiqueta, la raza no concuerda (*Hada*, *Nocturno*), según el orden raza + nombre de arriba.

#### Grupos y personajes

- `Hunter` (terminólogo, propio de IVA; 714 veces en IVA) → «Cazador», «Cazadora»; *Hunters* → «Cazadores». Sigue a *Hunter Apps* → «apps de cazador» (decidido). En minúscula a media frase (E-59).
- `Hunter Association` (terminólogo, propio de IVA; 106 veces) → «Asociación de Cazadores». Por sede: «Asociación de Cazadores de Ueno»... (quest_center/common/QcName.tbb, max 63: cabe). **No cabe** en map/all/MapNextPointTable.tbb (max 35): *Kinshicho Hunter Association* (#0.14.8) da 37 bytes y *Shinjuku Hunter Association* (#0.21.8), 36. Alternativas para ese campo: «Asoc. de Cazadores de Kinshicho» (31) o «Cazadores de Kinshicho» (22). *Hunter Association HQ* → «Sede de la Asociación de Cazadores» (35/35, justo).
- **Divisiones de los Cazadores** (event/HunterDataBase/HunterDataTable.tbb, columna 54, max 33): *Hunters Management* → «Administración de Cazadores» (28); *Hunters Safety Division* → «División de Seguridad» (22; con «de Cazadores» da 35, **no cabe**); *Hunters Restoral Division* → «División de Rescate» (20); *Hunter Association Intelligence* → «Inteligencia de Cazadores» (25). Los cargos *Nikkari, Hunter* → «Nikkari, cazador»; *John, Engineer* → «John, ingeniero»; *Jiro, Theologian* → «Jiro, teólogo».
- `Samurai` (terminólogo, propio de IVA; 255 veces) → «samurái», plural «samuráis» (RAE), en minúscula a media frase. *Samurai* es invariable en género (*el/la samurái*); el adjetivo concuerda con cada personaje (E-40).
- `Ashura-kai` (terminólogo, propio de IVA; 190 veces) → «Ashura-kai» (*el Ashura-kai*). *Ashura-kai man/woman* → «Hombre/Mujer del Ashura-kai»; *Ashura-kai member* → «Miembro del Ashura-kai»; *Ashura-kai Authorized Shop* → «Tienda oficial del Ashura-kai» (29/31); *Former Ashura-kai Shop* → «Antigua tienda del Ashura-kai».
- `Ring of Gaea` (terminólogo, propio de IVA; 183 veces) → «Anillo de Gea». SMT V escribe *Gea* (*Gaea Rage* ⇒ *Ira de Gea*, ya en la tabla). *Ring of Gaea member* (npc_room/NpcRoomTable.tbb#1.731.38) → «Miembro de Gea» (cambiado el 2026-11-10, ver Secundarias); *Gaea Man/Woman* → «Hombre/Mujer de Gea»; *Male/Female Gaean* (#1.805.38) y *Gaeans* → «Seguidor/Seguidora de Gea», «Seguidores de Gea». Alternativa para *Gaean*: «gaeano», que no existe en español.
- **Facciones y grupos** (event/HunterDataBase/HunterDataTable.tbb, max 37): *Unclean Ones* → «los Impuros»; *Crusaders* → «los Cruzados»; *Angels of Death* → «Ángeles de la Muerte»; *National Defense Divinities* → «Divinidades de Defensa Nacional» (31); *JSDF* → «Fuerzas de Autodefensa» (22), alt. dejar la sigla; *Lucifer's Minions* → «Esbirros de Lucifer»; *Demonstrators* → «Manifestantes»; *Maruo Faction* → «Facción de Maruo».
- **Personajes de IVA** (battle/NKMSortIndex.tbb, event/NpcData.tbb, event/HunterDataBase/HunterDataTable.tbb): nombres propios que se dejan igual: Flynn, Walter, Jonathan, Isabeau, Timothy, Nozomi, Asahi, Gaston, Toki, Hallelujah, Maruo, Tamagami, Fujiwara, Skins, Nikkari, Manabu, Hiroshi, Akira, Ken, Abe, Hugo, Betty, Yuriko, Tayama, Mii, Kei, Tenkai, Michizane, Yamato Takeru, Tokisada, Aramisaki, Lanling Wang, Shesha, Krishna, Vishnu-Flynn, Fusou Fujio, Hiro Jingu, G.H. Hills, K. Con cambio: *Demonic Hugo* → «Hugo demoníaco»; *Dr. Matsuda* → «Dr. Matsuda» (a media frase, *el doctor Matsuda*); *Prisoner Yokota* → «Prisionero Yokota»; *Asahi's dad* → «Papá de Asahi»; *Akira's sister* → «Hermana de Akira»; *Hunter Man/Woman* → «Cazador», «Cazadora»; *Mephistopheles* (event/NpcData.tbb#0.341.0) → «Mefistófeles» (SMT V: *Mephisto* ⇒ *Mefisto*); *En ｎo Ozuno* (#0.339.0, con una *ｎ* de ancho completo) → «En no Ozuno».
- `Liberator`, `Leader`, `Master` (terminólogo, formas de llamar al jugador): *Liberator* (5 veces) → «Libertador»; *Leader* (13) → «Líder»; *Master* (cuando un acompañante le habla al jugador, map/all/PartnerInfoTable.tbb#1.404.36) → «amo». Se confirma con las Negociaciones, que es donde más salen.
- `partner` (terminólogo, propio de IVA; unas 40 veces) → «acompañante», como *Main Partner* → «Acompañante principal» (decidido). *Partners 1/2* (event/HowTo/HowToTable.tbb) → «Acompañantes 1/2».
- **Etiquetas de los habitantes** (npc_room/NpcRoomTable.tbb, columna 38, max 43: 1479 textos, 146 distintos; quest_center/common/NpcHaichiTable.tbb, max 95) (terminólogo, patrón y género): *[Adjetivo] man/woman/boy/girl/fairy/monk/Samurai/Hunter* → «[Sustantivo] [adjetivo]»: *Innocent man* → «Hombre inocente», *Sleepy fairy* → «Hada somnolienta», *Talkative Samurai* → «Samurái parlanchín», *Loud Hunter* → «Cazador ruidoso», *Kind Samurai woman* (#1.216.38) → «Samurái amable» (con *woman* el adjetivo va en femenino; «Mujer samurái amable» si hace falta marcarlo), *Guard angel* → «Ángel guardián». 28 de estas etiquetas son también el nombre de quien habla en los mensajes (*Ashura-kai man* 20 veces, *Ring of Gaea member* 33, *Earthy man* 24): tienen que ser idénticas en la tabla y en el `{F812}` (G-3). Duda de género (E-40): las que el inglés no marca (*Uniformed Hunter*, #1.808.38; *Talkative Samurai*; *Thug*; *Composed teen*) se escriben en masculino solo si sus líneas o el japonés lo confirman; si no, quedan pendientes.

#### Demonios propios de IVA (battle/NKMSortIndex.tbb, max 31)

- **Nombres que se dejan igual** (174): Aniel, Azrael, Kazfiel, Israfel, Victor, Lailah, Hathor, Brigid, Vidofnir, Suparna, Hamsa, Haoma, Kukunochi, Mayahuel, Da Peng, Rukh, Tuofei, Caladrius, Gu Huo Niao, Tangata Manu, Master Therion, Xiuhtecuhtli, Shiwanna, Dis, Vodyanik, Peri, Pales, Alciel, Taotie, Pachacamac, Hresvelgr, Huoniao, Gurr, Itsumade, Moh Shuvuu, Camazotz, Alraune, Zaccoum, Skogsra, Shan Xiao, Hachiman, Inti, Mahamayuri, Ame no Uzume, Ukano Mitama, Kaiming Shou, Kamapua'a, Airavata, Chironnupu, Qing Niuguai, Pabilsag, Apis, Heqet, Heimdall, Jarilo, Nata Taishi, Tam Lin, Ictinike, Demonee-ho, Spriggan, Nadja, Lorelei, Ammut, Hsing-Hsing, Kabuso, Kaso, Stonka, Tlaltecuhtli, Kwancha, Knocker, Pendragon, Orochi, Gui Xian, Nergal, Guedhe, Hel, Ixtab, Cernunnos, Taowu, Catoblepas, Porewit, Raiju, Jueyuan, Chagrin, Girimehkala, Grendel, Wendigo, Lham Dearg, Okiku-Mushi, Ubu, Myrmecolion, Kartikeya, Beiji-Weng, Wu Kong, Tonatiuh, Ares, Xi Wangmu, Asherah, Sedna, Dzelarhons, Pele, Zhu Yin, Illuyanka, Long, Gucumatz, Patrimpas, Makara, Marishiten, Zhong Kui, Oumitsunu, Hitokotonushi, Murmur, Gemori, Dantalian, Orias, Bifrons, Melchom, Shax, Barbatos, Botis, Yomotsu Ikusa, Yamawaro, Momunofu, Yaksha, Bilwis, Yuki Jyorou, Shikome, Strix, Taraka, Maya, Kikimora, Fomorian, Astaroth, Balor, Samyaza, Horkos, Morax, Lucifuge, Ym, Nidhoggr, Mushussu, Kingu, Bai Suzhen, Toubyou, Dybbuk, Vetala, Enku, Churel, Mou-Ryo, Strigoii, Dullahan, David, Kangiten, Futotama, Kanbari, Kuda, Chupacabra, Mamedanuki, Katakirauwa, Tezcatlipoca, Ogun, Rama, Kanseiteikun, Asterius, Aeshma, Sanat, Berserker, Goblin, Medusa, Garrote, Inferno, Erlkonig (la fuente no tiene *ö*), Pyro Jack (como *Jack Frost*), Hairy Jack (alt. «Jack peludo»). *Orochi* solo: SMT V escribe *Yamata no Orochi* entero (la tabla ya tiene *Yamata-no-Orochi*).
- **Nombres con forma española**: *Seraph* → «Serafín» y *Virtue* → «Virtud» (SMT V traduce los coros de ángeles: *Power* ⇒ *Potestad*, *Throne* ⇒ *Trono*, *Dominion* ⇒ *Dominio*, *Principality* ⇒ *Principado*); *Pallas Athena* → «Palas Atenea»; *Persephone* → «Perséfone»; *Prometheus* → «Prometeo»; *Daphne* → «Dafne»; *Arachne* → «Aracne»; *Python* → «Pitón»; *Orcus* → «Orco»; *Titan* → «Titán» (SMT V: *the Titan Geryon* ⇒ *el titán Gerión*); *Hekatoncheires* → «Hecatónquiros»; *Centaur* → «Centauro»; *Minotaur* → «Minotauro»; *Sphinx* → «Esfinge»; *Harpy* → «Arpía»; *Gryphon* → «Grifo»; *Phoenix* → «Fénix»; *Manticore* → «Mantícora»; *Ouroboros* → «Uróboros»; *Demiurge* → «Demiurgo»; *Salamander* → «Salamandra», *Undine* → «Ondina», *Sylph* → «Sílfide», *Gnome* → «Gnomo»; *Dwarf* → «Enano»; *Ogre* → «Ogro»; *Vivian* → «Viviana»; *Jeanne d'Arc* → «Juana de Arco»; *Ghoul* → «Ghoul» (alt. «Gul»); *Zombie* → «Zombi»; *Zombie Cop* → «Policía zombi»; *Samurai Zombie* → «Samurái zombi»; *Corpse* → «Cadáver»; *Patriot* → «Patriota»; *Quicksilver* → «Azogue»; *Ancient of Days* → «Anciano de Días». Con tilde, como SMT V escribe *Quetzalcóatl*: *Tlaloc* → «Tláloc», *Ometeotl* → «Ometéotl», *Tlazolteotl* → «Tlazoltéotl», *Cabracan* → «Cabracán».
- **Nombres que se traducen** (como SMT V hace con *Mad Gasser* ⇒ *Gasero loco* o *Mothman* ⇒ *Hombre polilla*): *Wicker Man* → «Hombre de mimbre»; *Tattooed Man* → «Hombre tatuado»; *Jack the Ripper* → «Jack el Destripador»; *Night Stalker* → «Acechador nocturno»; *Wild Hunt* → «Cacería Salvaje»; *Hooligan* → «Hooligan» (alt. «Vándalo»); *Queen Mab* → «Reina Mab» (SMT V: *Shakespeare's Queen Mab* ⇒ *"La reina Mab" de William Shakespeare*; y *King Frost* ⇒ *Rey Frost*); *Frost Ace* → «As Frost» (como *Rey Frost*; alt. «Frost Ace»); *Frosts* → «Los Frost».
- **Hordas, ejércitos y fuerzas** (patrón): *[X] Horde* → «Horda [de X o adjetivo]»: *Giant* «de gigantes», *Innocent* «inocente», *Oni* «de oni», *Dragon* «de dragones», *Dead* «de muertos», *Wildfire* «incendiaria», *Demon* «de demonios», *Jaki* «de jaki», *Defiant* «rebelde», *Freezing* «gélida», *Gale* «tempestuosa», *Fallen* «de caídos», *Thunder* «del trueno», *Blazing* «ardiente», *Inferno* «infernal», *Blizzard* «de la ventisca», *Tengu* «de tengu», *Pirate* «pirata», *Itsumade*, *Strix*, *Zaccoum* «de Itsumade/Strix/Zaccoum», *Obsessed* «obsesionada», *Greedy* «codiciosa», *Chaos* «del Caos». *[X] Army* → «Ejército [de X]»: *Angel* «de ángeles», *Demon* «de demonios», *Herald* «de Heraldos», *Seraph* «de Serafines», *Metatron* «de Metatrón», *Corpse* «de cadáveres», *Yomi* «de Yomi», *Human* «humano». *[X] Force* → «Fuerza [adjetivo]»: *Azteca* «azteca», *Greek* «griega», *Indian* «india», *Norse* «nórdica». Todas caben en 31 (la más larga, «Ejército de Serafines», 22).
- **Formas y objetos de combate**: *Shesha 1st/2nd Form* → «Shesha (forma 1)», «(forma 2)», como *Brana 2* (la fuente no tiene «ª»); *Michael/Gabriel/Raphael/Uriel/Masakado (Giant)* → «Miguel/Gabriel/Rafael/Uriel/Masakado (gigante)»; *Crucified Flynn* → «Flynn crucificado»; *Inanna Remnant* → «Remanente de Inanna»; *Pillar of Light* → «Pilar de luz»; *Binding Field* → «Campo de contención»; *Warp Hole* → «Agujero de distorsión»; *Orb of the Gates* → «Orbe de las Puertas»; *Portable Cannon* → «Cañón portátil»; *Silhouette Lucif* (#1.1086.0, cortado en el inglés) → «Silueta de Lucifer» (18/31); *Lucifer Hikaru* → «Lucifer Hikaru». Duda: *Charon (Event)* y *Lucifer (2nd Form Normal)* parecen nombres internos; si el jugador los ve, «Caronte (evento)», «Lucifer (forma 2 normal)».
- **Errores del inglés** (§6, se señalan, no se corrigen): *Formorian* (#1.958.0) y *Fomorian*; *Hitokotonuchi* (#1.916.0) y *Hitokotonushi*. Propuesta: una sola forma, «Fomorian» e «Hitokotonushi».
- *Trial Cyber* y *Trial:Single:Sword*... (battle/NKMSortIndex.tbb, 33 textos) (terminólogo, duda): son los blancos de entrenamiento. *Trial Cyber* → «Ciber de prueba» (*Cyber* es la raza); los *Trial:Single:X* parecen internos. Se decide si el jugador los ve.

#### Lugares

- **Distritos y estaciones de Tokio** (map/all/MapYukaTable.tbb, MapNextPointTable.tbb, MapSystemTable.tbb, camp/SortMenuTable.tbb): los nombres japoneses se dejan igual (Ueno, Shinjuku, Ginza, Kinshicho, Kasumigaseki, Tsukiji, Midtown, Minami Sunamachi, Naraku, Kanda-no-yashiro, Tsukiji Konganji, Akihabara, Asakusa, Roppongi...). La parte en inglés se traduce: *Temple* → «Templo X» (*Fudo Temple* → «Templo Fudo», *Zojoji Temple* → «Templo Zojoji»); *Shrine* → «Santuario de X» (*Kanda Shrine*); *Park* → «Parque X» (*Kinshi Park*, *Miyashita Park*); *Station* → «Estación de X» (*Tokyo Station* → «Estación de Tokio»); *Building* → «Edificio X»; *Department Store* → «Almacenes X» (*Tosho*, *Nikoshi*); *Shelter* → «Refugio de X» (*Toyosu*, *Tennozu*); *Camp X* → «Campamento X» (*Ichigaya*, *Meguro*); *X Exit* → «Salida de X» (*Fairy Forest Exit* → «Salida del Bosque de las Hadas», 30/35). *Blasted X* → «X arrasado», *Infernal X* → «X infernal» (*Infernal Kasumigaseki*, camp/SortMenuTable.tbb#0.72.2: 21/21, justo); *Twisted Tokyo* → «Tokio retorcido». Con *Tokyo* → «Tokio» (rows.md): *Tokyo Tower* → «Torre de Tokio», *Tokyo Castle Ruins* → «Ruinas del Castillo de Tokio» (28/31); *Tokyo Dome* y *Dome Stadium* → «Tokyo Dome», «Estadio Dome» (nombre del estadio).
- **Lugares con nombre propio en inglés**: *Sky Tower* → «Sky Tower»; *Reverse Hills* → «Reverse Hills»; *Tir Na Nog* → «Tir Na Nog»; *Cafe Florida* → «Café Florida»; *Akujiki Restaurant* → «Restaurante Akujiki»; *Asakusa Land* → «Asakusa Land».
- **Lugares que se traducen**: *Fairy Forest* → «Bosque de las Hadas» (*Fairy* → «Hada»), *Deep Within Fairy Forest* (map/all/MapNextPointTable.tbb#0.13.8) → «Interior del Bosque de las Hadas» (32/35; «Profundidades del...» da 37, **no cabe**); *Eastern Kingdom of Mikado* → «Reino Oriental de Mikado»; *Mikado Kingdom* → «Reino de Mikado»; *Cosmic Egg* → «Huevo Cósmico» (*Cosmic Egg - Heart* → «Huevo Cósmico: Corazón»); *Yamato Perpetual Reactor* → «Reactor Perpetuo Yamato»; *Tokugawa Mandala* → «Mandala Tokugawa»; *YHVH's Universe* → «Universo de YHVH»; *New Universe* → «Nuevo universo»; *Throne of God* → «Trono de Dios» (*Throne* ⇒ *Trono*); *Diamond Realm* → «Reino de Diamante» (*Diamond* ⇒ *Diamante*); *Chaos Realm* → «Reino del Caos»; *Firmament* → «Firmamento»; *Lucifer Palace* → «Palacio de Lucifer»; *Domain* → «Dominio» (decidido); *Yomotsu Hirasaka* → «Yomotsu Hirasaka»; *Hall of Grief* → «Sala del Pesar»; *Monastery* → «Monasterio»; *Underground - Silver Prison* → «Subterráneo: Prisión de Plata»; *Ginza - Masakado's Rock* → «Ginza: Roca de Masakado»; *Kanda-no-yashiro Ark* → «Arca de Kanda-no-yashiro» (*the Ark* → «el Arca»); *Angel Hazard Zone* → «Zona de peligro angélico»; *National Diet Building* → «Edificio de la Dieta Nacional» (29/31; SMT V: *Tokyo Diet Building* ⇒ *Edificio de la Dieta de Tokio*); *Gakushuin University* → «Universidad Gakushuin»; *Ooi Wharf* → «Muelle de Ooi»; *Central Breakwater* → «Rompeolas central»; *Kiba Storage* → «Almacén de Kiba»; *South Exit Shopping District* → «Zona comercial Salida Sur»; *Ameyoko Way* → «Calle Ameyoko»; *Government Office Plaza* → «Plaza del Gobierno»; *Northern Lake Hill* → «Colina del Lago Norte»; *Metropolitan Highway 5* → «Autopista Metropolitana 5»; *Underground District* → «Distrito subterráneo»; *In Front of the Fountain* → «Frente a la fuente»; *Train Platform* → «Andén»; *No Destination* → «Sin destino»; *St. Nicholas Cathedral* → «Catedral de San Nicolás»; *St. John's Hospital* → «Hospital San Juan»; *Harajuku Police Station* → «Comisaría de Harajuku»; *Aoyama Cemetery* → «Cementerio de Aoyama». **No cabe**: *International Exhibition Center* (map/all/MapYukaTable.tbb#2.102.0 y ms_search_Table.tbb#0.152.0, max 31) da 36 bytes como «Centro Internacional de Exposiciones»: «Centro Int. de Exposiciones» (27). *Freight Company Building* → «Edificio de la empresa de carga» (31/31, justo).
- **Pisos** (map/all/MapNextPointTable.tbb): *B4F* → «S4» y *B4F Laboratory* → «Laboratorio S4», según los pisos provisionales del glosario.
- **Mikado** (mikado/MikadoTable.tbb): *Mikado Castle* → «Castillo de Mikado»; *Castle City* → «Ciudad del Castillo»; *Aquila Statue Plaza* → «Plaza de la Estatua de Aquila» (29/29 en #0.N.2, justo; 29/31 en los demás); *Obelisk Plaza* → «Plaza del Obelisco»; *Castle Interior* → «Interior del castillo»; *Samurai Station* (donde los comandantes samuráis tienen sus despachos) → «Puesto de los Samuráis»; *Barracks* → «Barracones»; *Lake Mikado* → «Lago Mikado»; *Bakery* → «Panadería»; *S's Blacksmith* → «Herrería de S»; *C's Apothecary* → «Botica de C» (como *K's Tavern* → «Taberna de K»); *Firmament Exit* → «Salida al Firmamento»; *Emergency Meeting Ground* → «Punto de reunión de emergencia» (31/31, justo).
- **Tiendas** (shop/ShopTable.tbb, max 31 y 63): *Weapon Shop* → «Tienda de armas»; *Black Market* → «Mercado negro»; *Members-Only Club* → «Club exclusivo»; *Drug Store* → «Farmacia»; las opciones *Buy Weapons/Armor/Items* → «Comprar armas/armaduras/objetos», *Sell Possessions* → «Vender pertenencias»; las categorías *Swords/Guns/Bullets* → «Espadas/Armas de fuego/Balas», *Head/Upper Body/Lower Body/Accessories* → «Cabeza/Torso/Piernas/Accesorios». Puntos de búsqueda (map/all/ms_search_Table.tbb, 159): las marcas parodiadas se dejan (*Uniqlone*, *Hismes*, *Isatan*, *Yodogawa Camera*, *BCD Mart*); lo genérico se traduce, con E-12: *Garbage Can* → «Bote de basura», *Car* → «Auto», *Locker* → «Casillero», *Tech Store* → «Tienda de tecnología», *Men's Shop* → «Tienda para caballeros», *Moto Tech Shop* → «Taller de motos».
- **Ordinales** (camp/SortMenuTable.tbb#0.78-90, max 21) (terminólogo, formato): SMT V escribe *1st* ⇒ *1.°*, y la fuente tiene «°», pero no «ª» ni «º». Propuesta, como *Brana 2*: *1st Passage* → «Pasaje 1», *1st - Entrance* → «Entrada 1», *4th Brane S* → «Brana 4 S». Alternativa para los masculinos: «1.er pasaje».

#### Menús y sistema

- **Comandos de conversación** (battle/UI/BattleComTable.tbb#2.0.1-2.2.1, max 17): *Scout* (*Have a demon join your party*) → «Reclutar» (SMT V: *recruit a demon* ⇒ *reclutar a un demonio*); *Fundraise* (*Have a demon donate funds*) → «Recaudar»; *Trade* (*Bargain with a demon for its item*) → «Trueque». Se usan igual en las apps y en sus ayudas (*the Scout skill* → «la habilidad Reclutar»).
- **Apps de cazador** (item/GauntletAppTable.tbb, 88, max 31; tienen que coincidir con sus menciones, según el glosario): *Fusion Booster 1-7, X* → «Potenciador de fusión 1-7, X» (24); *Demon Enhancer: St/Dx/Ma/Ag/Lu* → «Refuerzo demoníaco: Fu/De/Ma/Ag/Su» (abreviaturas decididas); *Skill Smoother 1-4* (baja el costo de PM) → «Reductor de PM 1-4»; *Summon Discount 1-4* → «Descuento de invocación 1-4»; *Expand Stock 1-16* → «Ampliar hueste 1-16»; *Skill Expansion 1-4* → «Ampliar habilidades 1-4»; *Demon Skill +1-4* → «Habilidad de demonio +1-4»; *Talk EXP Boost 1-4* → «EXP por conversación 1-4»; *HP/MP Recovery 1-2* → «Recuperación de PS/PM 1-2»; *Party HP/MP Recovery* → «Recuperación de PS/PM del grupo» (29); *Scout+*, *Fundraise+*, *Trade+* → «Reclutar+», «Recaudar+», «Trueque+»; *Expert Scout/Fundraiser/Trader* → «Reclutador/Recaudador/Negociante experto»; *Scout Gift/Bonus/Recovery* → «Regalo/Bonificación/Recuperación al reclutar»; *Fundraise/Trade Recovery* → «Recuperación al recaudar», «Recuperación en el trueque»; *Stats/Skill Plugin* → «Módulo de estadísticas/habilidades»; *Skill Augment* (*Makes skills mutate*) → «Mutador de habilidades»; *Gift Augment* → «Mejora de regalos»; *Demon Charmer* → «Encantador de demonios»; *Threatening Aura* → «Aura amenazante»; *Anti-Poison 1-2* → «Antiveneno 1-2»; *Preemptive Smirk Up 1-2* → «Sonrisa preventiva 1-2»; *Mapper* → «Cartógrafo»; *Enemy Match-Up* → «Afinidades del enemigo». Dudas: *ASAP* (#0.38.0, con espacio al final) y *Level Recovery/Level Heal*: las ayudas no están alineadas con los nombres y no dicen qué hacen; se ven en el juego.
- **Dificultades** (camp/ConfigTable.tbb#0.0.30-78, max 11): *Paradise* → «Paraíso» (8), *Skirmish* → «Escaramuza» (10), *Conflict* → «Conflicto» (9), *War* → «Guerra» (6), *Apocalypse* → «Apocalipsis» (11/11, justo). SMT V usa otras (*Safety*, *Casual*, *Hard*).
- **Menú de título** (title/TitleTable.tbb, max 19) (terminólogo, no cabe): *Audio Settings* → «Ajustes de audio» (16; «Configuración de audio», como SMT V dice *Settings*, da 23); *Import SMTIV Save* → «Importar SMTIV» (14; «Importar datos de SMTIV» da 23); *BGM Volume*, *SE Volume*, *Voice Volume* → «Vol. música», «Vol. efectos», «Vol. voces» (12, 12, 10). Lo de SMT V no cabe: *BGM Volume* ⇒ *Volumen de la música de fondo* (30), *SE Volume* ⇒ *Volumen de los efectos* (22), *Voice Volume* ⇒ *Volumen de las voces* (20).
- **Guardar y cargar** (saveLoadUI/SaveLoadUITable.tbb, max 19): *No Data* → «Sin datos» (9); *New Save* → «Nuevos datos» (12). «Nueva partida guardada» da 22, no cabe.
- **Menú de orden** (camp/SortMenuTable.tbb, columna 2, max 21): *Race* → «Raza», *Level* → «Nivel», *Alphabetic* → «Alfabético» (SMT V: *Sort by alphabetical order* ⇒ *Ordena por orden alfabético*), *Price* → «Precio», *MP Cost* → «Costo de PM», *Macca Cost* → «Costo de macca», *Skill Type* → «Tipo de habilidad», *Item Type* → «Tipo de objeto», *New Product* → «Novedad» (SMT V: *By New* ⇒ *Por novedad*), *Unregistered* → «Sin registrar», *Allies* → «Aliados». Afinidades: *[Elemento] Type* → «Tipo [elemento]»: «Tipo físico», «Tipo disparo», «Tipo fuego», «Tipo hielo», «Tipo eléctrico», «Tipo choque», «Tipo luz», «Tipo oscuridad», «Tipo elemental». Estadísticas: *STR/DEX/MAG/AGI/LUC* → «FUE/DES/MAG/AGI/SUE» (SMT V: *Str* ⇒ *Fue*; *Dexterity* → «Destreza» y *Luck* → «Suerte» ya están en la tabla). *Press OK to switch between ascending and descending* (50 textos) → «Presiona OK para alternar entre orden ascendente y descendente.»; duda: si *OK* es un botón de la consola, va su nombre.
- **Búsqueda de fusión** (unite/SearchTable.tbb, max 55-59): *Search Conditions* → «Condiciones de búsqueda»; *Demon to Include/Exclude* → «Demonio que incluir/excluir»; *Include Compendium* → «Incluir el compendio»; *New Demons Only* → «Solo demonios nuevos»; *Use Compendium Ticket* → «Usar vale del compendio»; *Exclude Element Race* → «Excluir Elementales»; *Top 10* → «Los 10 mejores»; *More*, *Even More* → «Más», «Aún más»; *Demon Level* → «Nivel del demonio»; *Skill Type* → «Tipo de habilidad»; *Skill Name* → «Nombre de habilidad»; *Locked Fusions* → «Fusiones bloqueadas».
- **Tutoriales** (event/HowTo/HowToTable.tbb, max 39): *Smirking* → «Sonrisa maliciosa» (decidido); *Demon Whispers* → «Susurros de demonios» (*whisper* → «susurrar», decidido); *Assist Attacks* → «Ataques de apoyo»; *Double Party* → «Grupo doble»; *Traps* → «Trampas»; *Mapper 1/2* → «Cartógrafo 1/2», como la app.
- *Godslayer Training* (terminólogo, propio de IVA) → «Entrenamiento de Matadioses». *Exchange DDS Cards* → «Intercambiar tarjetas DDS».

#### Objetos (item/ItemTable.tbb, max 31)

- **Reliquias por estrellas** (#3.0-54.0, 55): *N-Star [X]* → «[X] de N estrellas», en singular para 1: «Artilugio de 1 estrella», «... de 5 estrellas». *Gadget* «Artilugio», *Leisure* «Ocio», *Food* «Comida», *Furniture* «Mueble», *Cosmetics* «Cosmético», *Commodity* «Mercancía», *Fragrance* «Fragancia», *Document* «Documento», *Medicine* «Medicina» (*Medicine* ⇒ *Medicina*), *Clothing* «Ropa», *Black Material* «Material negro» (29, el más largo).
- **Inciensos** (#1.30-34.0, #6.1-7.0): *St/Ma/Dx/Ag/Lu Incense* → «Incienso de Fu/Ma/De/Ag/Su», *(Small)* → «(pequeño)», *HP/MP Incense* → «Incienso de PS/PM». SMT V: *Strength Incense* ⇒ *Incienso de fuerza*.
- **Piedras** (#1.15-56.0, #6.8-15.0): *[Habilidad] Stone* → «Piedra [habilidad]» (*Agi Stone* → «Piedra Agi»), por *Life Stone* ⇒ *Piedra vital*. *Summon Stone* → «Piedra de invocación», *Destiny Stone* → «Piedra del destino».
- **Otros consumibles**: *[Elemento] Battle Plans* (#6.25-36.0) → «Plan de batalla: [elemento]» (*Almighty* da 29); *Ailment Battle Plans* → «Plan de batalla: estados» (24; «estado alterado» da 32, **no cabe**); *Blade/Gun/Armor Boost Kit* → «Kit de mejora de espada/arma/armadura»; *5/10/20-Point Card* → «Tarjeta de 5/10/20 puntos»; *Balm of Rising* → «Bálsamo del renacer»; *Detox Solution* → «Solución desintoxicante»; *Expanse Meat* → «Carne del Cielo» (*Expanse* → «Inmensidad», decidido en Datos; el nombre largo no cabe: ver PENDING); *A5 Demoloin* (#1.59.0; *demon* + *sirloin*) → delicadas (E-23), provisional «Demolomo A5».
- **Accesorios** (patrón): *Earring* → «Arete» (E-12: no *pendiente*): *Red Earring* → «Arete rojo»; *Bracelet* → «Pulsera»: *Sage Bracelet* → «Pulsera del sabio», *Master Bracelet* → «Pulsera del maestro», *Wise King Bracelet* → «Pulsera del rey sabio», *Warlord Bracelet* → «Pulsera del caudillo» (20; «Brazalete de señor de la guerra» da 32, **no cabe**); *Ring* → «Anillo», *Rosary* → «Rosario», *Soul* → «Alma» (*Heated Soul* → «Alma ardiente»).
- **Munición** (patrón): *[X] Rounds* → «Balas [X]» (*Panic Rounds* → «Balas de pánico», *Flaemis Rounds* → «Balas Flaemis», *Zeus Rounds* → «Balas de Zeus»); *Shot* → «Disparo [X]»; *Hollow-Points* → «Balas de punta hueca».
- **Trajes** (#2.240-358.0, cada uno tres veces: cabeza, torso y piernas): *[Color] [Estilo]* → «[Estilo] [color]», con el color invariable: *Blue Agent* → «Agente azul», *Crimson Ninja* → «Ninja carmesí», *Officer Gray* → «Oficial gris», *Hero Red* → «Héroe rojo», *Military Green* → «Militar verde», *Navy Marine* → «Marine azul marino», *Gray Stealth* → «Sigilo gris», *Gold Jinbaori* → «Jinbaori dorado», *Yellow Hazmat* → «Traje de protección amarillo», *Gray Power Suit* → «Servoarmadura gris», *Blue-Orange Combat* → «Combate azul-naranja», *Bare Chest Purple* → «Torso desnudo morado», *Black Demonica* → «Demonica negro», *Dark/Verdant Goth* → «Gótico oscuro/verdoso», *Wonderland Goth* (#2.272.0) → «Gótico de fantasía» (20; «Gótico del País de las Maravillas» da 35, **no cabe**). Con nombre: *Hunter Suit* → «Traje de cazador», *Samurai Uniform* → «Uniforme de samurái», *Superior Samurai Suit* → «Traje de samurái superior», *Garment of Hope* → «Prenda de la esperanza», *Wings of Order* → «Alas del Orden», *Horns of Chaos* → «Cuernos del Caos», *Ulster Armor* → «Armadura del Úlster». *Skins* (personaje) no tiene que ver con los trajes.
- **Armas** (#2.0-239.0): los nombres propios se dejan (*Masamune*, *Kotetsu*, *Mjolnir*, *Laevateinn*, *Ame-no-habakiri*, *Ame-no-murakumo*, *Gae Bolg*, *Brionac*, *Longinus*, y los modelos: *MP9 Machinegun*, *AR-33*); lo descriptivo se traduce: *Steel Bazooka* → «Bazuca de acero», *.50 Heavy Revolver* → «Revólver pesado .50», *Magic Spear of Vigor* → «Lanza mágica del vigor», *Headhunter* → «Cazacabezas», *Unnamed Sword* → «Espada sin nombre», *Spear of Michael* → «Lanza de Miguel» (*Michael* ⇒ *Miguel*), *Masakado's Katana* → «Katana de Masakado».
- **Objetos clave que se repiten**: *Shesha Radar* → «Radar de Shesha»; *Fake Gauntlet* → «Guantelete falso»; *Supplies* → «Suministros»; *Medical Supplies* → «Suministros médicos»; *Kasumigaseki Keycard A/B* (#0.61.0) → «Llave de Kasumigaseki A/B» (23; «Tarjeta llave de Kasumigaseki A» da 31/31, justo); *Futotama-gushi* → «Futotama-gushi»; *Yen Coin*, *Yen Bill* → «Moneda de yen», «Billete de yen».

### Datos

Filas *oficial* (G-1) de la sección Datos (item/ItemHelpMess.mbm, battle/SkillHelpMess.mbm, status/profile.mbm, event/HunterDataBase/). Salen de `system-terms-datos.tsv`, de `glossary-candidates.tsv` y de términos que la sección repite en minúscula. No repiten las filas que GLOSSARY.md ya tiene. Las cifras son textos de la sección (3001).

#### Términos de sistema (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Pierce | perforar | SMT V (ejemplos: *All attacks will Pierce!* ⇒ *¡Todos los ataques perforan!*; *adds Pierce effect* ⇒ *añade el efecto Perforación*) | El efecto que atraviesa la resistencia de la afinidad (38 textos: *Effect: Pierce*, *Smirking: Pierce*). Sustantivo: *Effect: Pierce* → «Efecto: perforación». Ya en la Interfaz: *It pierced through the resistance!* → «¡Atravesó la resistencia!» (battle/Common/common.mbm#37). |
| pierce | perforar | SMT V (como *Pierce*) | *Fire attacks pierce until end of your turn*, *adds pierce to all attacks* (15 textos). |
| Instant kill | muerte instantánea | SMT V (ejemplo: *Chance of instakill* ⇒ *Posibilidad de muerte instantánea*) | SMT V escribe *instakill*; IVA, *Instant kill* (*Smirking: Instant kill*, 23 textos). Ya en la Interfaz: «¡Se activó la muerte instantánea!» (battle/Common/common.mbm#32). |
| instant kill | muerte instantánea | SMT V (como *Instant kill*) | *Instant kill attack* (5 textos). *Instant kills sleeping targets* (SkillHelpMess#148) usa el verbo: el validador avisará ahí si va «mata al instante». |
| critical | crítico | SMT V (ejemplo: *High chance of landing Critical hits* ⇒ *Alta probabilidad de asestar golpes críticos*) | *critical hit* → «golpe crítico»; *High critical/low hit rate* (12 textos). |
| Critical | crítico | SMT V (como *critical*) | *Effect: Critical rate up* (item/ItemHelpMess.mbm#755). |
| buffs | efectos positivos | SMT V (ejemplo: *All buffs have faded!* ⇒ *¡Se han desvanecido todos los efectos positivos!*) | *Removes status buffs* (9 textos). En la Interfaz quedó «mejoras»: ver pending.md. |
| debuffs | efectos negativos | SMT V (ejemplo: *All stat debuffs faded!* ⇒ *¡Se desvanecen todos los efectos negativos!*) | *Removes status debuffs* (4 textos). |
| Attack down | Ataque disminuido | SMT V (estado *Attack Down* ⇒ *Ataque disminuido*) | *Effect: Attack down* (SkillHelpMess#169, #238, #245). |
| Defense down | Defensa disminuida | SMT V (estado *Defense Down* ⇒ *Defensa disminuida*) | *Smirking: Defense down*, *Effect: Defense down* (6 textos). |
| defense down | defensa disminuida | SMT V (como *Defense down*) | *Effect: Pierce, defense down* (SkillHelpMess#234). |
| Stats down | estadísticas disminuidas | SMT V (ejemplo: *All stats down!* ⇒ *¡Todas las estadísticas disminuidas!*) | *Smirking: Stats down*, *Effect: Stats down* (SkillHelpMess#41, #126, #391). |
| max HP | PS máximos | SMT V (etiqueta *MAX HP* ⇒ *PS MÁX.*) | *Increases max HP* (4 textos). En las frases, «PS máximos»; la abreviatura *MÁX.* es la de las etiquetas de SMT V. |
| maximum HP | PS máximos | SMT V (como *max HP*) | *Slightly increases maximum HP* (4 textos). |
| max MP | PM máximos | SMT V (etiqueta *MAX MP* ⇒ *PM MÁX.*) | Igual que *max HP* (4 textos). |
| maximum MP | PM máximos | SMT V (como *max MP*) | 3 textos. |
| All allies | Todos los aliados | SMT V (etiqueta *all allies* ⇒ *todos los aliados*) | *Target: All allies* (item/ItemHelpMess.mbm#1991-1993). |

Fuerza de los ataques (SMT V, SkillHelpMess e ItemHelpMess): *Weak* → «débil» (*Weak   attack to* ⇒ *Ataque débil de tipo*), *Medium* → «medio» (⇒ *Ataque medio de tipo*), *Heavy* → «intenso» (⇒ *Ataque intenso de tipo*; 25 de 36 veces, las demás *fuerte*), *Severe* → «extremo» (⇒ *Ataque extremo de tipo*). En IVA: *Weak/Medium/Heavy/Severe <elemento> attack* y *1-4 medium attacks* (unos 200 textos). *Weak* es también la debilidad de una afinidad (*Weak against Phys*, *Weak to Sick*): «débil», como SMT V (*when striking weakness* ⇒ *al aprovechar una debilidad*). No van en la tabla porque *Heavy* es *pesado* en nombres de objetos ya traducidos (*Heavy Grimoire* → «Grimorio denso», *.50 Heavy Revolver* → «Revólver pesado .50», item/ItemTable.tbb#1.11.0, #2.155.0) y el validador avisaría de más.

#### Mitología de los perfiles (oficiales)

SMT V los nombra en sus perfiles con el mismo sentido (la misma figura, lugar, grupo u obra). Todos salen en status/profile.mbm.

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Goetia | Goecia | SMT V (ejemplo: *One of the 72 demons of the "Ars Goetia."* ⇒ *Uno de los 72 demonios de la Goecia.*) | El grimorio de los 72 demonios (13 textos: *One of the 72 demons of the Goetia*). En femenino: *la Goecia*. |
| Izanagi | Izanagi | SMT V (ejemplo: *The three gods born from Izanagi* ⇒ *los tres dioses nacidos de Izanagi*) | Dios japonés (9 textos). SMT V escribe una vez *Izangi*, por error. |
| Yomi | Yomi | SMT V (ejemplo: *in Yomi, the land of the dead* ⇒ *en Yomi, la tierra de los muertos*) | La tierra de los muertos de la mitología japonesa (5 textos; también *Yomi no Kuni*). |
| Buddha | Buda | SMT V (ejemplo: *he sent his daughters to tempt Buddha* ⇒ *envió a sus hijas a tentar a Buda*) | 7 textos. *Mitra-Buddha* → «Mitra-Buda» ya está decidido. No confundir con *Budha*, la deidad del planeta (item/ItemHelpMess.mbm#852; *Budha Pillar* → «Pilar de Budha», item/ItemTable.tbb#0.21.0), que se deja igual. |
| Moirae Sisters | Moiras | SMT V (ejemplo: *One of the three Moirae Sisters in Greek mythology* ⇒ *Una de las tres Moiras de la mitología griega*) | Las diosas griegas del destino (3 textos). SMT V no traduce *Sisters*. |
| Ssu-Ling | Ssu-Ling | SMT V (ejemplo: *One of the Ssu-Ling, celestial creatures in Chinese mythology* ⇒ *Uno de los Ssu-Ling, criaturas celestiales de la mitología china*) | Las cuatro bestias celestiales chinas (3 textos). |
| Grigori | Grigori | SMT V (ejemplo: *A leader of the Grigori* ⇒ *Líder de los Grigori*) | Grupo de ángeles (2 textos). |
| Kojiki | Kojiki | SMT V (ejemplo: *written about in the Kojiki* ⇒ *sobre la que se escribe en el Kojiki*) | Crónica japonesa (3 textos). |
| King Solomon | rey Salomón | SMT V (ejemplo: *invoked by King Solomon* ⇒ *invocados por el rey Salomón*) | 2 textos. |
| Ahura Mazda | Ahura Mazda | SMT V (ejemplo: *humanity's cry for Ahura Mazda* ⇒ *la llamada de la humanidad a Ahura Mazda*) | Dios zoroástrico (2 textos). |
| Bael | Bael | SMT V (ejemplo: *such as Bael, Beelzebub, Belphegor* ⇒ *como Bael, Belcebú, Belfegor*) | Demonio derivado de Baal (2 textos). |
| Asgard | Asgard | SMT V (ejemplo: *the father and son of Asgard* ⇒ *el padre y el hijo de Asgard*) | El reino de los dioses nórdicos (2 textos). |
| Valhalla | Valhalla | SMT V (ejemplo: *to take to Valhalla* ⇒ *para llevarlos al Valhalla*) | En masculino: *el Valhalla* (1 texto en Datos, 5 en IVA). |
| Typhon | Tifón | SMT V (ejemplo: *It was born from Typhon, the Giant of Wind* ⇒ *Es hijo de Tifón, el gigante del viento*) | Monstruo griego (2 textos). |
| Uranus | Urano | SMT V (ejemplo: *Giants born from Uranus and Gaia* ⇒ *Gigantes nacidos de Urano y Gaia*) | Dios griego (2 textos). |
| Gaia | Gaia | SMT V (como *Uranus*) | La diosa griega (2 textos). No es la *Gea* de *Ring of Gaea* (decidido). Un perfil la escribe *Gaea*: ver pending.md. |
| Hercules | Hércules | SMT V (ejemplo: *one of the 12 great Labors of Hercules* ⇒ *uno de los doce trabajos de Hércules*) | No *Heracles* (2 textos). |
| Hades | Hades | SMT V (ejemplo: *The guardian hound of Hades* ⇒ *El sabueso guardián del Hades*) | El inframundo griego, en masculino: *el Hades* (3 textos). |
| Venus | Venus | SMT V (ejemplo: *the planet Venus* ⇒ *el planeta Venus*) | La diosa y el planeta (4 textos). |
| Adam | Adán | SMT V (ejemplo: *the creation of Adam and Eve* ⇒ *la creación de Adán y Eva*) | 3 textos. |
| Eve | Eva | SMT V (como *Adam*) | 3 textos. |
| Bible | Biblia | SMT V (ejemplo: *a high-ranking demon in the Bible* ⇒ *Según la Biblia, es un demonio de alto rango*) | 2 textos. |
| Ramayana | Ramayana | SMT V (ejemplo: *In the Ramayana* ⇒ *Según el Ramayana*) | Epopeya hindú (2 textos). |
| Fujiwara no Chikata | Fujiwara no Chikata | SMT V (ejemplo: *the four oni controlled by Fujiwara no Chikata* ⇒ *los cuatro oni controlados por Fujiwara no Chikata*) | Figura histórica japonesa (4 textos). No es el personaje *Fujiwara* de IVA. |
| Lord of the Flies | Señor de las Moscas | SMT V (ejemplo: *Lord of the Flies and the Prince of Hell* ⇒ *Señor de las Moscas y príncipe del infierno*) | Epíteto de un demonio (status/profile.mbm#485). |
| Lady of Heaven | Dama del Cielo | SMT V (ejemplo: *Her name means "Lady of Heaven"* ⇒ *Su nombre significa "Dama del Cielo"*) | Epíteto de una diosa (status/profile.mbm#368). |
| A Midsummer Night’s Dream | El sueño de una noche de verano | SMT V (ejemplo: *in William Shakespeare's "A Midsummer Night's Dream."* ⇒ *en "El sueño de una noche de verano" de William Shakespeare*) | La comedia de Shakespeare (status/profile.mbm#234). |
| Gae Bolg | Gae Bolg | SMT V (ejemplo: *he received the legendary Gae Bolg* ⇒ *le dio la legendaria Gae Bolg*) | La lanza de Cú Chulainn (status/profile.mbm#37, #221; en Tablas, el arma, item/ItemTable.tbb#2.92.0). En femenino, como SMT V: *la Gae Bolg*. |

#### Decididos por el usuario: Datos

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Four Heavenly Kings | Cuatro Reyes Celestiales | Decidido 2026-11-09 (G-2) | El grupo de deidades budistas, como los perfiles de SMT V. |
| Gungnir | Gungnir | Decidido 2026-11-09 (G-2) | La lanza de Odín. |
| Ragnarok | Ragnarok | Decidido 2026-11-09 (G-2) | Con artículo: *el Ragnarok*. |
| Wheel of Fortune | rueda de la fortuna | Decidido 2026-11-09 (G-2) | Como el perfil de SMT V, en minúscula. *Fortune* sola no se fija. |
| Universe Ring | anillo del universo | Decidido 2026-11-09 (G-2) | El arma de Qiankun Quan, como el perfil de SMT V. |
| Expanse | Inmensidad | Decidido 2026-11-09 (G-2) | El lugar de donde vienen los demonios: *la Inmensidad*. *Expanse Meat* sigue «Carne del Cielo», porque «Carne de la Inmensidad» no cabe en su columna (PENDING). |
| Ceiling | Techo | Decidido 2026-11-09 (G-2) | La bóveda de roca que cubre Tokio: *el Techo*. |
| God’s Plan | Plan de Dios | Decidido 2026-11-09 (G-2) | *el Plan de Dios*. |
| God's Plan | Plan de Dios | Decidido 2026-11-09 (G-2) | Variante con apóstrofo recto. |
| Panic | Pánico | Decidido 2026-11-09 (G-2) | Estado alterado; con mayúscula, como SMT V con sus estados (*Inflige Pánico*). |
| Bind | Atadura | Decidido 2026-11-09 (G-2) | Estado alterado, como *Bind Rounds* → «Balas de atadura». |
| Mute | Silencio | Decidido 2026-11-09 (G-2) | Estado alterado, como *Mute Shot* → «Disparo de silencio». |
| Daze | Mareo | Decidido 2026-11-09 (G-2) | Estado alterado, como la Interfaz (*tiene mareos*). |
| Sick | Enfermedad | Decidido 2026-11-09 (G-2) | Estado alterado; *Weak to Sick* → «Débil contra Enfermedad». |
| KO | K.O. | Decidido 2026-11-09 (G-2) | *Revive del K.O. con la mitad de los PS*. |
| Selling Relic | Reliquia para vender | Decidido 2026-11-09 (G-2) | Texto genérico de objetos (302 veces). |
| Relic from beneath Tokyo | Reliquia hallada bajo Tokio | Decidido 2026-11-09 (G-2) | Texto genérico de objetos (145 veces). |
| Sneak Attack | Ataque sigiloso | Decidido 2026-11-09 (G-2) | Como el título *Sneak Attacker* → «Atacante sigiloso». |
| Hunter Database | Base de datos de cazadores | Decidido 2026-11-09 (G-2) | |
| Shogunate | shogunato | Decidido 2026-11-09 (G-2) | *el shogunato*. |
| female demon | demonio femenino | Decidido 2026-11-09 (G-2) | Solo cuando el inglés lo especifica. *demon* a secas es «el demonio» aunque sea mujer (*A demon… She…* → «Un demonio…»). Nunca «demonia» ni «la demonio». |
| demoness | (según la línea) | Decidido 2026-11-09 (G-2) | No es solo *female demon*: pasa por delicadas en cada caso. Nunca «demonia» ni «la demonio». Ejemplos: las Shikome → «mujeres demonio» (#454); *the demoness Lilith* → «Lilit, el demonio femenino que…» (#471). |

*Lost* → «Perdido» y *Brand* → «Marca» (provisional) también están decididos, pero no van en la tabla: con mayúscula, *Lost* también abre frases (*Lost {cantidad} Macca.*, battle/ResultMsg.mbm#16) y *Brand* se comprueba en el juego.

#### Patrones de Datos (decididos 2026-11-09)

Propuestas del terminólogo aprobadas por el usuario. *Limit* y *Brand* son provisionales: se comprueban en el juego.

#### Pendientes anteriores que aparecen en Datos

- `Four Heavenly Kings` (terminólogo, otro sentido): «he is the strongest of the Four Heavenly Kings» (status/profile.mbm#395, #396, #398, #399; 4 veces) → «Cuatro Reyes Celestiales», y se puede fijar como oficial. En Datos es siempre el grupo de deidades budistas, y SMT V lo nombra igual en sus perfiles: *one of the Four Heavenly Kings in Buddhist mythology* ⇒ *uno de los Cuatro Reyes Celestiales de la mitología budista*.
- `Gungnir` (terminólogo, otro sentido): «bearing his spear Gungnir and wearing his ring Draupnir» (status/profile.mbm#168) → «Gungnir», y se puede fijar como oficial. Es la lanza de Odín, como en el perfil de SMT V: *armed with both Gungnir, his mighty spear* ⇒ *armado con Gungnir, su poderosa lanza*.
- `Ragnarok` (terminólogo, otro sentido): «It is said that it will live through Ragnarok.» (status/profile.mbm#60; 10 veces en Datos) → «el Ragnarok», y se puede fijar como oficial. Los perfiles de SMT V lo usan con el mismo sentido y con artículo: *In Ragnarok, he will set the world ablaze* ⇒ *incendiará el mundo durante el Ragnarok*.
- `Universe Ring` (terminólogo, otro sentido): «Qiankun Quan (Universe Ring)» (status/profile.mbm#225) → «anillo del universo». Cambia la propuesta anterior («Anillo universal», el nombre de la habilidad): el perfil de SMT V de la misma figura dice *his trusty weapon Qiankun Quan (Universe Ring)* ⇒ *su fiel arma Qiankun Quan (anillo del universo)*.
- `Walpurgisnacht` (terminólogo, otro sentido): «Bilwis appears on Walpurgisnacht» (status/profile.mbm#444) → «la noche de Walpurgis», sin cambio. SMT V solo lo tiene como habilidad.
- `Mother Earth` (terminólogo, otro sentido): «A Mother Earth goddess of Japanese lore» (status/profile.mbm#43) → «una diosa madre de la tierra», sin cambio; no se fija. Los perfiles de SMT V usan *Madre Tierra* para el significado de un nombre (*Her name means "Mother Earth"* ⇒ *Su nombre significa "Madre Tierra"*) y *diosa madre* para *mother goddess*.
- `Fortune` (terminólogo, otro sentido): «she turns the Wheel of Fortune» (status/profile.mbm#40), «one of the Seven Gods of Fortune» (#395) → «la rueda de la fortuna», «los Siete Dioses de la Fortuna». *Fortune* sola no se fija. *Wheel of Fortune* sí se puede fijar como oficial: el perfil de SMT V de la misma diosa dice *she spins the Wheel of Fortune* ⇒ *hace girar la rueda de la fortuna*, en minúscula.
- `Resist Fire` (terminólogo, otro sentido): «Resist Fire/Ice/Elec/Force / Weak against Phys/Gun/Light/Dark» (item/ItemHelpMess.mbm#467) → «Resiste fuego/hielo/electricidad/choque / Débil contra físico/disparo/luz/oscuridad», sin cambio salvo la segunda línea. Las afinidades salen de la tabla (*Resist* → «Resistir», *Force* → «Choque», *Gun* → «Disparo»), y *Weak* → «débil» es la de SMT V (rows.md).
- `Lady`, `Lord` (GLOSSARY, Tablas: los tratamientos «se deciden juntos»; no está en PENDING.md): en Datos no hay tratamientos, solo epítetos: «also known as the ”Lady of the Lake.”» (status/profile.mbm#236) → «la Dama del Lago»; «Her name means ”Lady of Heaven”» (#368) → «Dama del Cielo» (SMT V, rows.md); «Lord of the Flies» (#485) → «Señor de las Moscas» (SMT V, rows.md); «his name means ”Lord.”» (#167) → «"Señor"». Nada de esto cambia lo que hay que decidir sobre los tratamientos.
- `Expanse` (GLOSSARY, Tablas: «duda: hay que ver si es el Firmamento»): «After the incident with the Yamato Perpetual Reactor in which a gate to the Expanse was created, the demon population surged.» (event/HunterDataBase/HunterDataBase.mbm#100; también #110) → «la Inmensidad». Datos muestra que es un lugar, con el que se abrió una puerta por la que llegaron demonios; no es el cielo. En otras secciones los demonios hablan de él como de su tierra (*One of my pals in the Expanse*, *the Expanse hotline*). *Firmamento* y el «Carne del Cielo» ya traducido (item/ItemTable.tbb#1.57.0, *Expanse Meat*) se leen como el cielo. «la Inmensidad» conserva la imagen del inglés (*expanse*, extensión inmensa); si se fija, *Expanse Meat* → «Carne de la Inmensidad». Decidido: «la Inmensidad». *Expanse Meat* → «Carne de la Inmensidad» no cabe en su columna: ver PENDING.

#### Estados alterados propios de IVA

SMT V no los tiene (sus estados son *Poison*, *Confusion*, *Charm*, *Seal*, *Sleep*, *Mud*, *Shroud*, *Mirage*). *Poison*, *Sleep* y *Charm* ya están en la tabla. SMT V escribe el nombre del estado con mayúscula en las descripciones (*Chance of inflicting Mud* ⇒ *Puede infligir Barro*; *afflicted with Sleep* ⇒ *sufre Sueño*); se propone lo mismo.

- `Panic` (terminólogo, propio de IVA): «Medium <elemento> attack. Inflicts Panic» (battle/SkillHelpMess.mbm#42; 24 veces) → «Pánico». Ya traducido así en *Panic Rounds* → «Balas de pánico» (item/ItemTable.tbb#2.738.0).
- `Bind` (terminólogo, propio de IVA): «Inflicts the Bind ailment» (battle/SkillHelpMess.mbm#63; 23 veces) → «Atadura», como *Bind Rounds* → «Balas de atadura» (item/ItemTable.tbb#2.739.0).
- `Mute` (terminólogo, propio de IVA): «Inflicts the Mute ailment» (battle/SkillHelpMess.mbm#99; 13 veces) → «Silencio», como *Mute Shot* → «Disparo de silencio» (item/ItemTable.tbb#2.767.0). La Interfaz dice el efecto con *sellar*: *Skills are sealed!* → «¡Las habilidades están selladas!» (battle/Common/common.mbm#49). SMT V tiene un estado parecido, *Seal* ⇒ *Sello*, pero IVA lo llama *Mute*.
- `Daze` (terminólogo, propio de IVA): «2-4 medium <elemento> attacks. Inflicts Daze» (battle/SkillHelpMess.mbm#173; 18 veces) → «Mareo», como la Interfaz: *is dizzy.* → «tiene mareos.» (battle/Common/common.mbm#38).
- `Sick` (terminólogo, propio de IVA): «Inflicts the Sick ailment» (battle/SkillHelpMess.mbm#67; 13 veces) → «Enfermedad», como la Interfaz: *fell ill!* → «¡enfermó!» (battle/Common/common.mbm#28). *Weak to Sick* (item/ItemHelpMess.mbm#735) → «Débil contra Enfermedad».
- `Lost` (terminólogo, propio de IVA): «Weak <elemento> attack. Inflicts Lost» (battle/SkillHelpMess.mbm#172; 4 veces), «Prevents demons from becoming Lost» (#456) → «Perdido». El estado de un demonio que sale del grupo. Las Tablas lo dejaron en inglés: *Lost Status* → «Estado Lost» (event/HowTo/HowToTable.tbb#0.15.4); si se fija «Perdido», ese texto pasa a «Estado Perdido». Decidido: «Perdido», y *Lost Status* → «Estado Perdido».
- `Brand` (terminólogo, duda): «Severe <elemento> attack. Inflicts Brand» (battle/SkillHelpMess.mbm#384), «Effect: Brand» (#91, #147, #301; 4 veces) → «Marca», como la habilidad de SMT V *Hellish Brand* ⇒ *Marca infernal*. Ningún texto de Datos dice qué hace; se comprueba en el juego.
- `KO` (terminólogo, propio de IVA): «Revives from KO with half HP» (battle/SkillHelpMess.mbm#93; 10 veces) → «K.O.» (*Revive del K.O. con la mitad de los PS*). SMT V llama a ese estado *Incapacitated* ⇒ *Incapacitación*, otra palabra. Decidido: «K.O.».

#### Etiquetas de las descripciones

Lo fijo de item/ItemHelpMess.mbm y battle/SkillHelpMess.mbm. SMT V no tiene estas etiquetas: sus descripciones son frases (*Weak Fire attack to 1 foe*).

- **Etiquetas** (terminólogo, propio de IVA): *Target:* (732 veces) → «Objetivo:», como la Interfaz (battle/BattleUI.mbm#0); *Target: None* → «Objetivo: ninguno». *Effect:* (344) → «Efecto:», como el menú de orden (camp/SortMenuTable.tbb#0.15.2). *Type:* (120) → «Tipo:» (camp/SortMenuTable.tbb#0.31.2). *Condition:* → «Condición:»; *Trigger:* → «Activación:»; *Chance:* → «Probabilidad:»; *Note:* → «Nota:» (1-4 veces cada una). *Infinite uses* → «Usos ilimitados». *Current AP: / After use:* (item/ItemHelpMess.mbm#19, #24, #1973) → «PA actuales: / Tras usarlo:» (*App Points* → «puntos de app», *AP* → «PA», decidido).
- `Limit` (terminólogo, duda): «Target: <código>. Limit: <código>» (item/ItemHelpMess.mbm#1; 100 veces) → «Límite:». El valor lo pone el juego y no sale en los textos: no se sabe si es la cantidad que se puede llevar o dónde se usa. *Infinite uses, Limit: <código>* (#1974) descarta que sea la cantidad de usos. Se comprueba en el juego.
- `Power` (terminólogo, otro sentido): «Power: <código> x<código> hit(s)» (item/ItemHelpMess.mbm#181; 290 veces) → «Potencia: <código> x<código> golpe(s)». Es el poder de un arma, no el demonio (*Potestad*); GLOSSARY ya dice que *Power* no es término fijo. *hit(s)* (240) → «golpe(s)»; *Hit%: Low* (15) → «Precisión: baja», por *Hit/evade rate* → «Precisión/evasión» (decidido).
- **Tipos de arma** (terminólogo, propio de IVA): *Type: Dagger/Sword/Spear/Blunt* (item/ItemHelpMess.mbm#61, #62, #146, #69; 120 veces) → «Tipo: daga/espada/lanza/contundente», como la tienda (*Swords* → «Espadas», shop/ShopTable.tbb#0.4.0).
- `Smirking` (terminólogo, decidido): «Heavy <elemento> attack. Smirking: Instant kill» (battle/SkillHelpMess.mbm#50; 38 veces) → «Sonrisa maliciosa: muerte instantánea». Sigue lo decidido (*Smirking* → «Sonrisa maliciosa», *Smirk* → «Sonrisa maliciosa»): *Induces Smirk* → «Provoca sonrisa maliciosa», *Removes Smirk* → «Quita la sonrisa maliciosa». Solo falta confirmar que la etiqueta va igual en las descripciones.
- **Textos genéricos de objetos** (terminólogo, propio de IVA; son textos completos que se repiten): *Selling Relic* (item/ItemHelpMess.mbm#1649; 302 veces) → «Reliquia para vender»; *Relic from beneath Tokyo* (#956; 145) → «Reliquia hallada bajo Tokio»; *Valuable* (#869; 60) → «Objeto de valor»; *Contract* (#2013; 37) → «Contrato». *Relics* → «Reliquias» ya está en la tabla.

#### Combate

- `buffs` (terminólogo, glosario): «Supports you with buffs and uses offensive items. Learns buff skills.» (camp/partnerDescriptionMsg.mbm#2) → «Te apoya con efectos positivos y usa objetos ofensivos. Aprende habilidades de efectos positivos.» La Interfaz puso «mejoras»; SMT V dice *efectos positivos* (rows.md). Con la fila nueva, el validador avisará en esa línea. Decidido: «efectos positivos» también en esa línea.
- `Hit/evade down`, `Critical rate up` (terminólogo, propio de IVA): «Medium <elemento> attack. Effect: Hit/evade down» (battle/SkillHelpMess.mbm#242; 6 veces) → «Precisión/evasión disminuida», por lo decidido (*Hit/evade rate* → «Precisión/evasión») y el estado de SMT V *Accuracy/Evasion Down* ⇒ *Precisión/evasión dis.*. «Effect: Critical rate up» (item/ItemHelpMess.mbm#755), *critical hit rate* (5 veces) → «probabilidad de crítico», como SMT V (*High chance of landing Critical hits* ⇒ *Alta probabilidad de asestar golpes críticos*).
- `Counter` (terminólogo, otro sentido): «Effect: Counter when attacked» (item/ItemHelpMess.mbm#673; también #707, #708, #734 y SkillHelpMess#447-450: 9 veces) → «Contraataca al recibir un ataque»; *Heavy counter* → «contraataque intenso»; *Chance of countering* → «Probabilidad de contraatacar». En SMT V *Counter* es una habilidad (*Contrataque*), y sus descripciones escriben *contraatacar* y *contratacar*. El DLE registra «contraatacar» y «contraataque»; se propone esa forma. No se fija: es el verbo.
- `Law`, `Neutral` (terminólogo, propio de IVA): «<elemento> attack. Strong vs. Law demons» (battle/SkillHelpMess.mbm#45), «Strong vs. Neutral demons» (#44), «Strong vs. Chaos demons» (#43) → «Fuerte contra demonios de la Ley», «... neutrales», «... del Caos». Son los alineamientos; *Chaos* → «Caos» ya está decidido. SMT V no tiene *Law*, y *Neutral* solo sale en nombres de amuletos.
- `Sneak Attack` (terminólogo, propio de IVA): «Phys attacks gain pierce. Sneak Attack activation rate increased» (battle/SkillHelpMess.mbm#499) → «Ataque sigiloso», como el título *Sneak Attacker* → «Atacante sigiloso» (camp/CampCecTable.tbb#0.67.0). Es otro término que *preemptive attack* → «ataque preventivo» (decidido).

#### Base de datos de cazadores (event/HunterDataBase/)

- **Títulos y etiquetas** (terminólogo, propio de IVA): *Hunter Database* (HunterDataBaseHelp.mbm#1) → «Base de datos de cazadores»; *View Hunter Database* (#0) → «Ver la base de datos de cazadores». En las fichas (HunterDataBase.mbm#10-140): *Hunter Name* → «Nombre» (sin género: hay fichas de cazadores y de una cazadora, E-40); *Age/Sex*, *Sex* → «Edad/sexo», «Sexo»; *Male*, *Female* → «Hombre», «Mujer»; *Home District* → «Distrito de origen»; *History*, *History (Addendum)*, *(Addendum 2)* → «Historial», «Historial (anexo)», «(anexo 2)»; *Summary* → «Resumen»; *Death* → «Fallecimiento»; *Functions* → «Funciones»; *Races* → «Razas»; *Emergence* → «Aparición»; *\*More Data Needed* → «\*Faltan datos».
- `God’s Plan` (terminólogo, propio de IVA): «Ironic name of artifacts made before God’s Plan.» (event/HunterDataBase/HunterDataBase.mbm#60; 7 veces) → «el Plan de Dios», como el título ya traducido (event/HunterDataBase/HunterDataTable.tbb#0.11.16). Es el nombre de un acontecimiento del pasado del mundo. IVA lo escribe con apóstrofo curvo y recto: va igual.
- `Ceiling` (terminólogo, propio de IVA): «the dome of rocks now referred to as the Ceiling» (event/HunterDataBase/HunterDataBase.mbm#110; 4 veces en Datos, 11 en IVA) → «el Techo». Es la bóveda de roca que cubre Tokio; el inglés usa la palabra común como nombre propio, y «el Techo» hace lo mismo.
- `cadet` (terminólogo, propio de IVA): «Proof that you are a Hunter cadet.» (item/ItemHelpMess.mbm#831), «In order for a cadet to advance» (HunterDataBase.mbm#30) → «cadete», como *Cadet* → «Cadete» (HunterDataTable.tbb#0.3.16) y *Hunter Cadet ID* → «ID de cadete cazador» (item/ItemTable.tbb#0.0.0). «Cadete» no marca género.
- `Reds`, `magnetite`, `Camp Ichigaya` (terminólogo, propio de IVA): «the human consumption of Reds» (HunterDataBase.mbm#100) → «Reds», el nombre de una sustancia que se come (en otras secciones, carteles como *The best Reds for the best demons!*); se deja como nombre propio. *magnetite* (#100) → «magnetita», como *Biological Magnetite* → «Magnetita biológica» (HunterDataTable.tbb#0.71.16). *Camp Ichigaya* (#40) → «Campamento Ichigaya», como el mapa (map/all/MapNextPointTable.tbb#0.89.8).
- **Apps del teléfono** (HunterDataBase.mbm#70) (terminólogo, propio de IVA): *Quest Management* → «Administración de misiones», *Skill Mangement* → «Administración de habilidades», *Item Management* → «Administración de objetos», *Party Management* → «Administración del grupo», como *Hunters Management* → «Administración de Cazadores» (HunterDataTable.tbb). *Demon Analysis* → «Análisis de demonios» (decidido, *Demon Analyze*); *Report Missing People* → «Reportar desaparecidos», como *Missing Hunters reported* → «Cazadores desaparecidos reportados» (camp/PlayLogTable.tbb#0.27.2); *Various Databases* → «Bases de datos varias»; *GPS* → «GPS». *Mangement* es un error del inglés (§6): se señala y no cambia nada.
- **Diferencias con lo ya traducido** (terminólogo, glosario): *Smartphones* → «Teléfonos inteligentes» (event/HunterDataBase/HunterDataTable.tbb#0.7.16), pero *smartphone* → «teléfono» está decidido; *Demon Summoning Program* → «Programa de invocación» (#0.13.16), pero la tabla dice «Programa de invocación de demonios». Las dos líneas son de Tablas; decidido: *Smartphones* → «Teléfonos»; *Demon Summoning Program* se queda «Programa de invocación», porque la forma completa no cabe en su columna (254 px; el inglés llega a 192). En Datos el término sale entero: *Hunters are awarded smartphones equipped with the Demon Summoning Program* (HunterDataBase.mbm#130).

#### Mitología de los perfiles que SMT V no tiene (status/profile.mbm)

- **lore** (terminólogo, patrón): «A sun goddess of Japanese lore» (145 textos con *lore*; 10 con *myth*, 12 con *folklore*, 7 con *legend*) → «de la mitología japonesa», «según la tradición hindú», «del folclore celta». No se fija: SMT V, en sus perfiles, traduce *lore* por *mitología* (14 de 26 veces), *tradición* (3), *folclore* (3) y *cultura* (3), y *myth*, *mythology* por *mitología*. La etiqueta *Lore* ⇒ *Historia* de SMT V es otra cosa (la pestaña del perfil).
- **Nombres de la mitología** (terminólogo, propio de IVA): *Marduk* (status/profile.mbm#502, #504; 4 veces) → «Marduk»; *Sakra* (#395-399; 4) → «Sakra»; *Mt. Meru* (4) → «monte Meru» (*Mt.* → «monte», tabla); *Hunahpu*, *Xbalanque*, *Xibalba* (#145, #312) → «Hunahpú», «Ixbalanqué», «Xibalbá», las formas del *Popol Vuh* en español; *Arthur* (#236, #286) → «Arturo» (*el rey Arturo*); *Excalibur* → «Excalibur»; *Round Table* (#236) → «la Mesa Redonda»; *Beowulf* → «Beowulf»; *World Tree* (#51, #60) → «el Árbol del Mundo»; *Takaamagahara* (#180, #181; 3) → «Takaamagahara», como lo escribe IVA; *Frigg*, *Hod*, *Hermod*, *Thokk* → se dejan; *Athena* (#341, #359; 3) → «Atenea», como *Pallas Athena* → «Palas Atenea» (decidido); *Book of Revelations*, *Revelations* (#100, #486; 3) → «el libro del Apocalipsis», «el Apocalipsis»; *Kappa* (#262, #438) → «kappa», en minúscula, porque es un tipo de yokai; *Four Holy Beasts* (#49) → «las Cuatro Bestias Sagradas» (SMT V llama a ese grupo *Ssu-Ling*, y IVA también en #205); *Imperial Court* (#639; 3) → «la corte imperial» (SMT V la escribe con minúscula y con mayúscula); *Shogunate* (#631, #639) → «el shogunato».
- `Gaea` (terminólogo, inconsistencia del inglés, §6): «born from the Greek goddess Gaea with no father» (status/profile.mbm#512) → «Gaia». Es la misma diosa que *Gaia* en #273 y #326 (fila oficial «Gaia»). *Gaea* → «Gea» va solo con *Ring of Gaea* (decidido). Decidido: «Gaia».

### Historia

Filas *oficial* (G-1) de la sección Historia (event/e…, battle/event/, battle/gameover/, map/, mikado/, ones_room/). Salen de `system-terms-historia.tsv`, de `glossary-candidates.tsv` y de términos y etiquetas de quien habla que la sección repite. No repiten las filas que GLOSSARY.md ya tiene. Las cifras son textos de la sección en inglés (2415; las 355 líneas en japonés no se cuentan, T-6). Los ejemplos de SMT V salen de sus perfiles, menús y escenas.

#### Términos (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Creator | Creador | SMT V (ejemplos: *was sealed in Shakan by the Creator* ⇒ *fue sellada en Shakan por el Creador*; *If the Creator's dead* ⇒ *Si el Creador ha muerto*) | Título de YHVH (9 textos: *the Creator, YHVH*, *the Creator’s universe*, battle/event/BtlEvent035/BtlEvent035.mbm#0, event/e062/e062.mbm#19). Con artículo y mayúscula: *el Creador*. *Creator God* está en pending.md. |
| Amatsu-kami | Amatsukami | SMT V (ejemplo: *She fell in love with Ninigi of the Amatsukami* ⇒ *Está enamorada de Ninigi de los Amatsukami*) | Los dioses celestiales japoneses (event/e628/e628.mbm#4, #10, #43, #49, #51, #62). SMT V lo escribe en una palabra; IVA, con guion y sin él. *Amatsu* sola es la raza (ya en la tabla). |
| Amatsu-Kami | Amatsukami | SMT V (como *Amatsu-kami*) | Variante del inglés con *K* mayúscula (event/e628/e628.mbm#46). |
| Kunitsu-kami | Kunitsukami | SMT V (ejemplo: *One of the Kunitsukami in Japanese mythology* ⇒ *Uno de los Kunitsukami de la mitología japonesa*) | Los dioses de la tierra japoneses (event/e628/e628.mbm#43). *Kunitsu* sola es la raza (ya en la tabla). |
| kunitsukami | Kunitsukami | SMT V (como *Kunitsu-kami*) | Variante del inglés en minúscula (event/e031/e031.mbm#3, #12). SMT V lo escribe con mayúscula. |
| fairy queen | reina de las hadas | SMT V (ejemplo: *before I knew it, I was made fairy queen* ⇒ *antes de saberlo, me nombraron reina de las hadas*) | Título de un personaje (event/e020/e020.mbm#57, event/e043/e043.mbm#11, event/e072/e072.mbm#19). En minúscula, como SMT V. |
| Fairy Queen | reina de las hadas | SMT V (como *fairy queen*) | Vocativo con mayúscula (event/e628/e628.mbm#45). |
| turn icons | iconos de acción | SMT V (*Press Turn Icons* ⇒ *iconos de acción*; ejemplo: *Adds 2 Press Turn Icons to user's next turn* ⇒ *Añade 2 iconos de acción al siguiente turno del usuario*) | El tutorial de combate (battle/event/BtlEvent001/BtlEvent001.mbm#4: *blue turn icons*). Es el mismo sistema que *Press Turn Icons*, ya en la tabla. |
| English | inglés | SMT V (etiqueta *English* ⇒ *Inglés*; ejemplo: *English Voices* ⇒ *Voces en inglés*) | El idioma: *...So the sign reads, in English.* (19 textos: map/m010/m010.mbm, event/e512/e512.mbm). En minúscula a media frase. |
| Japan | Japón | SMT V (ejemplo: *In Japan, she was worshipped by warriors* ⇒ *En Japón era venerada por los guerreros*) | El país (event/e645/e645.mbm#33, #39, #41; event/e650/e650.mbm#6, #22, #35). |

#### Nombres de quien habla (oficiales)

Etiquetas de SMT V (*CharacterName*) con el mismo sentido. G-3: la etiqueta tiene que ser idéntica en todas sus líneas.

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Man’s voice | Voz masculina | SMT V (personaje: *Man's Voice* ⇒ *Voz masculina*) | Etiqueta de quien habla (event/e050/e050.mbm#12, event/e502/e502.mbm#0, event/e621/e621.mbm#1). |
| Familiar voice | Voz familiar | SMT V (personaje: *Familiar Voice* ⇒ *Voz familiar*) | Etiqueta de quien habla (event/e096/e096.mbm#6). |
| Demon’s voice | Voz de demonio | SMT V (personaje: *Demon's Voice* ⇒ *Voz de demonio*) | Etiqueta de quien habla (event/e031/e031.mbm#1). |
| Young man | Joven | SMT V (personaje: *Young Man* ⇒ *Joven*) | Etiqueta de quien habla (event/e056/e056.mbm#1, #6). |
| Danu’s voice | Voz de Danu | SMT V (patrón: *Zeus's Voice* ⇒ *Voz de Zeus*, *Isis's Voice* ⇒ *Voz de Isis*) | Etiqueta de quien habla (event/e065/e065.mbm#56, #59). |
| Asahi’s voice | Voz de Asahi | SMT V (patrón, como *Danu’s voice*) | Etiqueta de quien habla (event/e041/e041.mbm#0, event/e055/e055.mbm#0). |
| Nozomi’s voice | Voz de Nozomi | SMT V (patrón, como *Danu’s voice*) | Etiqueta de quien habla (1 línea). |
| Hiroshi’s voice | Voz de Hiroshi | SMT V (patrón, como *Danu’s voice*) | Etiqueta de quien habla (1 línea). |
| Maitreya’s voice | Voz de Maitreya | SMT V (patrón, como *Danu’s voice*) | Etiqueta de quien habla (1 línea). |

#### Decididos por el usuario: Historia

Aprobados en bloque el 2026-11-09 (las propuestas del terminólogo). *Lord X* → «el señor X» (vocativo «señor X») y *Lady X* → «la señora X» no van en la tabla porque *Lord* y *Lady* también forman otros términos (*Demon Lord*, la raza *Lady* → «Dama»).

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| My Lord | mi Señor | Decidido 2026-11-09 (G-2) | Cuando un ángel habla de su dios; *the Lord* → «el Señor». |
| His Lordship | Su Señoría | Decidido 2026-11-09 (G-2) | Tratamiento de noble, con la afectación del inglés. |
| Miss Isabeau | señorita Isabeau | Decidido 2026-11-09 (G-2) | «la señorita Isabeau». |
| Sir Gaston | sir Gaston | Decidido 2026-11-09 (G-2) | *SIR Gaston* → «SIR Gaston». |
| SIR Gaston | SIR Gaston | Decidido 2026-11-09 (G-2) | El tic de la ficha de Gaston. |
| Captain Gaston | capitán Gaston | Decidido 2026-11-09 (G-2) |  |
| Grand Member | Gran Miembro | Decidido 2026-11-09 (G-2) | Conserva el doble sentido del inglés. |
| Hunter Boy | Chico Cazador | Decidido 2026-11-09 (G-2) | Apodo, con mayúsculas. |
| Boss | jefe | Decidido 2026-11-09 (G-2) | Trato. |
| Bro | Hermano | Decidido 2026-11-09 (G-2) | Apelativo fijo, con mayúscula. |
| Creator God | Dios Creador | Decidido 2026-11-09 (G-2) | *el Dios Creador*. |
| the Powers | los Poderes | Decidido 2026-11-09 (G-2) | Por *Divine Powers* → «Poderes Divinos». |
| Patriots | Patriotas | Decidido 2026-11-09 (G-2) | *the Patriots* → «los Patriotas»; etiqueta *The Patriots* → «Los Patriotas». |
| Maruology | Maruología | Decidido 2026-11-09 (G-2) |  |
| Male Maruo follower | Seguidor de Maruo | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Female Maruo follower | Seguidora de Maruo | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Aether | éter | Decidido 2026-11-09 (G-2) | En minúscula, como *magnetita*. |
| Axiom | Axioma | Decidido 2026-11-09 (G-2) | *el Axioma*. |
| Salvation | salvación | Decidido 2026-11-09 (G-2) | En minúscula (E-59). |
| Filth | Inmundicia | Decidido 2026-11-09 (G-2) | Con mayúscula, como el inglés; *Unclean Ones* → «los Impuros». |
| Demon Lord | Rey Demonio | Decidido 2026-11-09 (G-2) | *the Demon Lord Lucifer* → «el Rey Demonio Lucifer». |
| Allfather | Padre de Todos | Decidido 2026-11-09 (G-2) | *el Padre de Todos*. |
| Plain of High Heaven | Alta Llanura del Cielo | Decidido 2026-11-09 (G-2) |  |
| Tuatha De | Tuatha Dé | Decidido 2026-11-09 (G-2) |  |
| the Apathetic | el Apático | Decidido 2026-11-09 (G-2) | Epíteto de una vasija (*Sloth* → «la Pereza»). |
| the Devourer | el Devorador | Decidido 2026-11-09 (G-2) | (*Gluttony* → «la Gula»). |
| the Desired | el Deseado | Decidido 2026-11-09 (G-2) | (*Lust* → «la Lujuria»). |
| the Vengeful | el Vengativo | Decidido 2026-11-09 (G-2) | (*Wrath* → «la Ira»). |
| the Superior | el Altivo | Decidido 2026-11-09 (G-2) | (*Pride* → «la Soberbia»). |
| Gauntlet Rite | Rito del Guantelete | Decidido 2026-11-09 (G-2) |  |
| VR simulation | simulación de realidad virtual | Decidido 2026-11-09 (G-2) | *V-hee-R* va a delicadas. |
| Assist Gauge | indicador de apoyo | Decidido 2026-11-09 (G-2) |  |
| Play Coins | Monedas de juego | Decidido 2026-11-09 (G-2) | Provisional: se comprueba en el juego. |
| Styx | Estigia | Decidido 2026-11-09 (G-2) | *el río Estigia*; *ferryman* → «barquero». |
| portal cube | cubo portal | Decidido 2026-11-09 (G-2) |  |
| Node | Nodo | Decidido 2026-11-09 (G-2) | *Node 1-4* → «Nodo 1-4». |
| Adramalech | Adramelec | Decidido 2026-11-09 (G-2) | Error del inglés (§6). |
| Yamato no Orochi | Yamata-no-Orochi | Decidido 2026-11-09 (G-2) | Error del inglés (§6). |
| National Defense Deities | Divinidades de Defensa Nacional | Decidido 2026-11-09 (G-2) | Inconsistencia del inglés (§6). |
| Myoko’s Disk | Disco de Myoko | Decidido 2026-11-09 (G-2) | Inconsistencia del inglés (§6). |
| Yamato Reactor | Reactor Yamato | Decidido 2026-11-09 (G-2) | Forma corta de *Yamato Perpetual Reactor*. |
| Surrounding Hunters | Cazadores presentes | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Gathered people | Gente reunida | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Hunter on mission | Cazador en misión | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Divine Powers demon | Demonio de los Poderes Divinos | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Tamagami’s remnants | Remanente de Tamagami | Decidido 2026-11-09 (G-2) | Etiqueta; un solo hablante. |
| Street vendor | Vendedor ambulante | Decidido 2026-11-09 (G-2) | Etiqueta. |
| Woman called ”Noa” | Mujer llamada “Noa” | Decidido 2026-11-09 (G-2) | Etiqueta. |

#### Propuestas aprobadas de Historia (detalle)

El detalle del terminólogo, aprobado en bloque. Lo que tiene fila arriba manda; el resto (etiquetas de quien habla, patrones) se aplica igual.

Términos *por decidir* (G-2) de la sección Historia: event/e…, battle/event/, battle/gameover/, map/, mikado/, ones_room/. Las cifras son textos de la sección en inglés (2415); las 355 líneas en japonés se tratan aparte (T-6, al final). Lo que ya está traducido en otras secciones se cita para que coincida.

##### Pendientes anteriores que aparecen en Historia

- `Man` (terminólogo, otro sentido; ya en PENDING): en Historia es la interjección en 7 textos («Man, I would have gotten completely lost by myself.», event/e044/e044.mbm#25; también event/e621/e621.mbm#3, #26, #27, event/e634/e634.mbm#1, map/m037/m037.mbm#9) y la etiqueta de quien habla en 4 líneas (event/e619/e619.mbm#2, #4, #6). Propuesta sin cambio: no se fija; la etiqueta va «Hombre», como SMT V (*Man* ⇒ *Hombre*), y la interjección según el tono.
- `Lady`, `Lord` (GLOSSARY, Tablas: «se deciden juntos como tratamientos»): Historia es donde salen. Propuesta en «Tratamientos», abajo.
- `Bartender` (terminólogo, quien habla; ya en PENDING): 6 líneas en Historia (event/e999/e999.mbm#10-15). Las Tablas ya lo tradujeron «Cantinero» (quest_center/common/NpcHaichiTable.tbb), y PENDING propone «Tabernero». La etiqueta tiene que ser la misma en las tablas y en los mensajes (G-3): lo que se decida vale para las dos. **Decidido 2026-11-10: «Bartender»** (ver Secundarias).
- `Attack` (terminólogo, otro sentido): «Choose ”Attack” from the list of commands.» (battle/event/BtlEvent001/BtlEvent001.mbm#4) y las órdenes «Attack Heal Support Wait» (battle/event/BtlEventSub150/BtlEventSub150.mbm#4) → «Atacar», «Curar», «Apoyo», «Esperar». *Atacar* es la habilidad de SMT V (*Attack* ⇒ *Atacar*) y *Support* ⇒ *Apoyo* ya está en la tabla. Duda: el menú de comandos de combate no está en las tablas (debe ser una textura, PLAN, fase 1); si queda en inglés, el tutorial tendría que citar «Attack» tal cual. Se comprueba en el juego. *Attack* no se fija: como estadística es «Ataque» (GLOSSARY).
- `Power` (terminólogo, quien habla): la etiqueta *Power* (event/e039/e039.mbm#7) es el demonio → «Potestad», como dice GLOSSARY. Solo se confirma.

##### Tratamientos

SMT V no los traduce de una sola forma: *Lord Shiva* ⇒ *el Gran Shiva*, *Lord Lucifer* ⇒ *lord Lucifer* y *el gran Lucifer*, *Lord Okuninushi* ⇒ *el señor Okuninushi*, *Lady Ishtar* ⇒ *la Gran Ishtar*, y a veces lo quita (*Lady Idun* ⇒ *Idún*, *Lord Odin* ⇒ *Odín*). Por eso no hay término oficial (G-2). E-59: en minúscula a media frase.

- `Lord` (terminólogo, tratamiento): *Lord Merkabah* (10 textos), *Lord Dagda* (7), *Lord Lucifer* (6), *Lord Maitreya* (4), *Lord Tenkai* (2), *Lord Shax* (1) → «el señor X»; en vocativo, «señor X» («We need to ask you something, Lord Tenkai.» → «Tenemos que pedirle algo, señor Tenkai.», event/e072/e072.mbm#5). *LORD Dagda?* (event/e032/e032.mbm#5) → «¿SEÑOR Dagda?». Sirve para dioses, ángeles, demonios y humanos, y también en vocativo. Alternativa: «el gran X», la forma más frecuente de SMT V, pero no sirve en vocativo («gran Tenkai»). Las fichas ya lo usan para el trato (merkabah.md, gaston.md, odin.md, nozomi.md, demonee-ho.md).
- `My Lord`, `the Lord` (terminólogo, tratamiento): «My Lord shall construct as many of me as necessary.» (battle/event/BtlEvent061/BtlEvent061.mbm#0), *the Lord’s*, *our Lord’s* → «mi Señor», «el Señor», con mayúscula, como SMT V cuando un ángel habla de su dios (*My Lord does not wish for that to happen* ⇒ *Mi Señor no desea que ocurra tal cosa*).
- `His Lordship` (terminólogo, tratamiento): «His Lordship would like our messiah, Flynn, to stand with us now.» (event/e096/e096.mbm#7) → «Su Señoría», tratamiento de noble, con la afectación del inglés (ficha de Adramelech). Alternativa: «Su Majestad».
- `Lady` (terminólogo, tratamiento): *Lady Yuriko* (2 textos), *Lady Noa* (battle/event/BtlEventSub127/BtlEventSub127.mbm#0), *Lady Amaterasu* (1), *Ladies Mii and Kei* (map/m005/m005.mbm#3) → «la señora X», «las señoras Mii y Kei», como *Lord* → «señor». Alternativa: dejar «lady Yuriko». Como raza, *Lady* sigue siendo «Dama» (Tablas).
- `Miss Isabeau` (terminólogo, tratamiento; 7 textos) → «la señorita Isabeau», como propone la ficha de Asahi.
- `Sir Gaston`, `SIR Gaston` (terminólogo, tratamiento; 5 textos: event/e056/e056.mbm#22, event/e087/e087.mbm#19…) → «sir Gaston», «SIR Gaston». *Sir* es el título de caballero y en español se entiende; con *SIR* en mayúsculas se mantiene el tic que pide la ficha de Gaston. Alternativa: «don Gaston», que pierde lo caballeresco. *Captain Gaston* (event/e056/e056.mbm#10) → «el capitán Gaston».
- `Mr.` (terminólogo, tratamiento): «I’m sorry, Mr. Hunter.» (event/e634/e634.mbm#53; 4 textos) → «señor cazador»; «You worried, Mr. New Boss?» (event/e634/e634.mbm#60) → «señor nuevo jefe». *Mister* a secas, de un niño (event/e634/e634.mbm#6, #10) → «señor».
- `Grand Member` (terminólogo, título; 6 textos): «Yes! Grand Member! That’s Grand Member Maruo!» (event/e621/e621.mbm#1) → «Gran Miembro». El inglés juega con *member* (miembro de un grupo y, en la misma escena, *as precious as the family jewels*, el chiste anatómico); «miembro» tiene en español los mismos dos sentidos, así que el juego se conserva. Si se quiere revisar, va a delicadas (E-23).
- `Hunter Boy` (terminólogo, apodo; 5 textos): «Let me teach you a lesson, Hunter Boy!» (battle/event/BtlEventSub131/BtlEventSub131.mbm#1) → «Chico Cazador», con mayúsculas como apodo. Alternativa: «Cazadorcito», más burlón.
- `Boss` (terminólogo, trato; 5 textos: event/e035/e035.mbm#14, event/e634/e634.mbm#20) → «jefe».
- `Bro` (terminólogo, trato; 6 textos): «Sure thing, Bro!» (event/e051/e051.mbm#16) → «Hermano», con mayúscula como si fuera un nombre, como dice la ficha de Hallelujah («fijo en todo el juego»). *Hermano* como apelativo se usa en toda América. *Jefe* no sirve: el inglés los distingue (*He's not my boss, he's my bro*, event/e096/e096.mbm#10).

##### Títulos, grupos y nombres propios de IVA

- `Creator God` (terminólogo, propio de IVA): «I cannot permit allegiance with the Creator God over the Divine Powers.» (battle/event/BtlEvent008/BtlEvent008.mbm#0; también BtlEvent021#0, event/e063/e063.mbm#16) → «el Dios Creador», título de YHVH, con *Creator* → «Creador» (rows.md). SMT V solo lo tiene en minúscula y para otro dios (*The creator god Brahma* ⇒ *El dios creador Brahma*).
- `the Powers` (terminólogo, abreviatura): «The Powers must be after the sword.» (event/e043/e043.mbm#9; también event/e622/e622.mbm#8) → «los Poderes», por *Divine Powers* → «Poderes Divinos» (decidido).
- `Patriots` (terminólogo, quien habla y grupo): la etiqueta *The Patriots* (42 líneas, event/e645/e645.mbm) y «Just call us the Patriots» (#8) → «Los Patriotas», «los Patriotas», como ya está traducido *The Patriots* en event/quest/SubQuestData.tbb#0.43.64. El demonio *Patriot* ya es «Patriota» (Tablas), así que las dos formas coinciden.
- `Stephen`, `Noa`, `Burroughs` (terminólogo, nombres propios): «My name is Stephen.» (event/e037/e037.mbm#6; 7 textos y 8 líneas con su etiqueta), «Noa...» (event/e645/e645.mbm#25; 11 textos), la etiqueta *Burroughs* (map/m008/m008.mbm#1; 4 en Historia, 44 en IVA) → se dejan igual, como los demás nombres de IVA (Tablas). *Woman called ”Noa”* (event/e645/e645.mbm#26) → «Mujer llamada “Noa”».
- `Maruology`, `Maruo follower` (terminólogo, propio de IVA): «That’s what Maruology is all about!» (event/e621/e621.mbm#9; también map/m014/m014.mbm#2) → «Maruología». Etiquetas *Male Maruo follower* (12 líneas), *Female Maruo follower* (6), *Maruo follower* (1) → «Seguidor de Maruo», «Seguidora de Maruo», «Seguidor de Maruo», como *Male/Female Gaean* → «Seguidor/Seguidora de Gea» (Tablas).
- `Aether` (terminólogo, propio de IVA): «You might be more familiar with Aether by its other name, Magnetite.» (event/e072/e072.mbm#12; 6 textos) → «éter», en minúscula como *magnetite* → «magnetita» (decidido en Datos; E-59). Alternativa: «Éter», con mayúscula como el inglés.
- `Axiom` (terminólogo, propio de IVA): «It is about the mission that the Axiom has given you humans» (event/e901/e901.mbm#8, #9) → «el Axioma».
- `Salvation` (terminólogo, propio de IVA): «I know that it is difficult for you to accept my Salvation...» (battle/event/BtlEvent023/BtlEvent023.mbm#0; unos 15 textos, 3 con mayúscula) → «salvación», en minúscula en todos (E-59). Alternativa: «Salvación» donde el inglés la escribe con mayúscula (BtlEvent023#0, event/e067/e067.mbm#2, event/e901/e901.mbm#4).
- `Filth` (terminólogo, propio de IVA): «You are Filth beyond even that of the Unclean Ones.» (battle/event/BtlEvent033/BtlEvent033.mbm#0; también BtlEvent060#0, BtlEvent061#0, event/e015/e015.mbm#10: *Unclean Filth*) → «Inmundicia», con mayúscula como el inglés, junto a *Unclean Ones* → «los Impuros» (decidido). Alternativa: «Escoria».
- `Demon Lord` (terminólogo, título): «sworn knight of the Demon Lord Lucifer» (event/e096/e096.mbm#7) → «el Rey Demonio Lucifer». SMT V lo dice así en una línea genérica (*the Demon Lord you seek to defeat* ⇒ *ese Rey Demonio al que quieres derrotar*). La etiqueta japonesa *悪魔王ルシファー* (abajo) dice lo mismo. Alternativa: «el Señor de los Demonios».
- `Allfather` (terminólogo, epíteto): «Others among the kunitsukami may lap up the Allfather’s lies» (event/e031/e031.mbm#12) → «el Padre de Todos», el epíteto de Odín.
- `Plain of High Heaven` (terminólogo, lugar mitológico): «Means he’s a deity from the Plain of High Heaven.» (event/e628/e628.mbm#62) → «la Alta Llanura del Cielo». La frase explica *Amatsu-kami*, así que se traduce; en Datos el nombre japonés quedó «Takaamagahara».
- `Tuatha De` (terminólogo, otro sentido): «I am Danu, mother of the Tuatha De» (event/e020/e020.mbm#57) → «los Tuatha Dé». SMT V los nombra completos (*the Tuatha Dé Danann* ⇒ *los Tuatha Dé Danann*), con tilde en *Dé*. Alternativa: «los Tuatha Dé Danann», como SMT V, aunque agrega una palabra que el inglés no dice.
- **Epítetos y pecados de las vasijas** (terminólogo, títulos): «I am Jikokuten, the Apathetic. This jar draws the essence of Sloth.» (event/e073/e073.mbm#1), y lo mismo en event/e075#1, e077#1, e079#1, e081#1 → *the Apathetic* «el Apático» (Sloth «la Pereza»), *the Devourer* «el Devorador» (Gluttony «la Gula»), *the Desired* «el Deseado» (Lust «la Lujuria»), *the Vengeful* «el Vengativo» (Wrath «la Ira»), *the Superior* «el Altivo» (Pride «la Soberbia»). Los pecados, con su nombre en español y con mayúscula como el inglés. *el Altivo* en vez de *el Superior* para que el epíteto se lea con la soberbia, como los otros cuatro con su pecado; alternativa: «el Superior».
- `Gauntlet Rite` (terminólogo, propio de IVA): «Go to Aquila Statue Plaza to participate in the Gauntlet Rite?» (mikado/m000/m000.mbm#1) → «el Rito del Guantelete», por *Gauntlet* → «Guantelete» (decidido).

##### Sistema y mapas

- `VR` (terminólogo, propio de IVA): «You log out of the VR simulation.» (battle/event/Systematic_001-004, 7 textos) → «Sales de la simulación de realidad virtual.» La sigla en español es *RV*, poco reconocible, y *VR* en inglés no es neutra; la forma completa cabe en la caja. *V-hee-R* (Systematic_004#1, #3), el juego de Demonee-ho con la sigla, va a delicadas (E-23).
- `Assist Gauge` (terminólogo, propio de IVA): «The Assist Gauge increases.» (battle/event/BtlEvent022/BtlEvent022.mbm#110; también BtlEvent016#4, BtlEventSub131#4, #14) → «indicador de apoyo», como SMT V (*Magatsuhi Gauge* ⇒ *indicador de magatsuhi*) y como ya está traducido *Assist Attacks* → «Ataques de apoyo» (event/HowTo/HowToTable.tbb#0.17.4).
- `Play Coins` (terminólogo, marca): «You can pay me in Play Coins, if you’d like.» (battle/gameover/gameover.mbm#10; también #11, #16-18) → «Monedas de juego», el nombre de Nintendo en la consola en español. Provisional, como los menús de la consola: se comprueba en el juego.
- `Styx` (terminólogo, lugar mitológico): «welcome to the river Styx» (battle/gameover/gameover.mbm#1, #2, #5) → «el río Estigia». *ferryman* → «barquero», por *Charon* → «Caronte» (decidido).
- `region` (terminólogo, patrón de mapa): «Go to the Ueno region?» (map/L001/l001.mbm#1; 20 textos en map/L001/l001.mbm y map/m037/m037.mbm, con Ueno, Chiyoda, Ikebukuro, Shinjuku, Roppongi, Joto, Johoku, Daiba y *coastal region*) → «¿Ir a la región de Ueno?», «la región costera». SMT V usa *región* igual (*the Shinano region* ⇒ *la región de Shinano*). Los nombres japoneses se dejan igual (patrón de Tablas). *According to Mapper, up ahead is…* → «Según el Cartógrafo, más adelante está…», por la app *Mapper* → «Cartógrafo» (decidido).
- `portal cube`, `Node` (terminólogo, propio de IVA): «It seems no other portal cubes are activated...» (map/m028/m028.mbm#5; 8 textos en map/m028-m031) → «cubo portal»; las opciones *Node 1-4* (16 textos) → «Nodo 1-4». Alternativa: «cubo de transporte», por *the transportation cannot occur* de la misma línea.
- `request` (terminólogo, propio de IVA): «Must’ve intercepted the Hunter request.» (event/e043/e043.mbm#8; también event/e634/e634.mbm#44, event/e645/e645.mbm#8; en event/e049/e049.mbm#8 es el verbo) → «encargo», «el encargo para los cazadores». Es el pedido que alguien deja en la Asociación; *quest* → «misión» ya está en la tabla, y *quest notes* (event/e049/e049.mbm#0) → «las notas de la misión». Alternativa: «solicitud». Se confirma en Secundarias, donde más sale.

##### Errores e inconsistencias del inglés (§6: se señalan, no se corrigen)

- `Adramalech` (terminólogo, error del inglés): «Adramalech looks down at the broken sword» (battle/event/BtlEvent002/BtlEvent002.mbm#9; 3 textos) → «Adramelec», el nombre oficial (*Adramelech* ⇒ *Adramelec*, ya en la tabla).
- `Yamato no Orochi` (terminólogo, error del inglés): «I see you have Yamato no Orochi» (event/e628/e628.mbm#64) → «Yamata-no-Orochi», como en la tabla.
- `Burrough` (terminólogo, error del inglés): la etiqueta de quien habla de map/m007/m007.mbm#0 → «Burroughs».
- `National Defense Deities` (terminólogo, inconsistencia): «I am Tenkai, one of the National Defense Deities.» (event/e072/e072.mbm#4); en los demás textos y en las Tablas es *National Defense Divinities* → «Divinidades de Defensa Nacional» (decidido) en los dos.
- `Myoko’s Disk` (terminólogo, inconsistencia): «Myoko’s Disk shines in your hand.» (event/e072/e072.mbm#1); la tabla de objetos dice *Myoko's Disc* → «Disco de Myoko» (item/ItemTable.tbb#0.11.0, ya traducido) en los dos.
- `Yamato Reactor` (terminólogo, forma corta): «the Yamato Reactor in Ichigaya» (event/e049/e049.mbm#11) → «el Reactor Yamato», forma corta de *Yamato Perpetual Reactor* → «Reactor Perpetuo Yamato» (decidido).

##### Nombres de quien habla

Etiquetas `{F812}` de Historia que no están en el glosario ni en SMT V. Siguen el patrón de Tablas (*[Adjetivo] man/woman/Hunter* → «[Sustantivo] [adjetivo]») y tienen que coincidir en todas sus líneas (G-3). Las que el inglés no marca en género quedan con la decisión de conjunto pendiente (PENDING, lote tablas-005, E-40): aquí van en masculino solo como propuesta.

- **Grupos** (terminólogo, quien habla): *Surrounding Hunters* (16 líneas, event/e065/e065.mbm) → «Cazadores presentes»; *Gathered people* (7, event/e124/e124.mbm) → «Gente reunida»; *Hunter reinforcement* (5, event/e014-e016) → «Cazador de refuerzo»; *Hunter reinforcements* (1) → «Cazadores de refuerzo»; *Hunters* (ya en la tabla) → «Cazadores»; *Ashura-kai members* (2) → «Miembros del Ashura-kai»; *Gaeans* (2) → «Seguidores de Gea»; *Obsessed horde* (1) → «Horda obsesionada» (patrón de hordas, Tablas).
- **Cazadores** (terminólogo, quien habla y género E-40): *Hunter on mission* (7, event/e014/e014.mbm) → «Cazador en misión»; *Large Hunter*, *Small Hunter* (5 y 4, event/e049/e049.mbm) → «Cazador grandote», «Cazador bajito»; *Friendly Hunter* (3) → «Cazador amistoso»; *Expressionless*, *Flustered*, *Thick-jawed*, *Lazy-ish*, *Middle-aged Hunter* (2 cada una) → «Cazador inexpresivo», «nervioso», «de mandíbula ancha», «algo flojo», «de mediana edad»; *Male Hunter* (2) → «Cazador»; *Serious*, *Busy*, *Gentle-looking Hunter*, *Hunter guard* (1) → «Cazador serio», «ocupado», «de aspecto amable», «Guardia cazador». *Kinshicho Hunter* (1) → «Cazador de Kinshicho».
- **Ángeles, demonios y facciones** (terminólogo, quien habla): *Divine Powers demon* (7) → «Demonio de los Poderes Divinos»; *Sky Tower guard angel* (4) → «Ángel guardián de Sky Tower», por *Guard angel* → «Ángel guardián» (Tablas); *Overbearing angel* → «Ángel prepotente»; *Newcomer angel* → «Ángel novato»; *Cute demon*, *Sexy demon* (2 cada una, event/e050/e050.mbm) → «Demonio lindo», «Demonio sexy» (*demon* → «demonio» aunque sea mujer, decidido en Datos); *Lucifer’s minion* (2) → «Esbirro de Lucifer», por *Lucifer's Minions* → «Esbirros de Lucifer» (Tablas); *Merkabah’s subordinate* → «Subordinado de Merkabah»; *Eastern Crusader* → «Cruzado oriental», por *Crusaders* → «los Cruzados» y *Eastern Kingdom of Mikado* → «Reino Oriental de Mikado»; *Yuriko-faction Gaean* (4, map/m005/m005.mbm) → «Seguidor de Gea (Yuriko)», por *Male Gaean* → «Seguidor de Gea»; alternativa, si cabe: «Seguidor de Gea de Yuriko»; *Gaea man* (3) → «Hombre de Gea» (Tablas); *Ring of Gaea guard* → «Guardia del Anillo de Gea»; *Samurai guard* → «Guardia samurái»; *Maitreya cultist* (3) → «Devoto de Maitreya»; *Believer* (3) → «Creyente»; *Demonoid woman* → «Mujer demonoide».
- **Restos** (terminólogo, quien habla): *Tamagami’s remnants* (10, event/e645/e645.mbm, battle/event/BtlEventSub145) → «Remanente de Tamagami»; *Inanna’s remnants* (2) → «Remanente de Inanna», como *Inanna Remnant* → «Remanente de Inanna» (Tablas). El inglés va en plural, pero cada etiqueta es un solo hablante.
- **Personas** (terminólogo, quien habla y género E-40): *Child* (12, event/e634/e634.mbm) → «Niño» (E-40: el inglés no lo marca); *Girl* (4, event/e001/e001.mbm#101-112) → «Chica»; *Boy* (1) → «Chico»; *Street vendor* (4 en Historia, 8 en IVA, event/e999/e999.mbm) → «Vendedor ambulante» (E-40); *TV* (5, event/e001/e001.mbm#110-118) → «TV»; *Old man* → «Anciano»; *Old woman on the left/right* → «Anciana de la izquierda/derecha»; *Thin man*, *Thin woman* (3 cada una) → «Hombre delgado», «Mujer delgada»; *Toned woman* (3) → «Mujer atlética»; *Teary-eyed man* (2) → «Hombre lloroso»; *Grim-faced man* (2) → «Hombre sombrío», como ya está en las tablas; *Grim-faced guard*, *Gentle-looking guard* → «Guardia sombrío», «Guardia de aspecto amable»; *Mysterious man* (2, battle/gameover/gameover.mbm#0, #1) → «Hombre misterioso»; *Hunter-idolizing boy* (3) → «Niño fan de los cazadores»; *Hunter-aspiring sister* (2) → «Hermana aspirante a cazadora»; *Disinterested brother* → «Hermano indiferente»; *Helmeted girl* (2) → «Chica con casco»; *Man in a wheelchair* → «Hombre en silla de ruedas»; *Man who was crying* → «Hombre que lloraba»; *Irritated young man* → «Joven irritado», por *Young man* → «Joven» (rows.md); *Ill-natured man* → «Hombre malintencionado»; *Piercing gaze man* → «Hombre de mirada penetrante»; *Scrap-collecting man* → «Chatarrero».
- **Voces** (terminólogo, quien habla): *Boy’s voice*, *Girl’s voice* (4 cada una, event/e001/e001.mbm) → «Voz de chico», «Voz de chica»; *Old man’s voice* (2) → «Voz de anciano»; *Haughty woman’s voice* → «Voz de mujer altiva»; *Bewitching voice* (2) → «Voz seductora»; *Majestic*, *Upbeat*, *Pompous*, *Fierce*, *Arrogant voice* → «Voz majestuosa», «alegre», «pomposa», «feroz», «arrogante». Siguen *Man’s voice* → «Voz masculina» y *Familiar voice* → «Voz familiar» (SMT V, rows.md).
- **Con signo de pregunta** (terminólogo, E-52): *Nozomi?* (event/e020/e020.mbm#2, #5) → «¿Nozomi?», como ya está en las tablas; *Maruo?* (event/e644/e644.mbm#8) → «¿Maruo?».

##### Etiquetas en japonés (T-6)

Las 355 líneas en japonés de Historia no se traducen hasta saber si el juego las muestra (T-6), salvo las dos escenas que el PLAN manda traducir desde el japonés. Si se traducen, sus etiquetas (`{F812}`) tienen que coincidir con las del inglés (G-3). Propuesta:

- (terminólogo, quien habla): *バロウズ* (22) → «Burroughs»; *メルカバー* (21) → «Merkabah»; *悪魔王ルシファー* (20) → «Rey Demonio Lucifer» (ver *Demon Lord*, arriba); *イザボー* (11) → «Isabeau»; *悪魔化したサムライ* (8) → «Samurái demonizado»; *露天商* (6) → «Vendedor ambulante», como *Street vendor*; *店主* (6) → «Dependiente», como *Shopkeeper* (decidido); *デモニホ* (5) → «Demonee-ho»; *ルキフグス* (4) → «Lucifuge»; *ベリアル* (4) → «Belial»; *ラファエル*, *ミカエル*, *ガブリエル*, *ウリエル* (2 cada una) → «Rafael», «Miguel», «Gabriel», «Uriel»; *マザーハーロット* (2) → «Ramera babilónica»; *アドラメレク* (2) → «Adramelec»; *サナト* (2) → «Sanat»; *エンシェントデイ* (2) → «Anciano de Días»; *ピアレイ* (1) → «Peallaidh»; *イサカル* (1) → «Issachar»; *威厳に満ちた声* (1) → «Voz majestuosa», como *Majestic voice*. Habitantes (4 cada una): *顔が濃いギャル* → «Chica de rasgos marcados»; *警備員風の男* → «Hombre con pinta de guardia»; *江戸っ子風の男* → «Hombre con aire de Edo» (el *edokko*, el nacido en Tokio de toda la vida); *小汚い男* → «Hombre desaliñado»; *場違いな男* → «Hombre fuera de lugar»; *勘が鋭い男* → «Hombre perspicaz»; *ホスト風の男* → «Hombre con pinta de anfitrión de club»; *エリート風の男* → «Hombre con aire de élite»; *血気盛んな獄卒*, *礼儀正しい獄卒* (3 cada una) → «Carcelero impetuoso», «Carcelero educado». *テスト* (1) es una prueba: no se traduce.

### Secundarias

Filas de la sección Secundarias (event/quest/, quest_center/, npc_room/, event/PartnerTopic/; 1578 mensajes en en.jsonl, 1575 en la cuenta). Salen de `system-terms-secundarias.tsv` (202 términos), de `glossary-candidates.tsv` y de los términos y etiquetas de quien habla que la sección repite. No repiten las filas que GLOSSARY.md ya tiene. Las cifras son líneas de la sección en inglés. Los ejemplos de SMT V salen de sus tablas de texto (menús, misiones, escenas), emparejadas inglés-español.

#### Términos de sistema (oficiales)

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Heal | Curar | SMT V (ejemplo: *Heal all* ⇒ *Curar todos*, la opción que cura al grupo) | Opción del menú de la taberna, *Heal / Talk / Deliver* (quest_center/center/center*.mbm#0 y center14_a/b.mbm#1, quest_center/common/qc_common.mbm; 15 líneas). Mismo sentido: curar al grupo. Va con *Talk* → «Hablar» (ya en la tabla) y *Talk to Boss* → «Hablar con el jefe» (*Boss* → «jefe», decidido). El tutorial de Historia ya lo pone igual (*Attack Heal Support Wait*). *Heal up!* (3 textos de otra sección) es el verbo común. |

Oficiales de SMT V que no van en la tabla, porque en IVA también son palabras comunes de otras frases y el validador avisaría de más (como *Search*, *Special* y *End* en la Interfaz):

- *Never mind*, opción de menú (quest_center/center/center14_a.mbm, center14_b.mbm: *Deliver / Never mind*, 2 líneas) → «Mejor no». SMT V la traduce así como opción (*Never mind* ⇒ *Mejor no*, 3 de 4 veces). En los diálogos (12 veces en IVA) es la frase común.
- *accept* una misión → «aceptar» (SMT V: *Accept the quest "  "?* ⇒ *¿Aceptar la misión "  "?*; *Accepted quest "  "* ⇒ *Misión aceptada: "  "*). event/quest/QuestSys.mbm, 16 líneas; event/quest/QuestUITable.tbb ya lo dice así.
- *abandon* una misión → «abandonar» (SMT V: *: Abandoned.* ⇒ *: abandonada.*). event/quest/QuestSys.mbm#2, #36. *give up* (#35, #60) está en pending.md.
- *guest*, el personaje que se une al grupo → «personaje invitado» (SMT V: *Guest Characters* ⇒ *Personajes invitados*). «A guest has joined the party.» (event/quest/QuestSys.mbm#4) → «Un personaje invitado se unió al grupo», que además no marca género (DECISIONS 2026-11-09). En *u have a guest!!!* (SubQuestData) es «visita», ya traducido.

#### Aplicación de lo decidido

Términos de la sección que salen directamente de una decisión del glosario (fila, patrón o tabla ya traducida). No hay elección nueva; van para que el traductor y el validador los tengan a mano (G-3).

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Earthy man | Hombre rústico | Patrón de etiquetas (Tablas) y npc_room/NpcRoomTable.tbb#1.923.38 | Etiqueta de quien habla (24 líneas, npc_room/n075/n075.mbm). Es el que cuida la granja: «rústico» le va. G-3: igual que la tabla. |
| Chubby man | Hombre regordete | Patrón de etiquetas y NpcRoomTable.tbb#1.296.38 | Etiqueta (7 líneas, npc_room/n028/n028.mbm). |
| Anxious man | Hombre ansioso | Patrón de etiquetas y NpcRoomTable.tbb#1.917.38 | Etiqueta (7 líneas, npc_room/n063/n063.mbm). |
| Grumpy man | Hombre gruñón | Patrón de etiquetas y NpcRoomTable.tbb#1.1037.38 | Etiqueta (1 línea). |
| Starving man | Hombre hambriento | Patrón de etiquetas y NpcRoomTable.tbb#1.344.38 | Etiqueta (2 líneas). |
| Hunter man | Cazador | NpcRoomTable.tbb#1.108.38 y *Male Hunter* → «Cazador» (Historia) | Etiqueta (npc_room/n044/n044.mbm#0). |
| Vanguard leader | Líder de la vanguardia | Patrón de etiquetas y NpcRoomTable.tbb#1.1419.38 | Etiqueta (npc_room/n114/n114.mbm#0). |
| Sleepy fairy | Hada somnolienta | Patrón de etiquetas (Tablas; es el ejemplo del patrón) | Etiqueta (7 líneas). |
| Mischievous fairy | Hada traviesa | Patrón de etiquetas y NpcRoomTable.tbb | Etiqueta (6 líneas). |
| High-strung fairy | Hada nerviosa | Patrón de etiquetas y NpcRoomTable.tbb | Etiqueta (6 líneas). |
| Happy fairy | Hada feliz | Patrón de etiquetas y NpcRoomTable.tbb | Etiqueta (5 líneas). |
| Amiable fairy | Hada amable | Patrón de etiquetas y NpcRoomTable.tbb | Etiqueta (4 líneas). |
| Bitter fairy | Hada amargada | Patrón de etiquetas y NpcRoomTable.tbb | Etiqueta (3 líneas). |
| Ring of Gaea member | Miembro de Gea | Decidido por el usuario (2026-11-10), como la tabla ya traducida | Etiqueta (33 líneas). Antes «Miembro del Anillo de Gea» (Tablas); queda la forma corta de npc_room/NpcRoomTable.tbb (101 entradas). |
| Ashura-kai member | Miembro del Ashura-kai | Decidido en Tablas | Etiqueta (3 líneas); la tabla ya lo dice así. |
| Maitreya cultist | Devoto de Maitreya | Decidido en Historia | Etiqueta (3 líneas). |
| Commander | comandante | event/PartnerTopic/PartnerTopicTable.tbb (*I am indebted to the Commander* → «Estoy en deuda con el comandante») | event/PartnerTopic/PartnerTopic.mbm, 2 textos. En minúscula (E-59). |
| Commander Hope | comandante Hope | *Commander* → «comandante» y *Hope* como nombre propio (PENDING, lote historia-010) | event/PartnerTopic/PartnerTopic.mbm, 2 textos. |
| Hunter HQ | sede de los Cazadores | *Hunter Association HQ* → «Sede de la Asociación de Cazadores» (Tablas) | Forma corta (event/quest, 2 textos: *the new Hunter HQ in Kasumigaseki*, *return to the Hunter HQ*). |
| HQ | sede | Como *Hunter HQ* | «a package for you, from HQ» (quest_center, 2 líneas) → «de la sede». |
| Association | Asociación | *Hunter Association* → «Asociación de Cazadores» (decidido); PartnerTopicTable.tbb ya dice «Informé a la Asociación...» | Forma corta (16 textos: *The Association will pay extra*, *an Association record*). |
| Liberator | Libertador | Decidido en Tablas («se confirma con las Negociaciones») | 3 textos aquí (event/PartnerTopic/PartnerTopic.mbm, npc_room). PartnerTopicTable.tbb ya dice «¡Ese es nuestro Libertador!». Se confirma. |
| Master | amo | Decidido en Tablas (cuando un acompañante le habla al jugador) | 3 textos aquí, de un acompañante al jugador (event/quest/quest022.mbm#5, event/PartnerTopic/PartnerTopic.mbm). PartnerTopicTable.tbb ya dice «Trabajemos juntos, amo». Se confirma. *Master Bracelet* es el objeto (Tablas). |
| Master Bracelet | Pulsera del maestro | Decidido en Tablas (patrón de accesorios) | El objeto (item/ItemTable.tbb). Fila para que check.py no lo confunda con *Master* → «amo». |
| request | encargo | Decidido en Historia («se confirma en Secundarias») | Aquí es sustantivo una sola vez: «Kind of a luxurious request in these lean times» (event/quest/quest117.mbm#0). En las otras 3 es el verbo (*I humbly request that you...*). Se confirma. |
| Aoyama Cemetary | Cementerio de Aoyama | Lugares (Tablas) y map/all/MapYukaTable.tbb#2.123.0 | Error del inglés (§6: se señala, no se corrige): *Cemetary* por *Cemetery* (event/quest, 1 texto). |
| Ogunohara Park | Parque Ogunohara | Patrón *Park* → «Parque X» y MapYukaTable.tbb#2.126.0 («Ruinas del Parque Ogunohara») | «the ruins of Ogunohara Park» → «las ruinas del Parque Ogunohara» (event/quest, 1 texto). |
| Sakurada Way | calle Sakurada | Patrón *Ameyoko Way* → «Calle Ameyoko» | «the elevator on Sakurada Way» (event/quest/quest013.mbm#2). En minúscula a media frase (E-59). |
| Kenji | Kenji | Patrón: los nombres propios de IVA se dejan igual | 16 textos. |
| Nicho | Nicho | Patrón: los nombres japoneses de lugares se dejan igual | 2 textos. |
| Club Milton | Club Milton | Patrón: nombres propios de locales | 1 texto (con *Dogenzaka* → «Dogenzaka»). |

#### Revisados sin fila

De los 202 términos de `system-terms-secundarias.tsv`: 48 ya tienen fila en GLOSSARY.md (Hunter, Ring of Gaea, Macca, Champion, Terminal...). De los 154 restantes:

- **106** ya están cubiertos por una decisión del glosario: nombres propios que se dejan igual (Flynn, Nozomi, Toki, Gaston, Krishna, Shesha...), distritos y lugares con su patrón (Kinshicho, Tsukiji Konganji, *Tokyo Station* → «Estación de Tokio», *Fairy Forest*, *Eastern Kingdom of Mikado*, *Tokugawa Mandala*...), objetos de Tablas (*Red Earring*, *Sage Bracelet*, *Steel Bazooka*, *Panic Rounds*, *Shesha Radar*...), tratamientos (*Lord X*, *Lady X*, *Ladies Mii*, *Mr.*, *Dr.*) y los que van arriba en «Aplicación de lo decidido». *Expanse Meat* sigue en PENDING (Datos).
- **30** son palabras comunes que el script trajo como etiquetas de SMT V y que en esta sección no son términos: *new, place, hard, other, end, pass, special, off, dummy, always, next, return, start, 1st, 2nd, old, set, sound, fast, open, normal, remove, registered, none, original, guard, move, close, safety, all*.
- **13** son gritos, tartamudeos o fragmentos: *I-I*, *It’s Betty*, *CAN*, *NOT*, *IS*, *MIA*, *Th-The* + cinco objetos ya decididos, *P-Panic Rounds* y *Delivery Quest Description Second Time* (relleno, ver pending.md).
- **5** van a pending.md: *Log* (como *quest log*), *Champion Tournament*, *Number One*, *Bay Area*, *Wailing Gate*.

Etiquetas de quien habla en inglés (27 distintas): 9 ya decididas (Hunter, Burroughs, Angel, Demon, Asahi, Fujiwara, Ashura-kai member, Maitreya cultist, Ring of Gaea member), 13 por el patrón de Tablas y la tabla traducida (arriba), 3 ya en PENDING (*Bartender*, *New bartender* y *Bartender* con espacio) y 2 nuevas (*Neurisher*, *Medic*). Las etiquetas en japonés no se tratan (T-6).

#### Decididos por el usuario: Secundarias

Aprobados en bloque el 2026-11-10 (propuestas del terminólogo), sin artículo: la frase lo pone según el contexto.

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
| Bartender | Bartender | Decidido por el usuario (2026-11-10): se deja en inglés, se entiende bien | Etiqueta (274 líneas de quest_center, 6 de Historia), también en NpcHaichiTable.tbb y a media frase en minúscula («el bartender»). La etiqueta con espacio final (`{F812}Bartender {0000}`, center14_b.mbm#105-107) va igual, sin el espacio. |
| New bartender | Nuevo bartender | Decidido por el usuario (2026-11-10) | Etiqueta (44 líneas). |
| quest log | lista de misiones | Decidido por el usuario (2026-11-10) | quest_center/center/*.mbm#9 (13 tabernas). |
| delivery quest | misión de entrega | Decidido por el usuario (2026-11-10) | quest_center, event/quest/QuestSys.mbm#39. |
| give up | abandonar | Decidido por el usuario (2026-11-10) | Como *abandon* (event/quest/QuestSys.mbm#35, #60). |
| Champion Tournament | Torneo de Campeones | Decidido por el usuario (2026-11-10) | 52 líneas de la taberna. |
| ranking | clasificación | Decidido por el usuario (2026-11-10) | 102 líneas (*the ranking column* → «la columna de la clasificación»). |
| Number One | Número Uno | Decidido por el usuario (2026-11-10) | Con mayúsculas, como el grafiti del inglés. |
| bulletin board | tablero de anuncios | Decidido por el usuario (2026-11-10) | 78 líneas (E-10, E-12). |
| Armageddon | Armagedón | Decidido por el usuario (2026-11-10): excepción a G-1 | SMT V dice «apocalipsis», que chocaría con el subtítulo y la dificultad «Apocalipsis». |
| Bay Area | región costera | Decidido por el usuario (2026-11-10) | Como la *coastal region* del mapa (Historia). |
| Wailing Gate | Puerta de los Lamentos | Decidido por el usuario (2026-11-10) | event/quest/quest022.mbm#2 y contenido descargable (content24/evt/e220). |
| King of Tokyo | Rey de Tokio | Decidido por el usuario (2026-11-10) | Título, con mayúscula. |
| Hunter Notes | Notas del Cazador | Decidido por el usuario (2026-11-10), provisional | Si es un menú del juego, va su nombre; se ve en el juego. |
| Neurisher | Neurodonante | Decidido por el usuario (2026-11-10), provisional | Palabra inventada: pasa por delicadas (npc_room/n074/n074.mbm). |
| Medic | Personal médico | Decidido por el usuario (2026-11-10) | No marca género (npc_room/n114/n114.mbm#1). |

Condiciones de las misiones (event/quest/QuestSys.mbm), en infinitivo como los objetivos de QuestData: *Deliver* → «Entregar», *Slay* → «Eliminar», *Show* → «Mostrar», *Collect* → «Reunir», *Bring a demon that has...* → «Traer un demonio que tenga...», *Accomplish* → «Lograr». No van en la tabla: son verbos comunes.
