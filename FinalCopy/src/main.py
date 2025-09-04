import tkinter as tk
from tkinter import messagebox
from src.ui import APODApp
from src.config import API_URL, DATA_FILE
import requests
import json
from datetime import datetime

def fetch_apod_data():
    """Fetch APOD data from the NASA API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch APOD data: {e}")
        return None

def save_data_to_file(data):
    """Save the APOD data to the JSON file."""
    try:
        # Read existing data
        try:
            with open(DATA_FILE, "r") as json_file:
                existing_data = json.load(json_file)
                if not isinstance(existing_data, list):
                    existing_data = []
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Get the current date (fetch date)
        fetch_date = datetime.now().strftime("%Y-%m-%d")

        # Append new data and write back to the file
        existing_data.append({
            "title": data.get("title", "No Title"),
            "explanation": data.get("explanation", "No Explanation"),
            "image_url": data.get("url", ""),
            "fetch_date": fetch_date
        })
        with open(DATA_FILE, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def main():
    root = tk.Tk()
    app = APODApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()