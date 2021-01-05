import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

root = tk.Tk()

#Creacion de una ventana Emergente

def infoAdicional():
    messagebox.showinfo("Programa Juan","Practica Python Version 2021")

barMenu = tk.Menu(root)

root.config(menu=barMenu, width=300, height=300)

Archivo: Menu = tk.Menu(barMenu, tearoff=0)

Edicion = tk.Menu(barMenu, tearoff=0)

Herramientas = tk.Menu(barMenu, tearoff=0)

Ayuda = tk.Menu(barMenu, tearoff=0)

barMenu.add_cascade(label="Archivo", menu=Archivo)
# ---------Agregando submenu----------------
Archivo.add_command(label="Nuevo")
Archivo.add_command(label="Guardar")
Archivo.add_command(label="Guardar Como")
Archivo.add_separator()
Archivo.add_command(label="Cerrar")
Archivo.add_command(label="Salir")

barMenu.add_cascade(label="Edicion", menu=Edicion)
# ---------Agregando submenu------------------
Edicion.add_command(label="Deshacer")
Edicion.add_command(label="Rehacer")
Edicion.add_command(label="Copiar")
Edicion.add_command(label="Pegar")

barMenu.add_cascade(label="Herramientas", menu=Herramientas)
# -----------Agregando submenu-----------------
Herramientas.add_command(label="Sleccionar Linea")
Herramientas.add_command(label="Busqueda Avanzada")
Herramientas.add_command(label="Filtrar ip")

barMenu.add_cascade(label="Ayuda", menu=Ayuda)
# -----------Agregando submenu------------------
Ayuda.add_command(label="Documentos")
Ayuda.add_command(label="Informacion de Version",command=infoAdicional)
Ayuda.add_command(label="configuracion Adicional")

root.mainloop()
