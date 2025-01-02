from tkinter import *
from tkinter import font

class CustomButton(Canvas):
    def __init__(self, parent, width, height, color, text=None, text_font=None, command=None):
        Canvas.__init__(self, parent, borderwidth=1, relief="raised", highlightthickness=0)
        self.command = command
        self.text = text
        self.color = color
        self.text_font = text_font if text_font else font.Font(family="Helvetica", size=12, weight="bold")
        padding = 4
        self.oval_id = self.create_oval((padding, padding, width + padding, height + padding), outline=color, fill=color)
        self.text_id = None
        if text:
            self.text_id = self.create_text(width / 2 + padding, height / 2 + padding, text=self.text, font=self.text_font, fill="white")
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0) + padding
        height = (y1 - y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
    def _on_press(self, event):
        self.configure(relief="sunken")
        
    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

    def set_font(self, font_name, font_size, font_weight):
        self.text_font = font.Font(family=font_name, size=font_size, weight=font_weight)
        if self.text_id:
            self.itemconfig(self.text_id, font=self.text_font)
        
    def get_font(self):
        return self.text_font

    def set_text(self, text):
        self.text = text
        if self.text_id:
            self.itemconfig(self.text_id, text=self.text)
        else:
            padding = 4
            width = int(self['width']) - padding * 2
            height = int(self['height']) - padding * 2
            self.text_id = self.create_text(width / 2 + padding, height / 2 + padding, text=self.text, font=self.text_font, fill="white")
        
    def get_text(self):
        return self.text

    def set_color(self, color):
        self.color = color
        self.itemconfig(self.oval_id, outline=color, fill=color)
        
    def get_color(self):
        return self.color

    def bind_event(self, event, handler):
        self.bind(event, handler)

    def unbind_event(self, event):
        self.unbind(event)

# Create the main window
root = Tk()
root.geometry("400x400")

# Create the custom rounded button without initial text
button = CustomButton(root, 100, 25, 'red')
button.pack()

# Example of setting the text, font, and color through user's edits
button.set_font("Arial", 14, "bold")
button.set_text("Press Here")
button.set_color("blue")

# Add event programming example
def on_custom_event(event):
    print("Custom event triggered!")

# Bind a custom event to the button
button.bind_event("<Button-3>", on_custom_event)  # Right-click to trigger the custom event

# Run the application
root.mainloop()
