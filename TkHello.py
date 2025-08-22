# -*- coding: utf-8 -*-
"""
Created on Fri May 30 12:05:26 2025

@author: avefe
"""
import tkinter as tk 
from tkinter import ttk 
import win32com.client

def saludar():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    s= 'Hola Mundo'
    print(s)
    speaker.Speak(s)


root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = ttk.Button(text="¡Hola, mundo!", command=saludar)
boton.place(x=50, y=50)
root.mainloop()


