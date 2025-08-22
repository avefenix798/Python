from tkinter import *
from tkinter import messagebox
top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

messagebox.showinfo(message="Bienvenido al aplicativo", title="Título")

top.mainloop()