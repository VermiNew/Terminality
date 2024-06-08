@echo off
setlocal

REM Get the full path to the current directory
for %%I in ("%~dp0") do set "script_dir=%%~fI"

REM Prompt user for confirmation
echo.
echo This script will add the directory containing term.bat to the system PATH.
echo Adding the directory to the PATH allows you to run term.bat from any location in the command prompt.
echo.
echo WARNING: Modifying the system PATH can affect system behavior and other applications. 
echo Ensure that you understand the implications before proceeding.
echo.

set /p confirm=Do you want to continue? (Y/N): 

if /i "%confirm%"=="Y" (
    REM Add the directory containing term.bat to the system PATH
    set "path_to_add=%script_dir%"
    if defined path_to_add (
        echo Adding %path_to_add% to the system PATH...
        setx /M PATH "%PATH%;%path_to_add%"
        echo Directory added to the system PATH successfully.
    ) else (
        echo Failed to determine the directory to add to the system PATH.
        exit /b 1
    )
) else (
    echo Installation aborted.
    exit /b 1
)

echo Installation complete.

echo.
echo To uninstall Terminality and remove the added directory from the system PATH:
echo 1. Open a command prompt with administrative privileges.
echo 2. Run the following command:
echo    setx /M PATH "%PATH:;%path_to_add%=%%"
echo    (replace %path_to_add% with the actual path you added)
echo 3. Verify that the directory has been removed from the system PATH.
echo    You may need to restart your computer for the changes to take effect.
echo.
echo Thank you for using Terminality!
echo.

endlocal
