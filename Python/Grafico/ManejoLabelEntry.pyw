from tkinter import *

raiz = Tk()
raiz.config(bg="Gray")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#Variable que creamos de tipo cadena que vamos asociar al cuadro texto para la accion de boton

minombre = StringVar()
miapellido=StringVar()

nombre = Label(miFrame, text="Nombre: ")
nombre.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nombre.config(fg="Blue")

cuadroNombre = Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0, column=1,sticky="e", padx=10, pady=10)


Apellido = Label(miFrame, text="Apellido:")
Apellido.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame,textvariable=miapellido)
cuadroApellido.grid(row=1, column=1, sticky="e", padx=10, pady=10)

Direccion = Label(miFrame, text="Direccion:")
Direccion.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, sticky="e", padx=10, pady=10)

password = Label(miFrame, text="Password:")
password.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3,column=1,sticky="e",padx=10,pady=10)

comentarios = Label(miFrame, text="Comentarios:")
comentarios.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textoComentario = Text(miFrame,width=15,height=5)
textoComentario.grid(row=4, column=1, sticky="e", padx=10, pady=10)


scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#Agregar Boton

def codigoBoton():
    minombre.set("Juan Manuel")
    miapellido.set("Silva Garcia")




botonEnvio = Button(raiz, text="Enviar",command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()
