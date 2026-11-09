# smt4-apocalypse-esp

Traducción fan al español neutro de *Shin Megami Tensei IV: Apocalypse* (Nintendo 3DS), hecha desde el inglés oficial.

**Estado:** en preparación. Ya hay instalador, pero por ahora solo agrega las letras españolas a las fuentes del juego. Todavía no hay texto traducido.

> Es un proyecto de fans, sin relación con Atlus ni con Nintendo. **No incluye el juego ni sus archivos:** el instalador arma la traducción a partir de tu propia copia.

## Avance

<!-- progress: lo actualiza `python3 -I tools/progress.py --readme` en cada commit que toca translation/ -->
**Etapa actual:** Fase 1. Prueba técnica: Ida y vuelta del ejecutable (`code.bin`): tiene unos mil textos de interfaz en inglés de ancho completo (elementos, estados, mensajes cortos).

| Fase | Sección | Traducidos | Total | % |
|---|---|---:|---:|---:|
| 6.1 | Interfaz | 690 | 690 | 100,0 % |
| 6.2 | Tablas | 769 | 6.757 | 11,4 % |
| 6.3 | Datos | 0 | 3.001 | 0,0 % |
| 6.4 | Historia | 15 | 2.773 | 0,5 % |
| 6.5 | Secundarias | 2 | 1.578 | 0,1 % |
| 6.6 | Negociaciones | 0 | 11.518 | 0,0 % |
| 6.7 | Demonios en combate | 0 | 4.380 | 0,0 % |
| 6.8 | Contenido descargable | 0 | 542 | 0,0 % |
| | **Total** | **1.476** | **31.239** | **4,7 %** |
<!-- /progress -->

Qué entra en cada sección y cómo se cuenta: [translation/README.md](translation/README.md).

## Instalar

Necesitas la versión **europea** del juego en un `.3ds` (o `.cxi`) descifrado, y Python 3.

1. Descarga este repositorio.
2. En Windows, abre `install.bat`. En Linux o macOS, ejecuta `python3 install.py`.
3. Elige dónde instalar: **Azahar**, **Citra** o **la SD de una 3DS** con Luma3DS. Después arrastra tu `.3ds` a la ventana.

El instalador encuentra solo la carpeta de los emuladores. En una 3DS, activa *Enable game patching* en la configuración de Luma3DS (mantén SELECT al encenderla). Para quitar la traducción, abre el instalador otra vez y elige *Desinstalar*: borra solo lo que instaló.

## Documentos

- [PLAN.md](PLAN.md): fases y pendientes técnicos.
- [TEAM.md](TEAM.md): el equipo de traducción (roles, modelos, controles y el lote paso a paso).
- Reglas:
  - [STYLE.md](STYLE.md): guía de estilo.
  - [TECH.md](TECH.md): reglas técnicas.
  - [GLOSSARY.md](GLOSSARY.md): glosario.
  - [characters/](characters): fichas de personajes.
- [DECISIONS.md](DECISIONS.md) y [PENDING.md](PENDING.md): decisiones tomadas y cola de pendientes.
- [translation/](translation): la traducción, sus secciones y su formato.
- [tools/](tools): las herramientas.
  - `ctr.py`, `mbm.py`, `tbb.py`: extraen el juego y leen y escriben sus mensajes y tablas.
  - `bcfnt.py`, `font.py`, `letters.py`: dibujan las letras españolas en las fuentes.
  - `layout.py`: mide los renglones en píxeles y los parte.
  - `batch.py`, `check.py`, `review.py`, `corpus.py`: preparan, validan y controlan los lotes.
  - `smt5v.py`, `build_ooz.sh`: leen los términos oficiales de *SMT V: Vengeance*.
  - `patch.py`: arma la traducción.
  - `progress.py`: calcula el avance.

El repositorio guarda solo nuestra traducción y nuestras herramientas, nunca texto del juego ni la ROM.
