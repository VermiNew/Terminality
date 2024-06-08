@echo off
@cls
setlocal enabledelayedexpansion

for %%I in ("%~dp0") do set "scriptpath=%%~fIbin\main.py"

:visuals
python "%scriptpath%"
set /p command=""
!command!
goto visuals
