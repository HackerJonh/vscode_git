import tkinter as tk
from tkinter import Menu, filedialog
from tkinter import messagebox

root = tk.Tk()

#Creacion de una ventana Emergente

def infoAdicional():
    messagebox.showinfo("Programa Juan", "Practica Python Version 2021")
    
def info_Licencia():
    messagebox.showwarning("Licencia", "Producto bajo Licencia GNU")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la Aplicacion?")
  #Si quremos cambiar el si o no por aceptar o cancelar debemos cambiar el metodo askquestion por askokcancel
    if valor == "yes":
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar.Documento Bloqueado")

    if valor == False:
        root.destroy()

def Abrir_Fichero():
    fichero = filedialog.askopenfilename(title="Abrir",filetypes=(("Ficheros de Excel","*.xls"),("Ficheros de Texto","*.txt")))

def new_windows():
    nueva_ventana = tk.Toplevel(bg="blue")
    nueva_ventana.title("Nueva Ventana")
    Etiqueta = tk.Label(nueva_ventana, text="Nueva Ventana")
    Etiqueta.pack()
    
    

barMenu = tk.Menu(root)

root.config(menu=barMenu, width=300, height=300)

Archivo = tk.Menu(barMenu, tearoff=0)

Edicion = tk.Menu(barMenu, tearoff=0)

Herramientas = tk.Menu(barMenu, tearoff=0)

Ayuda = tk.Menu(barMenu, tearoff=0)

barMenu.add_cascade(label="Archivo", menu=Archivo)
# ---------Agregando submenu----------------
Archivo.add_command(label="Abrir", command=Abrir_Fichero)
Archivo.add_command(label="Nuevo",command=new_windows)
Archivo.add_command(label="Guardar")
Archivo.add_command(label="Guardar Como")
Archivo.add_separator()
Archivo.add_command(label="Cerrar",command=cerrarDocumento)
Archivo.add_command(label="Salir",command=salirAplicacion)

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
Ayuda.add_command(label="Licencia",command=info_Licencia)
Ayuda.add_command(label="configuracion Adicional")

root.mainloop()
