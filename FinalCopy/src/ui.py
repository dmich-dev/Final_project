import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import requests
import json
import platform
from io import BytesIO
from datetime import datetime
from src.config import API_URL, DATA_FILE
import os

class APODApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NASA Daily Photo")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E2E2E")
        
        # Suppress macOS Tkinter deprecation warning
        if self.is_macos():
            os.environ['TK_SILENCE_DEPRECATION'] = '1'

        self.create_widgets()
        self.current_pil_image = None
        
    def is_macos(self):
        """Check if running on macOS."""
        return platform.system() == 'Darwin'

    def create_widgets(self):
        # Use system colors for better compatibility across platforms
        bg_color = "#2E2E2E" if not self.is_macos() else "#3D3D3D"
        
        top_frame = tk.Frame(self.root, bg=bg_color)
        top_frame.pack(fill="x", pady=10)

        self.title_label = tk.Label(
            top_frame,
            text="NASA Daily Photo",
            font=("Helvetica", 14, "bold"),
            wraplength=600,
            justify="center",
            bg=bg_color,
            fg="white"
        )
        self.title_label.pack(anchor="center", pady=5)

        self.date_label = tk.Label(self.root, text="", font=("Helvetica", 12), justify="center", bg="#2E2E2E", fg="white")
        self.date_label.pack(pady=5)

        image_frame = tk.Frame(self.root, bg="#2E2E2E")
        image_frame.pack(pady=10)
        self.image_label = tk.Label(image_frame, bg="#2E2E2E")
        self.image_label.pack()

        explanation_frame = tk.Frame(self.root, bg="#2E2E2E")
        explanation_frame.pack(fill="both", expand=True, pady=10)
        explanation_scrollbar = tk.Scrollbar(explanation_frame)
        explanation_scrollbar.pack(side="right", fill="y")
        self.explanation_text = tk.Text(
            explanation_frame,
            wrap="word",
            font=("Helvetica", 10),
            bg="#2E2E2E",
            fg="white",
            yscrollcommand=explanation_scrollbar.set,
            height=8
        )
        self.explanation_text.pack(fill="both", expand=True)
        explanation_scrollbar.config(command=self.explanation_text.yview)

        fetch_button = tk.Button(
            self.root,
            text="Fetch Picture",
            command=self.fetch_apod,
            bg="#4287f5",  # Bright blue background
            fg="Black",    # White text
            font=("Helvetica", 10, "bold"),  # Bold text for better visibility
            relief=tk.RAISED,  # Give buttons a raised appearance
            padx=10,           # Add horizontal padding
            pady=5             # Add vertical padding
        )
        fetch_button.pack(pady=20)

        save_button = tk.Button(
            self.root,
            text="Save Picture",
            command=self.save_current_image,
            bg="#4287f5",  # Bright blue background
            fg="Black",    # White text
            font=("Helvetica", 10, "bold"),  # Bold text for better visibility
            relief=tk.RAISED,  # Give buttons a raised appearance
            padx=10,           # Add horizontal padding
            pady=5             # Add vertical padding
        )
        save_button.pack(pady=5)

    def fetch_apod(self):
        # Enable the explanation text before updating
        self.explanation_text.config(state="normal")
        apod_data = self.fetch_apod_data()
        if apod_data:
            self.update_gui(apod_data)

    def fetch_apod_data(self):
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch APOD data: {e}")
            return None

    def update_gui(self, apod_data):
        title = apod_data.get("title", "No Title")
        explanation = apod_data.get("explanation", "No Explanation")
        image_url = apod_data.get("url", "")
        date = apod_data.get('date', "No Date")

        try:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_data = Image.open(BytesIO(image_response.content))
            self.current_pil_image = image_data.copy()

            max_width, max_height = 600, 400
            # Use fallback resampling method for macOS compatibility
            image_data.thumbnail((max_width, max_height))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")
            return

        # Create PhotoImage and store it as attribute to prevent garbage collection
        self.photo_image = ImageTk.PhotoImage(image_data)
        self.image_label.config(image=self.photo_image)

        self.title_label.config(text=title)
        # Clear, insert text, then disable editing
        self.explanation_text.delete("1.0", tk.END)
        self.explanation_text.insert(tk.END, explanation)
        self.explanation_text.config(state="disabled")  # Make read-only

 
        self.save_data_to_file({
            "title": title,
            "explanation": explanation,
            "image_url": image_url
        })

    def save_data_to_file(self, data):
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            try:
                with open(DATA_FILE, "r") as json_file:
                    existing_data = json.load(json_file)
                    if not isinstance(existing_data, list):
                        existing_data = []
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            fetch_date = datetime.now().strftime("%Y-%m-%d")
            existing_data.append({
                "title": data.get("title", "No Title"),
                "explanation": data.get("explanation", "No Explanation"),
                "image_url": data.get("image_url", ""),
                "fetch_date": fetch_date
            })
            with open(DATA_FILE, "w") as json_file:
                json.dump(existing_data, json_file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def save_current_image(self):
        if hasattr(self, "photo_image") and self.current_pil_image is not None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")]
            )
            if file_path and self.current_pil_image:
                self.current_pil_image.save(file_path)
                messagebox.showinfo("Success", f"Image saved as {file_path}")
            else:
                messagebox.showinfo("Info", "Save operation canceled.")
        else:
            messagebox.showwarning("Warning", "No image to save.")

def main():
    root = tk.Tk()
    app = APODApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()