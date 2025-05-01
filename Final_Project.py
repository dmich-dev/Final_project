import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image handling
import requests
import json
from io import BytesIO  # To handle image data in memory

# Constants
API_KEY = "T8RPfyvEf6Zn8riLQ0efTZUQreaMpEEKpQr4utyb"
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
DATA_FILE = "finalproject_data_collection.json"

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

        # Append new data and write back to the file
        existing_data.append(data)
        with open(DATA_FILE, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def update_gui(apod_data):
    """Update the GUI with the fetched APOD data."""
    try:
        # Debugging: Print the fetched data
        print("Fetched APOD Data:", apod_data)

        # Extract relevant data
        title = apod_data.get("title", "No Title")
        explanation = apod_data.get("explanation", "No Explanation")
        image_url = apod_data.get("url", "")

        # Ensure explanation is not empty
        if not explanation:
            explanation = "No explanation available for this image."

        # Debugging: Print the explanation being updated
        print(f"Updating explanation: {explanation}")

        # Fetch the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        image_data = Image.open(BytesIO(image_response.content))

        # Update the image in the GUI
        img = ImageTk.PhotoImage(image_data)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection

        # Update the title and explanation
        title_label.config(text=title)
        explanation_label.config(text=f"Description: {explanation}")
        explanation_label.update_idletasks()  # Force the UI to refresh

        # Save the data to the JSON file
        save_data_to_file({
            "title": title,
            "explanation": explanation,
            "image_url": image_url
        })
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update GUI: {e}")

def fetch_apod():
    """Fetch APOD data and update the GUI."""
    apod_data = fetch_apod_data()
    if apod_data:
        update_gui(apod_data)

def UI():
    """Set up the GUI."""
    global image_label, title_label, explanation_label

    root = tk.Tk()
    root.title("NASA Daily Photo")

    # Title display
    title_label = tk.Label(root, text="Astronomy Picture of the Day\nDiscover the cosmos! Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.", font=("Helvetica", 14, "bold"), wraplength=600, justify="center")
    title_label.pack(pady=10)

    # Date display
    date_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
    date_label.pack(pady=5)

    # Image and explanation display (stacked vertically)
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    explanation_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=600, justify="left")
    explanation_label.pack(pady=10)

    # Credit display
    credit_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"), wraplength=600, justify="left")
    credit_label.pack(pady=5)

    # Fetch button
    fetch_button = tk.Button(root, text="Fetch Picture", command=fetch_apod)
    fetch_button.pack(pady=20)

    # Run the GUI loop
    root.mainloop()

# Call the UI function to start the GUI
UI()