from tkinter import *

class TextWidget:
    def __init__(self, root):
        self.root = root
        self.text_widget = Text(root, height=5, width=30)
        self.text_widget.pack()

    def error(self):
        self.text_widget.insert(END, "DesignUI has an error.")

    def change_label(self, new_text):
        if new_text:  # Check if new_text is provided
            self.text_widget.delete(1.0, END)
            self.text_widget.insert(END, new_text)
        else:  # If new_text is not provided, call the error method
            self.error()

# Example usage
if __name__ == "__main__":
    root = Tk()
    text_widget = TextWidget(root)
    text_widget.change_label("")  # This will call the error method
    root.mainloop()
