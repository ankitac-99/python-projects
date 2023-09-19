import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)  # Clear the existing text
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

# Create the main application window
app = tk.Tk()
app.title("Text Editor")

# Create a text widget for text input
text = tk.Text(app, wrap=tk.WORD)
text.pack(expand=tk.YES, fill=tk.BOTH)

# Create a menu bar
menu = tk.Menu(app)
app.config(menu=menu)

# Create the "File" menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Start the main event loop
app.mainloop()
