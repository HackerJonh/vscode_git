from tkinter import *

raiz = Tk()

#Cambiar el titulo de la ventana
raiz.title("Ventana de prueba")

#Cambiar el Ancho y el largo de la ventana
#raiz.geometry("650x400")

#Cambiar el color de fondo de la ventana
raiz.config(bg="gray")

#Redimencionar ventana
raiz.resizable(True,True)

#----------Creacion del Frame--------------------

miFrame = Frame()
#El atributo pack permite diferntes parametros side, fill, anchor. Revisar documentacion
miFrame.pack(fill="both",expand="True")

miFrame.config(bg="gray")

miFrame.config(width="350",height="350")

#Cambiar el borde
miFrame.config(bd=20)
miFrame.config(relief="groove")

#Cambiar el cursosr del frame
miFrame.config(cursor="pirate")

#Metodo para que la ventana sea constante
raiz.mainloop()
