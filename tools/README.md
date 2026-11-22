# Herramientas

Lo que se programó para SMT IV: Apocalypse. Se corren desde la raíz del repo, con la extracción del juego en `../smt4a-local/`.

| Script | Qué hace |
|---|---|
| `ctr.py`, `mbm.py`, `tbb.py`, `codebin.py` | Extraen el juego y leen y escriben sus mensajes, sus tablas y los textos del ejecutable |
| `bcfnt.py`, `font.py`, `letters.py` | Dibujan las letras españolas en las fuentes |
| `layout.py` | Mide los renglones en píxeles y los parte |
| `patch.py` | Arma la traducción |
| `kit_adapter.py`, `hooks.py` | El adaptador del kit de traducción: `kit_adapter.py export` escribe el original en el formato común, y `hooks.py` le da al kit las secciones, la caja y los bytes de este repo |
| `progress.py` | Las secciones y lo que no se cuenta; con `--readme`, actualiza `translation/README.md` |
| `batch.py`, `check.py`, `review.py`, `corpus.py` | Los lotes de antes del kit (los chequeos y el corpus los sigue usando `hooks.py`) |
| `smt5v.py`, `build_ooz.sh` | Leen los términos oficiales de *SMT V: Vengeance* |

## Instalador

- `install.py` (o `install.bat`): `--target azahar` o `--target citra` instalan la traducción como mod en el emulador; `--target sd --folder RUTA`, en la SD de una 3DS con Luma3DS; `--uninstall` la quita.
- El `.exe` de Windows se arma con `tools\build_exe.bat` (Windows, con Python 3); queda en `build\exe\`.
