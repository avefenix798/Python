# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:15:19 2024

@author: Emmanuel
"""
from tkinter import *
root = Tk()
etiqueta1 = Label(root, text="¡Hola Mundo!").pack()
etiqueta2 = Label(root, text="Informacion" ).pack()



marco_principal= Frame()
marco_principal.pack()
marco_principal.config(width="800" , height="600")
marco_principal.config( bg="white")
root.mainloop()