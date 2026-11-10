# Plan

## Decisiones

- **Variante:** español neutro (*tú*/*ustedes*, sin regionalismos de ningún país), como en The Hundred Line.
- **Base:** el inglés oficial. El japonés solo resuelve género, sujeto omitido y trato; la versión japonesa se consigue cuando haga falta.
- **Terminología:** la de la traducción oficial de *SMT V: Vengeance* en lo que comparte con IVA (demonios, habilidades, razas, estados, objetos). Se toma solo el término; el registro es siempre el de esta traducción: español neutro, natural y nunca literal. Lo propio de IV e IVA se decide aquí y va al glosario.
- **Versión base:** la europea (`CTR-P-BG4P`, ID `00040000001A6B00`), sin actualización. Es la copia del usuario, ya descifrada.
- **Pruebas:** en emulador (Azahar). La partida, que avanza junto con la traducción, es la prueba en el juego.
- **Sin spoilers:** los documentos, los commits y el chat nombran zonas o archivos, nunca hechos de la historia.
- **Contenido del repo:** como en THL, solo nuestra traducción y nuestras herramientas.

## Pendiente de decidir

Las decisiones de traducción pendientes están en [PENDING.md](PENDING.md) (el encargo original, el registro de época, «¡Demonios!»).

1. **Dónde vive el equipo.** Propuesta: un repo propio, como translation-reviewer, con los roles, las plantillas y los chequeos generales. Aquí quedaría solo lo de IVA. Mientras tanto, el equipo vive aquí ([TEAM.md](TEAM.md), [.claude/](.claude)).

## Fases

### Fase 0. Antes de empezar

- [x] Verificar si existe una traducción fan de IVA al español: no hay ninguna (2026-11-07). Se hace desde cero.
- [x] Revisar la versión del juego: europea, sin actualización.

### Fase 1. Prueba técnica

Antes de esto no se decide nada más.

- [x] Extraer los archivos del juego: `tools/ctr.py extract`, a una carpeta fuera del repo.
- [x] Ida y vuelta de los mensajes (`.mbm`): 1243 de 1243 archivos idénticos (`tools/mbm.py roundtrip`).
- [x] Ida y vuelta de las tablas (`.tbb`): 489 de 489 archivos idénticos (`tools/tbb.py roundtrip`). 6.757 textos para traducir, con su largo máximo en bytes.
- [ ] Ida y vuelta del ejecutable (`code.bin`): tiene unos mil textos de interfaz en inglés de ancho completo (elementos, estados, mensajes cortos).
- [ ] Ida y vuelta de las texturas con texto.
- [ ] Una línea con «¿Ñandú? ¡Sí!» en el emulador, con `install.py --test`: mensajes de crear datos, guardar y cargar (`tests/font.jsonl`) y menú de título, que es de una tabla (`tests/tables.jsonl`). Falta verlo en el juego.
- [ ] Pseudolocalización: todo el texto un 35% más largo, con á é í ó ú ü ñ, sus mayúsculas, ¿ ¡ y un ID corto por línea. Jugar una hora (menús, combate, negociación, compendio) y anotar los glifos que faltan en cada fuente, los cortes, los cuelgues y el texto que no cambió (está en el ejecutable o en una textura).
- [ ] Límites: ancho de cada caja en píxeles, renglones por caja, ancho de la etiqueta con el nombre de quien habla (`{F812}`) y bytes de los campos fijos. Los saltos de línea los pone el texto (`{F801}`), así que los renglones se parten aquí.
- [x] Fuente: las 16 letras (á é í ó ú ü ñ, sus mayúsculas, ¿ ¡) dibujadas en las 4 fuentes (`tools/font.py`), en los códigos del cirílico (`tools/letters.py`).

### Fase 2. Inventario y presupuesto

- [ ] Volumen por tipo de texto: historia, secundarias, negociaciones, descripciones, interfaz, combate.
- [ ] Costo por pasada (en THL: ~25k tokens leídos y ~18k escritos cada 250 líneas) y cuántas pasadas recibe cada tipo.

### Fase 3. Documentos

- [x] Leer *SMT V: Vengeance*: `tools/smt5v.py` (con ooz, de `tools/build_ooz.sh`) empareja sus nombres en inglés y en español por posición. Lo extraído queda local.
- [ ] Glosario ([GLOSSARY.md](GLOSSARY.md)): el terminólogo revisa los 317 candidatos de SMT V que aparecen en IVA y, antes de cada sección, sus términos de sistema (`tools/smt5v.py terms`), y propone las filas. Hechos: los 317 candidatos (343 filas oficiales; 29 por decidir en PENDING) y la Interfaz (2026-11-08).
- [x] Guía de estilo ([STYLE.md](STYLE.md)): la parte general de la de THL y el encargo, con las reglas numeradas para que los revisores las citen.
- [ ] Fichas de personajes ([characters/](characters)): género, trato con cada uno, muletillas, groserías. Plantilla lista; las escribe el perfilador. Hechas: las 9 de la Interfaz (2026-11-08).
- [ ] Fichas por personalidad para las negociaciones.
- [x] Reglas técnicas ([TECH.md](TECH.md)): códigos de control, saltos, caja, bytes y caracteres.
- [x] Registro de decisiones ([DECISIONS.md](DECISIONS.md)) y cola de pendientes ([PENDING.md](PENDING.md)).

### Fase 4. Herramientas

- [x] Adaptador del juego: extraer, insertar, medir el ancho en píxeles y los bytes, y partir los renglones (`tools/ctr.py`, `mbm.py`, `tbb.py`, `layout.py`).
- [x] Chequeos (`tools/check.py`), con los de THL (y → e, o → u, signos, comillas, léxico regional, vosotros, glosario) y los de IVA (códigos, saltos, caja, bytes, caracteres). Cada aviso cita su regla.
- [x] Memoria de traducción: una línea repetida se traduce una vez y se copia a las idénticas (`tools/batch.py`).
- [x] Equipo: los roles como agentes con su modelo y su esfuerzo (`.claude/agents/`), la skill que los ordena (`translate-batch`) y los controles contra reglas inventadas (`tools/review.py`). Ver [TEAM.md](TEAM.md).
- [x] Instalador (`install.py`, `install.bat`): arma la traducción desde la copia del jugador y la instala en Azahar, Citra o la SD de una 3DS con Luma3DS. Trae desinstalador y no reparte archivos del juego.
- [x] Avance por sección (`tools/progress.py --readme`), en el README y en [translation/README.md](translation/README.md).

### Fase 5. Piloto

- [ ] Piloto de la Interfaz: su primer lote (250 líneas), por el equipo completo, con revisión del usuario de todas las líneas.
- [ ] Piloto de diálogos: al llegar a la Historia.
- [ ] Ajustar documentos y roles con lo que salga.
- [ ] Set de oro: líneas con su traducción buena y sus trampas, para probar cada cambio de prompt.

### Fase 6. Traducción

Datos e interfaz primero; después la historia en orden, las secundarias y las negociaciones por personalidad. Siempre por delante de la partida. Qué entra en cada sección: [translation/README.md](translation/README.md).

- [x] 6.1 Interfaz (2026-11-08)
- [x] 6.2 Tablas (2026-11-09)
- [x] 6.3 Datos
- [ ] 6.4 Historia
- [ ] 6.5 Secundarias
- [ ] 6.6 Negociaciones
- [ ] 6.7 Demonios en combate
- [ ] 6.8 Contenido descargable

### Fase 7. Entrega

- [ ] Idealmente, una prueba en una 3DS real.
- [ ] Registro de cambios y publicación.

## Notas de IVA

- **Negociaciones:** si una misma línea la dicen demonios de distinto género, no puede marcar el género del que habla («¡Qué cansancio!», no «Estoy cansado»). Verificar al extraer.
- **Nombres insertados** (demonio, objeto, cantidad): sin artículo ni participios con género; fórmulas como «Obtienes: X».
- **«¡Demonios!» y «¡Diablos!»** se vuelven ambiguas en este juego: decidir si se evitan.
- **Japonés en la versión inglesa:** dos escenas cerca del final quedaron sin traducir. Atlus prometió un parche, pero no hay confirmación de que haya salido. Se traducen desde el japonés.
- **Límites:** con fuente proporcional se mide en píxeles; en los campos fijos, en bytes. En los mensajes cada carácter ocupa 2 bytes, también la «á».
- **Tablas (`.tbb`):** guardan nombres y textos cortos en ASCII de un byte, en campos de largo fijo (objetos, demonios, razas, misiones, lugares, descripciones de menús). Las letras españolas usan los mismos códigos de dos bytes que los mensajes, porque son Shift-JIS válido, como el japonés que también traen las tablas; cuestan un byte más cada una. Falta comprobarlo en el juego. Si en el juego no se ven, la alternativa es un código de un byte (el katakana de un byte, que la fuente trae).
- **Nombres de demonios:** están en `battle/NKMSortIndex.tbb`, con marcadores internos («Reserved», «Dummy», «(Giant)») que no se muestran.
- **Japonés que quedó en los archivos:** 2844 mensajes, la mayoría (unos 2000) en los mensajes de demonios en combate (`battle/DevilMsg`, `camp/CecDevilMsg`). Ver si el juego los muestra antes de contarlos para traducir.

## Referencias

- [Texto sin traducir en IVA](https://www.nintendolife.com/news/2016/09/atlus_issues_apology_for_smtiva_translation_error) (Nintendo Life)
