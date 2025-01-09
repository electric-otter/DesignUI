import tkinter as tk
from tkinter import ttk, filedialog
import platform

def adjust_for_os(os_name=None):
    if os_name is None:
        os_name = platform.system()
    if os_name == "Windows":
        window.title("Windows Compatibility")
        window.geometry("800x600")
        # Add more Windows-specific settings here
    elif os_name == "Darwin":
        window.title("macOS Compatibility")
        window.geometry("1024x768")
        window.attributes('-fullscreen', True)  # Start in fullscreen mode for macOS
        # Add more macOS-specific settings here
    elif os_name == "Linux":
        window.title("Linux Compatibility")
        window.geometry("1280x720")
        window.config(bg='lightgrey')  # Change background color for Linux
        # Add more Linux-specific settings here
    else:
        window.title(f"{os_name} Compatibility")
        window.geometry("800x600")

def change_icon():
    filetypes = [
        ("ICO files", "*.ico"),
        ("PNG files", "*.png"),
        ("All files", "*.*")
    ]
    icon_path = filedialog.askopenfilename(title="Select Icon", filetypes=filetypes)
    if icon_path:
        window.iconphoto(True, tk.PhotoImage(file=icon_path))

def set_os(os_name):
    adjust_for_os(os_name)

window = tk.Tk()
adjust_for_os()

frame = ttk.Frame(window, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

resizable_button = ttk.Button(frame, text="Resizable", command=lambda: window.resizable(True, True))
resizable_button.grid(row=0, column=0, padx=5, pady=5)

fixed_size_button = ttk.Button(frame, text="Fixed Size", command=lambda: window.resizable(False, False))
fixed_size_button.grid(row=0, column=1, padx=5, pady=5)

fullscreen_button = ttk.Button(frame, text="Fullscreen", command=lambda: window.attributes('-fullscreen', True))
fullscreen_button.grid(row=1, column=0, padx=5, pady=5)

windowed_button = ttk.Button(frame, text="Windowed", command=lambda: window.attributes('-fullscreen', False))
windowed_button.grid(row=1, column=1, padx=5, pady=5)

change_icon_button = ttk.Button(frame, text="Change Icon", command=change_icon)
change_icon_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

windows_button = ttk.Button(frame, text="Windows OS", command=lambda: set_os("Windows"))
windows_button.grid(row=3, column=0, padx=5, pady=5)

macos_button = ttk.Button(frame, text="macOS", command=lambda: set_os("Darwin"))
macos_button.grid(row=3, column=1, padx=5, pady=5)

linux_button = ttk.Button(frame, text="Linux OS", command=lambda: set_os("Linux"))
linux_button.grid(row=4, column=0, padx=5, pady=5)

newos_button = ttk.Button(frame, text="NewOS", command=lambda: set_os("NewOS"))
newos_button.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
