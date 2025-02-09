@echo off
REM Check if a file name was provided
if "%~1"=="" (
    echo Usage: orbit ^<file_name^>
    exit /b 1
)

REM Run Python script with the provided file name
python run.py "%~1"
