# Plan

## Decisiones

- **Variante:** español neutro (*tú*/*ustedes*, sin regionalismos de ningún país), como en The Hundred Line.
- **Base:** el inglés oficial. El japonés solo resuelve género, sujeto omitido y trato; la versión japonesa se consigue cuando haga falta.
- **Terminología:** la de la traducción oficial de *SMT V: Vengeance* en lo que comparte con IVA (demonios, habilidades, razas, estados, objetos). Se toma el término, no el registro: esa traducción es, casi seguro, de España. Lo propio de IV e IVA se decide aquí y va al glosario.
- **Pruebas:** en emulador (Azahar). La partida, que avanza junto con la traducción, es la prueba en el juego.
- **Sin spoilers:** los documentos, los commits y el chat nombran zonas o archivos, nunca hechos de la historia.
- **Contenido del repo:** como en THL, solo nuestra traducción y nuestras herramientas.

## Pendiente de decidir

1. **El encargo original del prompt de editor de THL** (las 11 secciones). Si está el texto, los roles parten de él; si no, de su resumen.
2. **Dónde vive el equipo.** Propuesta: un repo propio, como translation-reviewer, con los roles, las plantillas y los chequeos generales. Aquí quedaría solo lo de IVA. Mientras tanto, [TEAM.md](TEAM.md) vive aquí.
3. **Cómo se ejecuta.** Propuesta: subagentes de Claude Code, un archivo por rol en `.claude/agents/` con su modelo y su esfuerzo, llamados en orden por una skill. El modelo y el esfuerzo de cada rol se deciden con el piloto.
4. **Versión base.** Propuesta: la americana. El parche de SMT IV de Projeto Amala funciona bien en la americana y solo a medias en la europea.
5. **Otras traducciones fan.** Si existe una de SMT IV al español, decidir si se consulta.
6. **Registro solemne** (dioses y demonios que hablan de época). En THL quedó «de época, sin *vosotros*»; confirmar si se mantiene.

## Fases

### Fase 0. Antes de empezar

- [ ] Escribir a Projeto Amala, que tradujo SMT IV al portugués (IVA usa el mismo motor), por sus herramientas o notas: extraer e insertar texto, fuente y texturas.
- [ ] Verificar si existe una traducción fan de SMT IV al español (hay un titular en Noisy Pixel, sin confirmar) y si alguien está traduciendo IVA.
- [ ] Revisar la versión del juego: región y actualización.

### Fase 1. Prueba técnica

Antes de esto no se decide nada más.

- [ ] Ida y vuelta: extraer e insertar el texto sin cambios da archivos idénticos.
- [ ] Una línea con «¿Ñandú? ¡Sí!» en el emulador.
- [ ] Pseudolocalización: todo el texto un 35% más largo, con á é í ó ú ü ñ, sus mayúsculas, ¿ ¡ y un ID corto por línea. Jugar una hora (menús, combate, negociación, compendio) y anotar los glifos que faltan en cada fuente, los cortes, los cuelgues y el texto que no cambió (está en el ejecutable o en una textura).
- [ ] Límites: ancho de cada caja en píxeles, renglones por caja, bytes de los campos fijos y si el motor parte las líneas solo.
- [ ] Fuente: agregar los glifos que falten.

### Fase 2. Inventario y presupuesto

- [ ] Volumen por tipo de texto: historia, secundarias, negociaciones, descripciones, interfaz, combate.
- [ ] Costo por pasada (en THL: ~25k tokens leídos y ~18k escritos cada 250 líneas) y cuántas pasadas recibe cada tipo.

### Fase 3. Documentos

- [ ] Glosario alineado con *SMT V: Vengeance*: sus tablas en inglés y en español, emparejadas por ID, con las fórmulas de las descripciones. Lo extraído queda local.
- [ ] Guía de estilo: la parte general de la de THL, con las reglas numeradas para que los revisores las citen.
- [ ] Fichas de personajes: género, trato con cada uno, muletillas, groserías.
- [ ] Fichas por personalidad para las negociaciones.
- [ ] Reglas técnicas: códigos de control, límites, saltos de línea.
- [ ] Registro de decisiones.

### Fase 4. Herramientas

- [ ] Adaptador del juego: extraer, insertar, medir ancho y bytes.
- [ ] Chequeos desde el primer día, con los barridos de THL (y → e, o → u, signos, comillas, léxico regional, calcos frecuentes, mayúsculas, género).
- [ ] Memoria de traducción: una línea repetida se traduce una vez.
- [ ] Parche para el emulador, sin la ROM.

### Fase 5. Piloto

- [ ] 300 a 500 líneas del comienzo, de todos los tipos, por el equipo completo, con revisión humana de todas.
- [ ] Ajustar documentos y roles con lo que salga.
- [ ] Set de oro: líneas con su traducción buena y sus trampas, para probar cada cambio de prompt.

### Fase 6. Traducción

Datos e interfaz primero; después la historia en orden, las secundarias y las negociaciones por personalidad. Siempre por delante de la partida.

### Fase 7. Entrega

- [ ] Idealmente, una prueba en una 3DS real.
- [ ] Registro de cambios y publicación.

## Notas de IVA

- **Negociaciones:** si una misma línea la dicen demonios de distinto género, no puede marcar el género del que habla («¡Qué cansancio!», no «Estoy cansado»). Verificar al extraer.
- **Nombres insertados** (demonio, objeto, cantidad): sin artículo ni participios con género; fórmulas como «Obtienes: X».
- **«¡Demonios!» y «¡Diablos!»** se vuelven ambiguas en este juego: decidir si se evitan.
- **Japonés en la versión inglesa:** dos escenas cerca del final quedaron sin traducir. Atlus prometió un parche, pero no hay confirmación de que haya salido. Se traducen desde el japonés.
- **Límites:** con fuente proporcional se mide en píxeles; en los campos fijos, en bytes (una «á» puede ocupar el doble).

## Referencias

- [Projeto Amala: SMT IV en portugués](https://noisypixel.net/shin-megami-tensei-iv-fan-pt-br-patch-released/) (Noisy Pixel)
- [Texto sin traducir en IVA](https://www.nintendolife.com/news/2016/09/atlus_issues_apology_for_smtiva_translation_error) (Nintendo Life)
