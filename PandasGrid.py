import pandas as pd
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("DataFrame in Treeview")

tree = ttk.Treeview(root)
tree.pack(expand=True, fill='both')

# Assuming 'df' is your pandas DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 
                    'Age': [30, 24, 35], 
                    'City': ['New York', 'London', 'Paris']})

tree['columns'] = list(df.columns)
tree['show'] = 'headings' # Hide the default first column (index)

for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100) # Adjust width as needed

for index, row in df.iterrows():
    tree.insert("", "end", values=list(row.values))

root.mainloop()
