import tkinter as tk
from tkinter import messagebox, filedialog  # Import filedialog for save dialog
from PIL import Image, ImageTk  # Import Pillow for image handling
import requests
import json
from io import BytesIO  # To handle image data in memory
from datetime import datetime  # Import datetime module

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

        # Get the current date (fetch date)
        fetch_date = datetime.now().strftime("%Y-%m-%d")

        # Append new data and write back to the file
        existing_data.append({
            "title": data.get("title", "No Title"),
            "explanation": data.get("explanation", "No Explanation"),
            "image_url": data.get("url", ""),  # Ensure the key matches the API response
            "fetch_date": fetch_date  # Add the fetch date
        })
        with open(DATA_FILE, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def save_image(image_data):
    """Save the fetched image to a user-specified location."""
    try:
        # Open a file dialog for the user to choose the save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:  # If the user selects a file path
            image_data.save(file_path)
            messagebox.showinfo("Success", f"Image saved as {file_path}")
        else:
            messagebox.showinfo("Info", "Save operation canceled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")

def save_current_image():
    """Allow the user to save the currently displayed image to a file."""
    try:
        # Check if there is an image displayed
        if hasattr(image_label, "image") and image_label.image is not None:
            # Ask user for file path
            file_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")]
            )
            if file_path:
                # Get the current image from the label
                # We need to keep a reference to the original PIL image
                # So let's store it as a global variable when updating the GUI
                global current_pil_image
                if current_pil_image:
                    current_pil_image.save(file_path)
                    messagebox.showinfo("Success", f"Image saved as {file_path}")
                else:
                    messagebox.showwarning("Warning", "No image data available to save.")
            else:
                messagebox.showinfo("Info", "Save operation canceled.")
        else:
            messagebox.showwarning("Warning", "No image to save.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")

def update_gui(apod_data):
    """Update the GUI with the fetched APOD data."""
    try:
        # Extract relevant data
        title = apod_data.get("title", "No Title")
        explanation = apod_data.get("explanation", "No Explanation")
        image_url = apod_data.get("url", "")
        date = apod_data.get('date', "No Date")

        # Fetch the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        image_data = Image.open(BytesIO(image_response.content))
        global current_pil_image
        current_pil_image = image_data.copy()

        # Resize the image to fit the GUI window while maintaining aspect ratio
        max_width, max_height = 600, 400  # Set maximum dimensions for the image
        image_data.thumbnail((max_width, max_height), Image.LANCZOS)

        # Update the image in the GUI
        img = ImageTk.PhotoImage(image_data)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection

        # Update the title and explanation
        title_label.config(text=title)
        explanation_text.delete("1.0", tk.END)  # Clear the existing text
        explanation_text.insert(tk.END, explanation)  # Insert the new explanation

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
    global image_label, title_label, explanation_label, root, explanation_text

    root = tk.Tk()
    root.title("NASA Daily Photo")
    root.geometry("800x600")  # Set a fixed window size
    root.configure(bg="#2E2E2E")

    # Create a frame for the title
    top_frame = tk.Frame(root, bg="#2E2E2E")
    top_frame.pack(fill="x", pady=10)

    # Title display
    title_label = tk.Label(
        top_frame,
        text="NASA Daily Photo",
        font=("Helvetica", 14, "bold"),
        wraplength=600,
        justify="center",
        bg="#2E2E2E",
        fg="white"
    )
    title_label.pack(anchor="center", pady=5)  # Center the title

    # Date display
    date_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center", bg="#2E2E2E", fg="white")
    date_label.pack(pady=5)

    # Image display
    image_frame = tk.Frame(root, bg="#2E2E2E")
    image_frame.pack(pady=10)
    image_label = tk.Label(image_frame, bg="#2E2E2E")  # Remove fixed width/height
    image_label.pack()

    # Explanation display with scrollbar
    explanation_frame = tk.Frame(root, bg="#2E2E2E")
    explanation_frame.pack(fill="both", expand=True, pady=10)
    explanation_scrollbar = tk.Scrollbar(explanation_frame)
    explanation_scrollbar.pack(side="right", fill="y")
    explanation_text = tk.Text(
        explanation_frame,
        wrap="word",
        font=("Helvetica", 10),
        bg="#2E2E2E",
        fg="white",
        yscrollcommand=explanation_scrollbar.set,
        height=8
    )
    explanation_text.pack(fill="both", expand=True)
    explanation_scrollbar.config(command=explanation_text.yview)

    # Credit display
    credit_label = tk.Label(
        root,
        text="",
        font=("Helvetica", 10, "italic"),
        wraplength=600,
        justify="center",
        bg="#2E2E2E",
        fg="white"
    )
    credit_label.pack(pady=5)

    # Fetch button
    fetch_button = tk.Button(
        root,
        text="Fetch Picture",
        command=fetch_apod,
        bg="gray",
        fg="white"
    )
    fetch_button.pack(pady=20)

    # Save button
    save_button = tk.Button(
        root,
        text="Save Picture",
        command=save_current_image,
        bg="gray",
        fg="white"
    )
    save_button.pack(pady=5)

    # Run the GUI loop
    root.mainloop()

# Call the UI function to start the GUI
UI()