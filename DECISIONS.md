# Registro de decisiones

Las decisiones del usuario, con fecha. Una regla nueva de [STYLE.md](STYLE.md), [TECH.md](TECH.md) o [GLOSSARY.md](GLOSSARY.md) se anota aquí cuando sale de una decisión.

- **2026-11-05** Español neutro, como en The Hundred Line (STYLE E-10 a E-13).
- **2026-11-05** Base: el inglés oficial. El japonés solo resuelve género, sujeto omitido y trato (E-1).
- **2026-11-05** Terminología: la de *SMT V: Vengeance* en lo que comparte con IVA (G-1).
- **2026-11-05** Pruebas en emulador. La partida del usuario, que avanza junto con la traducción, es la prueba en el juego.
- **2026-11-07** Versión base: la europea (`00040000001A6B00`), sin actualización.
- **2026-11-07** Instalador propio para Azahar, Citra y la SD de una 3DS con Luma3DS, que arma la traducción desde la copia de cada jugador.
- **2026-11-07** El proyecto se hace desde cero, con herramientas propias.
- **2026-11-07** Nombres de archivos, carpetas, opciones y código en inglés; documentos, comentarios y mensajes al jugador en español.
- **2026-11-07** Secciones de la traducción (fase 6) y su avance en el README.
- **2026-11-07** Modelo y esfuerzo de cada rol ([TEAM.md](TEAM.md#roles)) como punto de partida; se ajustan con el piloto y el set de oro. max solo si lo pide el usuario.
- **2026-11-07** Controles contra reglas inventadas ([TEAM.md](TEAM.md#controles)).
- **2026-11-07** «Español neutro, natural, 0 literal» (STYLE E-10). De SMT V se toma solo el término (G-1); los documentos no nombran otra variedad de español.
- **2026-11-07** Prompts de los 7 roles aprobados (control 1 de [TEAM.md](TEAM.md#controles)).
- **2026-11-07** Antes de traducir una sección, el terminólogo revisa sus términos (`tools/smt5v.py terms --section SECCIÓN`) y el usuario decide los *por decidir*. Así la Interfaz no fija palabras sobre la marcha.
- **2026-11-07** G-1 se amplía a los términos de sistema y de menú que IVA comparte con SMT V (*Demon Compendium*, *Macca*, *Save Data*), sacados de sus menús y textos de sistema.
- **2026-11-07** Antes de la Interfaz, el perfilador escribe las fichas de quienes hablan en ella.
- **2026-11-07** El primer lote de la Interfaz (250 líneas) es su piloto, con revisión del usuario de todas las líneas, y de él sale el primer set de oro. El piloto de diálogos se hace al llegar a la Historia.
- **2026-11-08** Fichas de la Interfaz aprobadas ([characters/](characters)). Trato con el jugador (E-30): *usted* para Mido (y Suspicious man), Saint Germain, Spirit of the Spring y System voice; *tú* para Napaea, Hooded man, Charon y Shopkeeper. Los demás mensajes de sistema, con *tú*.
- **2026-11-08** El género de Saint Germain, Spirit of the Spring y Shopkeeper queda pendiente: ninguna línea de la Interfaz lo necesita. Si una lo necesita, va a [PENDING.md](PENDING.md).
- **2026-11-08** El registro de época (E-31) se decide al llegar a la Historia. Mientras, «Ye gods» de Charon (`battle/ResultMsg.mbm#17`) pasa por el agente de líneas delicadas con una solución provisional.
- **2026-11-08** Glosario de la Interfaz aprobado: 343 filas oficiales de SMT V (G-1) y 90 términos decididos (G-2), con las recomendaciones del terminólogo y del orquestador ([GLOSSARY.md](GLOSSARY.md)). *Terminal* va en femenino. Los menús de la consola, *Book/View/Overwrite*, *ON/OFF*, los pisos del ascensor y las terminales de Mikado y Sky quedan *provisionales* hasta verlos en el juego.
- **2026-11-08** Los 28 candidatos con otro sentido que no salen en la Interfaz (y la raza *Divine*) se deciden al llegar a su sección ([PENDING.md](PENDING.md#términos)). *Nebiros* lleva el nombre de SMT V, *Naberius* (G-1).
- **2026-11-08** El revisor y el editor no ejecutan `tools/review.py` ni editan `translation/`: lo hace el orquestador (en dos lotes lo hicieron por su cuenta).
- **2026-11-08** *2nd Brane* → «Brana 2» (la fuente no tiene «ª»). Los términos de sistema van en minúscula a media frase (E-59). Al jugador se le da la bienvenida con «Bienvenido» (es masculino según las fichas). «Ofertas», no «rebajas».
- **2026-11-08** Recomendaciones del piloto aprobadas: «¡Envenenaron a X!» (E-42) y «Por favor» en los avisos que lo traen en inglés. *Macca* sigue como en la tabla.
- **2026-11-08** *performance* → «capacidades». *Search/Special/End* → «Buscar/Especial/Terminar», provisionales.
- **2026-11-08** Interfaz: se traducen por si acaso las 2 líneas en japonés con sentido (Burroughs y el aviso de terminal); las 17 de relleno o prueba («ダミー», el silabario) quedan fuera de la cuenta.
- **2026-11-08** Glosario de Tablas aprobado: 41 filas oficiales, 13 términos y los patrones del terminólogo ([GLOSSARY.md](GLOSSARY.md#tablas)). Raza + nombre siempre (T-1). *Sky Terminal* → «Terminal de Sky Tower». Quedan en PENDING: Luxurors/Casualries, *Jack Union*, el prefijo *A.*, las categorías de misión y *Bartender*.
- **2026-11-09** Tablas: «Matadioses» en battle/NKMSortIndex.tbb (1 px sobre la columna) y «Asoc. Cazadores» en la lista de misiones (event/quest/QuestData.tbb) se dejan así; se comprueba en el juego si dan problemas.
- **2026-11-09** Glosario de Datos aprobado: 45 filas oficiales, 20 términos decididos y los patrones del terminólogo ([GLOSSARY.md](GLOSSARY.md#datos)). *Expanse* → «Inmensidad», *Lost* → «Perdido», *KO* → «K.O.», *buffs* → «efectos positivos» también en la Interfaz, *Power* → «Potencia», *Ceiling* → «Techo», *Shogunate* → «shogunato», *Gaea* del perfil #512 → «Gaia». *Limit* y *Brand*, provisionales. Quedan fuera de la cuenta el relleno de Datos y los mensajes sin texto (solo códigos).
- **2026-11-09** El ancho de la caja (T-3) es un aviso, no un límite: abreviaturas reconocibles sí; quitar palabras o acortar perdiendo el sentido, no. Si no cabe, va completo con su aviso y se revisa en el juego. Los bytes de las tablas (T-4) siguen siendo un límite duro.
- **2026-11-09** datos-002: *hoity toity* → «pretencioso» (item/ItemHelpMess.mbm#1035) queda así. «una Nue» (#901) y «un Mamedanuki» (#920) son criaturas distintas, cada una con su género: no hay nada que igualar.
