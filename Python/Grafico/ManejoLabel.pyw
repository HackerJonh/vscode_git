from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

# Crear etiqueta de texto.
miLabel = Label(miFrame, text="Hola Alumnos de Python",fg="blue",font=(14))
miLabel.place(x=50, y=50)


root.mainloop()
