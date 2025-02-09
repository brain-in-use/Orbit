# Get the directory of this script
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PROJECT_ROOT = Split-Path -Parent $SCRIPT_DIR

# Check if a file was provided
if (-not $args[0]) {
    Write-Host "Usage: scripts\run.ps1 <file.orb>"
    exit 1
}

# Resolve the absolute path of the input file
$INPUT_FILE = Resolve-Path $args[0]

# Run the interpreter
$env:PYTHONPATH = $PROJECT_ROOT
python -m src.interpreter $INPUT_FILE