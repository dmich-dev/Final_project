#!/bin/bash

# Run the NASA Daily Photo application using the project's virtual environment
# This script must be run from the FinalCopy directory

# Path to the virtual environment Python interpreter
VENV_PYTHON="/Users/djmichaud/repos/Final-project/.venv/bin/python"

# Check if we're in the correct directory
if [ ! -d "src" ]; then
    echo "Error: This script must be run from the FinalCopy directory"
    echo "Please change to that directory first with: cd /Users/djmichaud/repos/Final-project/FinalCopy"
    exit 1
fi

# Run the application
echo "Starting NASA Daily Photo application..."
"$VENV_PYTHON" -m src.main
