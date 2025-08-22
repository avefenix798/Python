# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 00:01:16 2023

@author: Emmanuel
"""

import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()