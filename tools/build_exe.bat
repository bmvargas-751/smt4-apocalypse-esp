@echo off
rem Arma build\exe\smt4a-esp-install.exe: el instalador en un solo archivo, sin Python.
rem Se ejecuta en Windows y necesita Python 3 solo para armarlo (py -3).
rem PyInstaller va en un entorno aparte, en %TEMP%\smt4a-build, sin tocar el Python del sistema.
chcp 65001 >nul
pushd "%~dp0.."
set "ROOT=%CD%"
set "WORK=%TEMP%\smt4a-build"
set "VENV=%WORK%\venv"
if not exist "%VENV%\Scripts\python.exe" (
    py -3 -m venv "%VENV%" || goto :error
)
"%VENV%\Scripts\python.exe" -m pip install --quiet --disable-pip-version-check --upgrade pyinstaller || goto :error
"%VENV%\Scripts\python.exe" -m PyInstaller --noconfirm --clean --onefile --console ^
    --name smt4a-esp-install ^
    --paths "%ROOT%\tools" ^
    --add-data "%ROOT%\translation;translation" ^
    --add-data "%ROOT%\tests;tests" ^
    --distpath "%ROOT%\build\exe" ^
    --workpath "%WORK%\work" ^
    --specpath "%WORK%" ^
    "%ROOT%\install.py" || goto :error
popd
echo.
echo Listo: build\exe\smt4a-esp-install.exe
exit /b 0

:error
popd
echo.
echo No se pudo armar el .exe.
exit /b 1
