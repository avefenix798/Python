# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:42:36 2024

@author: Emmanuel
"""

from tkinter import *
root = Tk()


def click_boton():
    texto = Label(root,text="No lo presiones" ).grid()
    
boton1 = Button(root , text= "No presiones el boton",bg= "red", padx=100, pady= 25 , command=click_boton ).grid(row=1,column=2)

root.mainloop()