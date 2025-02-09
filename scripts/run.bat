@echo off
REM Get the directory of this script
set SCRIPT_DIR=%~dp0
set PROJECT_ROOT=%SCRIPT_DIR%..

REM Check if a file was provided
if "%~1"=="" (
    echo Usage: scripts\run.bat <file.orb>
    exit /b 1
)

REM Resolve the absolute path of the input file
for %%I in ("%~1") do set INPUT_FILE=%%~fI

REM Run the interpreter
set PYTHONPATH=%PROJECT_ROOT%
python -m src.interpreter "%INPUT_FILE%"