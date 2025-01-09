import tkinter as tk

class Counter:
    def __init__(self, root, start=0, increment_step=1, decrement_step=1, 
                 font=("Arial", 48), bg="white", fg="black"):
        self.value = start
        self.increment_step = increment_step
        self.decrement_step = decrement_step
        self.root = root
        self.root.title("Counter")
        self.root.configure(bg=bg)

        self.label = tk.Label(root, text=str(self.value), font=font, bg=bg, fg=fg)
        self.label.pack()

        self.increment_button = tk.Button(root, text="Increment", command=self.increment)
        self.increment_button.pack(side=tk.LEFT)

        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        self.decrement_button.pack(side=tk.RIGHT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.BOTTOM)

    def increment(self):
        self.value += self.increment_step
        self.update_label()

    def decrement(self):
        self.value -= self.decrement_step
        self.update_label()

    def reset(self):
        self.value = 0
        self.update_label()

    def update_label(self):
        self.label.config(text=str(self.value))

if __name__ == "__main__":
    root = tk.Tk()
    app = Counter(root, start=0, increment_step=1, decrement_step=1, 
                  font=("Arial", 48), bg="lightblue", fg="black")
    root.mainloop()
