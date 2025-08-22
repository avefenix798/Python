# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:19:11 2024

@author: Emmanuel
"""

import tkinter as tk
import pandas as pd 
from tkinter import ttk
def Copiar():
    datos = pd.DataFrame({'Ventas':[23,34,45,34,34]}) 
    datos.to_clipboard()
    
    
    
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = ttk.Button(text="Copiar", command=Copiar)
boton.place(x=50, y=50)
root.mainloop()