# Guía de estilo

Reglas de traducción de IVA. Cada regla tiene un número para que los revisores la citen en sus hallazgos. Las reglas técnicas (códigos, saltos, cajas, bytes, caracteres) están en [TECH.md](TECH.md) y los términos fijos, en [GLOSSARY.md](GLOSSARY.md).

Al final de cada regla se indica de dónde sale:
- **[THL]**: la guía de estilo de The Hundred Line.
- **[Encargo §N]**: tu encargo de 11 secciones, cuyo resumen está en [TEAM.md](TEAM.md#el-encargo).
- **[PLAN]**: las decisiones de [PLAN.md](PLAN.md).

Aquí no se agrega ninguna regla sin fuente.

## Base

- **E-1** Se traduce desde el inglés oficial, frase por frase y con el mismo sentido. El japonés solo resuelve género, sujeto omitido y trato. [PLAN] [THL]
- **E-2** Naturalidad antes que literalidad. Fidelidad: no se añade ni se quita información. Calidad literaria: ritmo, sin repeticiones y sin sinónimos artificiales. [Encargo §1]
- **E-3** No se agregan palabras que el original no dice. Si el inglés no lo dice y el español no lo necesita, no se añade. [THL]
- **E-4** Se lee el contexto: quién habla, a quién y qué pasó antes. Si algo es ambiguo, se señala; nunca se inventa contexto. [Encargo §7]
- **E-5** Se cambia solo con motivo: error, literalidad, artificialidad, fluidez, intención, localización, inconsistencia o género. Lo que ya está bien se deja, y no se inventan errores para justificar un cambio. [Encargo §10, §11]

## Español neutro

- **E-10** Español neutro y natural, nunca literal: como lo diría una persona en una conversación equivalente, comprensible en toda América y sin regionalismos marcados de ningún país. [THL] [Decisión 2026-11-07]
- **E-11** El plural es siempre *ustedes*, nunca *vosotros*:
  - Verbos en 3.ª persona del plural; pronombres *los/las*, *les* y *se* (*se lo dije*).
  - Posesivo *su*, o *de ustedes* si *su* queda ambiguo.
  - Imperativo con el subjuntivo (*descansen*, *vayan*). Si la frase queda ambigua con *ellos*, se reformula.

  [THL]
- **E-12** Vocabulario regional que se evita, con su forma neutra según el contexto y el registro del personaje: [THL]

  | Evitar | Usar |
  |---|---|
  | vale | está bien, de acuerdo, bueno, okey (según el tono) |
  | echar de menos | extrañar |
  | menudo (*menudo punto ciego*) | qué, vaya |
  | venga (ánimo) | vamos, anda |
  | tío/tía (= amigo) | amigo, viejo (casual) u omitir; *tío* (pariente) se mantiene |
  | guay, mola | genial, increíble, me encanta |
  | coger | tomar, agarrar, atrapar |
  | pillar | atrapar, entender, sorprender |
  | ordenador | computadora |
  | móvil | teléfono |
  | pasta (dinero) | dinero |
  | majo/maja | simpático, agradable |
  | gilipollas | idiota, imbécil |
  | joder | maldición, mierda, rayos (según la intensidad del original) |
  | enfadarse | enojarse |
  | pulsar (un botón) | presionar |
  | mando (de consola) | control |
  | ratón (de la computadora) | mouse |
  | vídeo | video |
  | castellano (nombre del idioma) | español |
  | bombona | cartucho, tanque, garrafa (según el objeto) |
  | destripe (spoiler) | spoiler |
  | gafas | lentes, anteojos |
  | bañador | traje de baño |
  | nevera | refrigerador |
  | mono/mona (= bonito) | lindo, tierno |
  | fardar | presumir |
  | motero | motociclista |
  | tragaperras | tragamonedas |
  | cristal (el material) | vidrio |
  | aparcamiento, aparcar | estacionamiento, estacionar |
  | jersey | suéter |
  | auriculares | audífonos |
  | seta | hongo |
  | coche | auto |
  | cubo de basura | bote de basura |
  | pendientes (joya) | aretes |
  | marcapáginas | separador |
  | ambientador | aromatizante |
  | taquilla (armario) | casillero |
  | diana (de dardos) | tablero de dardos |
  | pista (de tenis) | cancha |
  | chaval | chico |
  | judía (legumbre) | frijol |
  | megafonía | altavoz |
- **E-13** Tampoco van regionalismos latinoamericanos marcados: *¿ya?* por «¿sí?», *fome*, *lata*, *plata*, *tomar desayuno*, *chido*, *bacán*, *boludo*, *wey*, *pana*, *harto*, *po*, *cachai*, *recién*, *qué onda*, *nomás*. [THL]

## Localización y voz

- **E-20** Modismos, juegos de palabras, humor, sarcasmo, referencias culturales e insultos llevan un equivalente natural; no se conserva lo literal por fidelidad a las palabras. *idiot*, *moron* → *idiota*, *imbécil*; *tonto* solo para un *silly* o *dumb* suave. [Encargo §2] [THL]
- **E-21** Cada personaje habla como en el original: formalidad, vocabulario, humor, trato y peculiaridades. No todos hablan igual; tiene que sonar espontáneo, no a texto traducido ni demasiado formal. Lo de cada uno está en su ficha ([characters/](characters)). [Encargo §3]
- **E-22** Los tics van según el inglés: cortes, tartamudeos, jerga, muletillas y groserías. Las groserías no se suavizan ni se intensifican: igualan la intensidad del original. [THL]
- **E-23** Frases delicadas (juegos de palabras, muletillas, referencias, acertijos): se traducen desde el inglés con una solución provisional y se anotan en [PENDING.md](PENDING.md). No se agregan datos que el inglés no tiene. [THL]

## Trato

- **E-30** *Tú* por defecto; *usted* solo si la ficha del personaje lo dice. El trato depende de con quién habla, y se mantiene igual entre dos personajes durante todo el juego. [THL]
- **E-31** Registro de época (dioses y demonios que hablan a la antigua): pendiente de decidir ([PENDING.md](PENDING.md)). Mientras tanto, nunca *vosotros* (E-11). [PLAN]

## Género

- **E-40** Género y concordancia, con prioridad máxima:
  - Se revisan artículos, adjetivos, pronombres y participios.
  - El género no se deduce por el nombre ni se asume masculino.
  - Si hay duda, la línea queda pendiente.

  [Encargo §4]
- **E-41** Si una misma línea la dicen personajes de distinto género (pasa en las negociaciones), no puede marcar el género de quien habla: *¡Qué cansancio!*, no *Estoy cansado*. [PLAN]
- **E-42** Los nombres que el juego inserta (demonio, objeto, cantidad) van sin artículo ni participios con género, con fórmulas como *Obtienes: X*. [PLAN]

## Gramática y formato

- **E-50** Gramática, ortografía, puntuación, mayúsculas, tiempos y preposiciones según las convenciones actuales; se evitan las construcciones posibles pero poco naturales. [Encargo §5]
- **E-51** *y* → *e* ante el sonido /i/ (*e iglesia*, *e hijo*); *o* → *u* ante /o/ (*u otro*), también al inicio de la oración. [THL]
- **E-52** Signos de apertura obligatorios: `¿` y `¡`. Si la línea continúa una frase de la anterior (empieza en minúscula), el signo de apertura va en la anterior. [THL]
- **E-53** `?!` del inglés → `¡¿...?!`. Varios signos de cierre llevan la misma cantidad de apertura: `¡¡FUERA!!`. [THL]
- **E-54** Puntos suspensivos: tres puntos `...`, sin espacio antes. Sin espacios dobles ni espacio antes de un signo. [THL]
- **E-55** Tartamudeo: `P-Por favor`, con la mayúscula repetida si la palabra la lleva. [THL]
- **E-56** Gritos en MAYÚSCULAS, como el inglés. [THL]
- **E-57** Porcentajes sin espacio: `50%`. [THL]
- **E-58** Comillas donde el inglés las usa para una cita. El punto final va fuera de las comillas; `?`, `!` y `...` van dentro si son de lo citado. Las comillas son las del juego (`“...”`), porque la fuente no tiene las rectas (T-5). [THL]
- **E-59** Lugares y términos comunes del juego van en minúscula a media frase. Llevan mayúscula al inicio de la oración, en las etiquetas de menú y mapa, y en los nombres propios. [THL]

## Método

- **E-60** Se revisa en siete pasadas: fidelidad, naturalidad, localización, gramática, género (aparte, al final), consistencia y lectura final. [Encargo §9]
- **E-61** El glosario manda: nombres, habilidades y términos no se cambian por gusto, y lo que debe quedar sin traducir no se traduce. Una inconsistencia se señala, no se corrige por cuenta propia. [Encargo §6]
