@echo off
rem Instalador de la traduccion al espanol de SMT IV: Apocalypse (necesita Python 3).
chcp 65001 >nul
pushd "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (py -3 instalar.py %*) else (python instalar.py %*)
popd
pause
