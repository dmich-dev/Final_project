# NASA APOD Viewer (Cross-Platform)

## Project Overview
This Python application connects to NASA's Astronomy Picture of the Day (APOD) API, fetching daily astronomical images and their descriptions. It features a graphical user interface (GUI) built with Tkinter, allowing users to view, save, and store APOD images and information. The application has been optimized to work across Windows, macOS, and Linux platforms.

## Features
- Fetches the latest APOD image and description from NASA's API
- Displays images and explanations in an interactive Tkinter GUI
- Allows users to save the displayed image to their computer
- Stores all fetched data in a local JSON file for future reference

## File Structure
```
Final-project
├── FinalCopy
│   ├── src
│   │   ├── __init__.py    # Package initialization
│   │   ├── config.py      # Configuration settings (API keys, URLs)
│   │   ├── main.py        # Application entry point
│   │   └── ui.py          # GUI setup and event handling
│   ├── data
│   │   └── finalproject_data_collection.json  # Stores fetched APOD data
│   ├── Requirements.txt   # Project dependencies
│   ├── run_app.sh         # Shell script to run the app from the FinalCopy directory
│   ├── debug.py           # Debug utility
│   └── mac_debug.py       # macOS specific debug utility
├── nasa_photo.sh          # Shell script to run the app from any directory
└── README.md              # Project documentation
```

## Installation Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Final-project
   ```

2. **Set up a virtual environment (recommended)**:
   ```
   # For Windows:
   python -m venv .venv
   .venv\Scripts\activate

   # For macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```
   # Navigate to the FinalCopy directory
   cd FinalCopy
   
   # Install required packages
   pip install -r Requirements.txt
   ```

4. **Run the application**:
   
   **Using the provided scripts (easiest):**
   
   On macOS/Linux:
   ```
   # From the FinalCopy directory
   ./run_app.sh
   
   # From any directory
   /path/to/Final-project/nasa_photo.sh
   ```
   
   **Direct Python command:**
   ```
   # From the FinalCopy directory
   # For Windows:
   python -m src.main
   
   # For macOS/Linux:
   python3 -m src.main
   ```

5. **Set up an alias (optional, for macOS/Linux users)**:
   Add the following to your `~/.bashrc` or `~/.zshrc`:
   ```
   alias nasaphoto="/path/to/Final-project/nasa_photo.sh"
   ```
   
   Then reload your shell configuration:
   ```
   source ~/.bashrc  # or source ~/.zshrc
   ```
   
   Now you can run the application from anywhere simply by typing:
   ```
   nasaphoto
   ```

## API Usage Details
- The application uses NASA's [APOD API](https://api.nasa.gov/) to fetch daily images and descriptions.
- You must provide a valid API key in `config.py`. A demo key is included for testing.
- API endpoint used: `https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY`

## How Data is Stored
- All fetched APOD data (title, explanation, image URL, fetch date) is appended to `data/finalproject_data_collection.json`.
- This allows users to keep a local history of all images and information retrieved during usage.

## Known Issues / Limitations
- The application only fetches the current day's APOD; browsing previous days is not supported.
- Some APOD entries may be videos or have missing images, which may not display correctly.
- Requires an internet connection to fetch new data from the API.
- When running in WSL, you may need an X server configured for GUI applications.
- On macOS, there might be a deprecation warning about Tk, which can be safely ignored (we've added code to suppress this).

## Debugging Summary
- Errors during API requests or file operations are shown as pop-up messages in the GUI.
- If the application fails to fetch or display an image, check your internet connection and API key.
- For further debugging, you can use the provided debug utilities:
  ```
  # Basic debugging (from FinalCopy directory)
  python3 debug.py
  
  # Detailed environment checking for macOS (from FinalCopy directory)
  python3 mac_debug.py
  ```
- Common issues:
  - "No module named 'src'" - Make sure to run the application from the FinalCopy directory
  - "No module named 'PIL'" or "No module named 'tkinter'" - Install required dependencies as described in the installation instructions
  - Path-related issues - We've updated the code to use absolute paths for better cross-platform compatibility

## Credits and Acknowledgements
- [NASA APOD API](https://api.nasa.gov/) for providing daily astronomical images and data.
- [Pillow](https://python-pillow.org/) for image processing.
- [Requests](https://docs.python-requests.org/) for HTTP requests.
- Tkinter for the GUI framework.
- Developed as a Programming 2 final project.