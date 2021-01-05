from tkinter import *

root = Tk()

varOpcion=IntVar()

Radiobutton(root, text="Masculino",variable=varOpcion,value=1).pack()

Radiobutton(root,text="Femenino",variable=varOpcion,value=2).pack()






root.mainloop()