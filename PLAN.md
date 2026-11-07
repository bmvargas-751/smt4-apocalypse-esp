# Plan

## Decisiones

- **Variante:** español neutro (*tú*/*ustedes*, sin regionalismos de ningún país), como en The Hundred Line.
- **Base:** el inglés oficial. El japonés solo resuelve género, sujeto omitido y trato; la versión japonesa se consigue cuando haga falta.
- **Terminología:** la de la traducción oficial de *SMT V: Vengeance* en lo que comparte con IVA (demonios, habilidades, razas, estados, objetos). Se toma el término, no el registro: esa traducción es, casi seguro, de España. Lo propio de IV e IVA se decide aquí y va al glosario.
- **Versión base:** la europea (`CTR-P-BG4P`, ID `00040000001A6B00`), sin actualización. Es la copia del usuario, ya descifrada.
- **Pruebas:** en emulador (Azahar). La partida, que avanza junto con la traducción, es la prueba en el juego.
- **Sin spoilers:** los documentos, los commits y el chat nombran zonas o archivos, nunca hechos de la historia.
- **Contenido del repo:** como en THL, solo nuestra traducción y nuestras herramientas.

## Pendiente de decidir

1. **El encargo original del prompt de editor de THL** (las 11 secciones). Si está el texto, los roles parten de él; si no, de su resumen.
2. **Dónde vive el equipo.** Propuesta: un repo propio, como translation-reviewer, con los roles, las plantillas y los chequeos generales. Aquí quedaría solo lo de IVA. Mientras tanto, [TEAM.md](TEAM.md) vive aquí.
3. **Cómo se ejecuta.** Propuesta: subagentes de Claude Code, un archivo por rol en `.claude/agents/` con su modelo y su esfuerzo, llamados en orden por una skill. El modelo y el esfuerzo de cada rol se deciden con el piloto.
4. **Registro solemne** (dioses y demonios que hablan de época). En THL quedó «de época, sin *vosotros*»; confirmar si se mantiene.

## Fases

### Fase 0. Antes de empezar

- [x] Verificar si existe una traducción fan de IVA al español: no hay ninguna (2026-11-07). Se hace desde cero.
- [x] Revisar la versión del juego: europea, sin actualización.

### Fase 1. Prueba técnica

Antes de esto no se decide nada más.

- [x] Extraer los archivos del juego: `tools/ctr.py extract`, a una carpeta fuera del repo.
- [x] Ida y vuelta de los mensajes (`.mbm`): 1243 de 1243 archivos idénticos (`tools/mbm.py roundtrip`).
- [ ] Ida y vuelta del resto del texto: tablas (`.tbb`), ejecutable y texturas.
- [ ] Una línea con «¿Ñandú? ¡Sí!» en el emulador: mod armado con `pruebas/fuente.jsonl` (mensajes de crear datos, guardar y cargar), falta verlo en el juego.
- [ ] Pseudolocalización: todo el texto un 35% más largo, con á é í ó ú ü ñ, sus mayúsculas, ¿ ¡ y un ID corto por línea. Jugar una hora (menús, combate, negociación, compendio) y anotar los glifos que faltan en cada fuente, los cortes, los cuelgues y el texto que no cambió (está en el ejecutable o en una textura).
- [ ] Límites: ancho de cada caja en píxeles, renglones por caja y bytes de los campos fijos. Los saltos de línea los pone el texto (`{F801}`), así que los renglones se parten aquí.
- [x] Fuente: las 16 letras (á é í ó ú ü ñ, sus mayúsculas, ¿ ¡) dibujadas en las 4 fuentes (`tools/fuente.py`), en los códigos del cirílico (`tools/letras.py`).

### Fase 2. Inventario y presupuesto

- [ ] Volumen por tipo de texto: historia, secundarias, negociaciones, descripciones, interfaz, combate.
- [ ] Costo por pasada (en THL: ~25k tokens leídos y ~18k escritos cada 250 líneas) y cuántas pasadas recibe cada tipo.

### Fase 3. Documentos

- [ ] Glosario alineado con *SMT V: Vengeance*: sus tablas en inglés y en español, emparejadas por ID, con las fórmulas de las descripciones. Lo extraído queda local.
  - [ ] El usuario instala *SMT V: Vengeance* para sacar sus tablas.
- [ ] Guía de estilo: la parte general de la de THL, con las reglas numeradas para que los revisores las citen.
- [ ] Fichas de personajes: género, trato con cada uno, muletillas, groserías.
- [ ] Fichas por personalidad para las negociaciones.
- [ ] Reglas técnicas: códigos de control, límites, saltos de línea.
- [ ] Registro de decisiones.

### Fase 4. Herramientas

- [ ] Adaptador del juego: medir ancho y bytes. Extraer e insertar ya están (`tools/ctr.py`, `tools/mbm.py`).
- [ ] Chequeos desde el primer día, con los barridos de THL (y → e, o → u, signos, comillas, léxico regional, calcos frecuentes, mayúsculas, género).
- [ ] Memoria de traducción: una línea repetida se traduce una vez.
- [x] Instalador (`instalar.py`, `instalar.bat`): arma la traducción desde la copia del jugador y la instala en Azahar, Citra o la SD de una 3DS con Luma3DS. Trae desinstalador y no reparte archivos del juego.
- [x] Avance por sección (`tools/avance.py --readme`), en el README y en [traduccion/README.md](traduccion/README.md).

### Fase 5. Piloto

- [ ] 300 a 500 líneas del comienzo, de todos los tipos, por el equipo completo, con revisión humana de todas.
- [ ] Ajustar documentos y roles con lo que salga.
- [ ] Set de oro: líneas con su traducción buena y sus trampas, para probar cada cambio de prompt.

### Fase 6. Traducción

Datos e interfaz primero; después la historia en orden, las secundarias y las negociaciones por personalidad. Siempre por delante de la partida. Qué entra en cada sección: [traduccion/README.md](traduccion/README.md).

- [ ] 6.1 Interfaz
- [ ] 6.2 Tablas
- [ ] 6.3 Datos
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
- **Tablas (`.tbb`):** guardan nombres y textos cortos en ASCII de un byte (objetos, razas, misiones, lugares, descripciones de menús). Ahí la «á» no puede usar el código de dos bytes de los mensajes; hace falta un código de un byte.
- **Japonés que quedó en los archivos:** 2844 mensajes, la mayoría (unos 2000) en los mensajes de demonios en combate (`battle/DevilMsg`, `camp/CecDevilMsg`). Ver si el juego los muestra antes de contarlos para traducir.

## Referencias

- [Texto sin traducir en IVA](https://www.nintendolife.com/news/2016/09/atlus_issues_apology_for_smtiva_translation_error) (Nintendo Life)
