# NASA APOD Viewer

## Project Overview
This Python application connects to NASA's Astronomy Picture of the Day (APOD) API, fetching daily astronomical images and their descriptions. It features a graphical user interface (GUI) built with Tkinter, allowing users to view, save, and store APOD images and information.

## Features
- Fetches the latest APOD image and description from NASA's API
- Displays images and explanations in an interactive Tkinter GUI
- Allows users to save the displayed image to their computer
- Stores all fetched data in a local JSON file for future reference

## File Structure
```
my-python-api-ui-app
├── src
│   ├── config.py          # Configuration settings (API keys, URLs)
│   ├── main.py            # Application entry point
│   └── ui.py              # GUI setup and event handling
├── data
│   └── finalproject_data_collection.json  # Stores fetched APOD data
├── Requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd my-python-api-ui-app
   ```

2. **Install dependencies**:
   Ensure you have Python installed. Then, run:
   ```
   pip install -r Requirements.txt
   ```

3. **Run the application**:
   ```
   python -m src.main
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

## Debugging Summary
- Errors during API requests or file operations are shown as pop-up messages in the GUI.
- If the application fails to fetch or display an image, check your internet connection and API key.
- For further debugging, review the terminal output or add print statements as needed.

## Credits and Acknowledgements
- [NASA APOD API](https://api.nasa.gov/) for providing daily astronomical images and data.
- [Pillow](https://python-pillow.org/) for image processing.
- [Requests](https://docs.python-requests.org/) for HTTP requests.
- Tkinter for the GUI framework.
- Developed as a Programming 2 final project.