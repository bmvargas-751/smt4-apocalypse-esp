# smt4-apocalypse-esp

Traducción fan al español neutro de *Shin Megami Tensei IV: Apocalypse* (Nintendo 3DS), hecha desde el inglés oficial.

**Estado:** traducción completa (todos los diálogos, misiones, negociaciones, descripciones y menús de los archivos de texto del juego, el contenido descargable y los textos cortos de interfaz del ejecutable). Quedan en inglés los textos de las texturas.

> Es un proyecto de fans, sin relación con Atlus ni con Nintendo. **No incluye el juego ni sus archivos:** el instalador arma la traducción a partir de tu propia copia.

## Avance

<!-- loc:progress -->
Actualizado: 2026-11-22.

**Etapa actual:** Fase 7. Prueba en el juego: Jugar con la traducción completa y anotar cortes, cajas que se pasan, glifos que faltan y texto que quedó en inglés.

### Fases

| Fase | Estado |
|---|---|
| 0. Decisiones | ✅ |
| 1. Prueba técnica | ✅ |
| 2. Inventario y costo | ✅ 22.862 líneas |
| 3. Glosario y fichas | ✅ |
| 4. Herramientas | ✅ |
| 5. Piloto | ✅ |
| 6. Traducción | ✅ 100,0 % |
| 7. Prueba en el juego | ⏳ |
| 8. Entrega | ⏳ |

### Secciones

| Sección | Líneas | Traducidas | Avance |
|---|---:|---:|---:|
| Interfaz | 688 | 688 | 100,0 % |
| Tablas | 6.757 | 6.757 | 100,0 % |
| Datos | 2.599 | 2.599 | 100,0 % |
| Historia | 2.409 | 2.409 | 100,0 % |
| Secundarias | 1.085 | 1.085 | 100,0 % |
| Negociaciones | 5.847 | 5.847 | 100,0 % |
| Demonios en combate | 1.973 | 1.973 | 100,0 % |
| Contenido descargable | 488 | 488 | 100,0 % |
| Ejecutable | 1.016 | 1.016 | 100,0 % |
| **Total** | **22.862** | **22.862** | **100,0 %** |
<!-- /loc:progress -->

Qué entra en cada sección y cómo se cuenta: [translation/README.md](translation/README.md).

## Instalar

Necesitas la versión **europea** del juego en un `.3ds` (o `.cxi`) descifrado.

**Windows:**

1. Descarga `smt4a-esp-install.exe` de la [última versión](../../releases/latest). No hace falta Python.
2. Ábrelo con doble clic, arrastra tu `.3ds` a la ventana y presiona Enter.
3. Al lado de tu copia aparece otra, traducida: «NOMBRE (Español).3ds». Ábrela en Azahar o Citra. La original no se toca.

**Linux o macOS** (o Windows con Python 3): descarga este repositorio y ejecuta `python3 install.py` (en Windows, `install.bat`).

**En una 3DS** (con Luma3DS), la traducción va como mod en la SD: `python3 install.py --rom TU_JUEGO.3ds --target sd --folder E:\` (la raíz de la SD), y en la configuración de Luma3DS se activa *Enable game patching* (mantén SELECT al encenderla). Con `--target azahar` o `--target citra` también se puede instalar como mod en un emulador; `--uninstall` lo quita.

Para armar el `.exe` desde el repositorio: `tools\build_exe.bat` (Windows, con Python 3); queda en `build\exe\`.

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
