# Constants for the application configuration
import os

API_KEY = "T8RPfyvEf6Zn8riLQ0efTZUQreaMpEEKpQr4utyb"
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
# Use absolute paths that work cross-platform
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "finalproject_data_collection.json")