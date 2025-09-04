#!/bin/bash

# Run the NASA Daily Photo application from any directory

# Path to project directory
PROJECT_DIR="/Users/djmichaud/repos/Final-project/FinalCopy"
VENV_PYTHON="/Users/djmichaud/repos/Final-project/.venv/bin/python"

# Change to the project directory and run the application
cd "$PROJECT_DIR" && "$VENV_PYTHON" -m src.main
