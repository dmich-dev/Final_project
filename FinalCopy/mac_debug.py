import os
import sys
import traceback
import platform

def check_environment():
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if data directory exists
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    print(f"Data directory path: {data_dir}")
    print(f"Data directory exists: {os.path.exists(data_dir)}")
    
    # Check for tkinter
    try:
        import tkinter
        print("Tkinter is available")
        print(f"Tkinter version: {tkinter.TkVersion}")
    except ImportError:
        print("Tkinter is NOT available")
    
    # Check for Pillow/PIL
    try:
        from PIL import Image, ImageTk
        print("Pillow is available")
        print(f"Pillow version: {Image.__version__}")
    except ImportError:
        print("Pillow is NOT available")
    
    # Check for requests
    try:
        import requests
        print("Requests is available")
        print(f"Requests version: {requests.__version__}")
    except ImportError:
        print("Requests is NOT available")

if __name__ == "__main__":
    print("=== Environment Check ===")
    check_environment()
    
    print("\n=== Running Application ===")
    try:
        from src.main import main
        main()
    except Exception as e:
        print(f"\nERROR: {e}")
        traceback.print_exc()
