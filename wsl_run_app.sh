#!/bin/bash
# WSL-specific script for running the NASA Daily Photo application

# Check if DISPLAY variable is set
if [ -z "$DISPLAY" ]; then
    echo "DISPLAY environment variable is not set."
    echo "Setting DISPLAY to connect to Windows X server..."
    
    # Get the IP address of the host Windows machine
    WINDOWS_IP=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
    
    # Set DISPLAY to point to the Windows X server
    export DISPLAY=$WINDOWS_IP:0
    
    echo "DISPLAY set to $DISPLAY"
fi

# Path to project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/FinalCopy"

# Check for Python and required packages
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first:"
    echo "  sudo apt update && sudo apt install -y python3 python3-pip python3-venv"
    exit 1
fi

# Check for virtual environment or create one
VENV_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Check for required packages
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Tkinter is not installed. Please install it with:"
    echo "  sudo apt update && sudo apt install -y python3-tk"
    exit 1
fi

# Install required Python packages if needed
cd "$PROJECT_DIR" && pip install -r Requirements.txt

# Run the application
echo "Starting NASA Daily Photo application..."
cd "$PROJECT_DIR" && python3 -m src.main

# Deactivate virtual environment when done
deactivate
