# smt4-apocalypse-esp

Traducción fan al español neutro de *Shin Megami Tensei IV: Apocalypse* (Nintendo 3DS), hecha desde el inglés oficial.

**Estado:** en preparación. Ya hay instalador, pero por ahora solo agrega las letras españolas a las fuentes del juego. Todavía no hay texto traducido.

> Es un proyecto de fans, sin relación con Atlus ni con Nintendo. **No incluye el juego ni sus archivos:** el instalador arma la traducción a partir de tu propia copia.

## Avance

<!-- avance: lo actualiza `python3 -I tools/avance.py --readme` en cada commit que toca traduccion/ -->
**Etapa actual:** Fase 1. Prueba técnica: Ida y vuelta del resto del texto: tablas (`.tbb`), ejecutable y texturas.

| Fase | Sección | Traducidos | Total | % |
|---|---|---:|---:|---:|
| 6.1 | Interfaz | 0 | 707 | 0,0 % |
| 6.2 | Tablas | — | por medir | — |
| 6.3 | Datos | 0 | 3.001 | 0,0 % |
| 6.4 | Historia | 0 | 2.773 | 0,0 % |
| 6.5 | Secundarias | 0 | 1.578 | 0,0 % |
| 6.6 | Negociaciones | 0 | 11.518 | 0,0 % |
| 6.7 | Demonios en combate | 0 | 4.380 | 0,0 % |
| 6.8 | Contenido descargable | 0 | 225 | 0,0 % |
| | **Total** | **0** | **24.182** | **0,0 %** |
<!-- /avance -->

Qué entra en cada sección y cómo se cuenta: [traduccion/README.md](traduccion/README.md).

## Instalar

Necesitas la versión **europea** del juego en un `.3ds` (o `.cxi`) descifrado, y Python 3.

1. Descarga este repositorio.
2. En Windows, abre `instalar.bat`. En Linux o macOS, ejecuta `python3 instalar.py`.
3. Elige dónde instalar: **Azahar**, **Citra** o **la SD de una 3DS** con Luma3DS. Después arrastra tu `.3ds` a la ventana.

El instalador encuentra solo la carpeta de los emuladores. En una 3DS, activa *Enable game patching* en la configuración de Luma3DS (mantén SELECT al encenderla). Para quitar la traducción, abre el instalador otra vez y elige *Desinstalar*: borra solo lo que instaló.

## Documentos

- [PLAN.md](PLAN.md): decisiones, pendientes y fases.
- [TEAM.md](TEAM.md): cómo se reparten la traducción y la revisión.
- [traduccion/](traduccion): la traducción, sus secciones y su formato.
- [tools/](tools): las herramientas.
  - `ctr.py`: extrae los archivos del juego.
  - `mbm.py`: lee y escribe los mensajes.
  - `bcfnt.py` y `fuente.py`: dibujan las letras españolas en las fuentes.
  - `parche.py`: arma la traducción.
  - `avance.py`: calcula el avance.

El repositorio guarda solo nuestra traducción y nuestras herramientas, nunca texto del juego ni la ROM.
