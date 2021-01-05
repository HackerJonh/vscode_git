import tkinter as tk
from tkinter import ttk

win = tk.Tk()

#Agregando Titulo
win.title("Ejemplo de importacion de Modulo")

#Agregando un Label

etiquetaA = ttk.Label(win, text="Una Etiqueta")
etiquetaA.grid(column=0, row=0)

#Agregando un evento a un Boton

def click_me():
    action.configure(text="Me has presionado")
    etiquetaA.configure(foreground="red")
    etiquetaA.configure(text="Una etiqueta roja")

#Agregando el boton

action = ttk.Button(win, text="Presioname", command=click_me)
action.grid(column=1, row=0)


win.mainloop()