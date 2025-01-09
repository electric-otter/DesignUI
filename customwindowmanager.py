import tkinter as tk
from tkinter import ttk

class CustomWindowManager:
    def __init__(self, root, settings=None):
        self.root = root
        self.root.title("Custom Window Manager")

        # Default settings
        self.settings = {
            "window_size": "400x300",
            "background_color": "#f0f0f0",
            "button_text": "Close",
            "button_command": self.root.quit
        }

        # Update settings with user-defined settings
        if settings:
            self.settings.update(settings)

        # Set window size
        self.root.geometry(self.settings["window_size"])

        # Modern style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TFrame", background=self.settings["background_color"])

        # Create a frame
        frame = ttk.Frame(root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Add a close button
        close_button = ttk.Button(frame, text=self.settings["button_text"], command=self.settings["button_command"])
        close_button.pack(pady=20)

    def update_settings(self, settings):
        self.settings.update(settings)
        # Apply changes to the window manager
        self.root.geometry(self.settings["window_size"])
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    custom_settings = {
        "window_size": "600x400",
        "background_color": "#d3d3d3",
        "button_text": "Exit",
        "button_command": root.quit
    }
    app = CustomWindowManager(root, custom_settings)
    root.mainloop()
