import tkinter as tk
from tkinter import filedialog
import subprocess

def open_file():
    filepath = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if filepath:
        subprocess.Popen(['notepad.exe', filepath])  
        print(f"Selected file: {filepath}")
    else:
        print("No file selected.")

root = tk.Tk()
root.title("File Dialog Example")

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=20)

root.mainloop()
