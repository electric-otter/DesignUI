import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageUploader(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.upload_btn = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if file_path:
            img = Image.open(file_path)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploader(master=root)
    app.pack()
    root.mainloop()
