import tkinter as tk
from tkinter import *
from tkinter import ttk

root =tk.Tk()

root.title("Ejemplo")

#---------Variables---------
playa = IntVar()
Montana = IntVar()
Turismo = IntVar()
image_dir="C:\\Users\\Nathalie\\Desktop\\vscode_git\\Python\\Grafico\\turismo.png"

def opcionesViaje():

    opcionEscogida = ""
    
    if (playa.get() == 1):
        opcionEscogida += " playa"

    if (Montana.get() == 1):
        opcionEscogida += " montana"

    if (Turismo.get() == 1):
        opcionEscogida += " Turismo Local"
    
    textoFinal.config(text=opcionEscogida)
        
#Colocando una imagen       
photo = PhotoImage(file=image_dir)
Label(root,image=photo).pack()     


frame = ttk.Frame(root)
frame.pack()

Label(frame,text="Elige destinos",width=50).pack()

ttk.Checkbutton(frame, text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
ttk.Checkbutton(frame, text="Montaña",variable=Montana,onvalue=1,offvalue=0,command=opcionesViaje).pack()
ttk.Checkbutton(frame, text="Turismo", variable=Turismo,onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()
