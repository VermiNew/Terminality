@echo off
@title Terminality
@cls
setlocal enabledelayedexpansion

for %%I in ("%~dp0") do set "scriptpath=%%~fIbin\main.py"

:visuals
python "%scriptpath%"
set /p command=""

if /I "!command!"=="exit" (
    exit
) else (
    !command!
)
goto visuals
