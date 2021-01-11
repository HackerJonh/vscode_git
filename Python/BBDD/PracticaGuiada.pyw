import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, ttk,font,messagebox
from tkinter import *



#------------Propiedades Ventanas---------------
root=Tk()
root.title("Practica Guiada 1")
root.config(bg="Light Gray")

#-----------Variables----------

fuente = font.Font(weight='bold')

#------------Frame-------------------
miFrame=tk.Frame(root,width=600,height=600)
miFrame.pack()


#-----------Menus------------------
barMenu=tk.Menu(root)
root.config(menu=barMenu, width=300, height=300)

BDD=tk.Menu(barMenu,tearoff=0)

Borrar=tk.Menu(barMenu,tearoff=0)

Crud=tk.Menu(barMenu,tearoff=0)

Ayuda=tk.Menu(barMenu,tearoff=0)

barMenu.add_cascade(label="BDD",menu=BDD)
barMenu.add_cascade(label="Borrar",menu=Borrar)
barMenu.add_cascade(label="CRUD",menu=Crud)
barMenu.add_cascade(label="Ayuda",menu=Ayuda)

#----------------------SubMenu----------------------
BDD.add_command(label="Conectar")
BDD.add_command(label="Salir")
Borrar.add_command(label="Borrar Datos")
Crud.add_command(label="Crear")
Crud.add_command(label="Leer")
Crud.add_command(label="Actualizar")
Crud.add_command(label="Borrar")
Ayuda.add_command(label="Licencia")
Ayuda.add_command(label="Acerca de")

#----------------------Labels----------------

Id=tk.Label(miFrame,text="ID")
Id.grid(row=0,column=0,sticky="e",padx=10,pady=10)

Nombre=ttk.Label(miFrame,text="Nombre: ")
Nombre.grid(row=1,column=0,sticky="e",padx=10,pady=10)

Apellido=ttk.Label(miFrame,text="Apellido: ")
Apellido.grid(row=2,column=0,sticky="e",padx=10,pady=10)

Password = ttk.Label(miFrame, text="Password: ")
Password.grid(row=3, column=0, sticky="e", padx=10, pady=10)

Direccion=ttk.Label(miFrame,text="Direccion: ")
Direccion.grid(row=4,column=0,sticky="e",padx=10,pady=10)

#----------------Entry----------------------
cuadroId=ttk.Entry(miFrame)
cuadroId.grid(row=0,column=1,sticky="e",padx=10,pady=10)

cuadroNombre=ttk.Entry(miFrame)
cuadroNombre.grid(row=1, column=1, sticky="e", padx=10, pady=10)

cuadroApellido=ttk.Entry(miFrame)
cuadroApellido.grid(row=2,column=1,sticky="e",padx=10,pady=10)

cuadroPass = ttk.Entry(miFrame,show="*")
cuadroPass.grid(row=3, column=1, sticky="e", padx=10, pady=10)

cuadroDireccion = ttk.Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, sticky="e", padx=10, pady=10)

#----------------Buttons---------------------

botonCrear=ttk.Button(miFrame,text="Create")
botonCrear.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)

botonRead = ttk.Button(miFrame, text="Read")
botonRead.grid(row=5, column=1, sticky=S+N+E+W, padx=2, pady=2)

botonUpdate = ttk.Button(miFrame, text="Update")
botonUpdate.grid(row=5, column=2, sticky=S+N+E+W, padx=2, pady=2)

botonDelete = ttk.Button(miFrame, text="Delete")
botonDelete.grid(row=5, column=3, sticky=S+N+E+W, padx=2, pady=2)



















root.mainloop()
