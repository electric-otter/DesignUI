from tkinter import *

def search():
    query = search_entry.get()
    # Perform your search logic here using the 'query' variable
    print("Search query:", query)

root = Tk()
root.title("Search...")

search_label = Label(root, text="Search:")
search_label.pack(side="left")

search_entry = Entry(root)
search_entry.pack(side="left", fill="x", expand=True)

search_button = Button(root, text="Search", command=search)
search_button.pack(side="left")

root.mainloop()
