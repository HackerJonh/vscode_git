from tkinter import *

raiz = Tk()
raiz.config(bg="Gray")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

nombre = Label(miFrame, text="Nombre: ")
nombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)
nombre.config(fg="Blue")

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1)


Apellido = Label(miFrame, text="Apellido:")
Apellido.grid(row=1, column=0, sticky="e", padx=5, pady=5)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=5, pady=5)

Direccion = Label(miFrame, text="Direccion")
Direccion.grid(row=2, column=0, sticky="e", padx=5, pady=5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=5, pady=5)

password = Label(miFrame, text="Password")
password.grid(row=3, column=0,sticky="e", padx=5, pady=5)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, sticky="e", padx=5, pady=5)
cuadroPass.config(show="*")

raiz.mainloop()
