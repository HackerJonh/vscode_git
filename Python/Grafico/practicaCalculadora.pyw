from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""

resultado=0

# Contruyendo la calculadora

# -------------------Pantalla------------------

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla, font=("arial",20,"bold"),width=22)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4,)
pantalla.config(background="black", fg="#03f943", justify="right",bd=20)

# -------------Pulsaciones Teclado---------------


def NumeroPulsado(num):
    global operacion
    
    if operacion != "":

        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#---------------Funcion Suma-----------------
def suma(num):

    global operacion

    global resultado

    resultado+=int(num)

    operacion = "suma"
    
    numeroPantalla.set(resultado)

def resta(num):
    
    global operacion

    global resultado

    resultado-=int(num)

    operacion = "resta"
    
    numeroPantalla.set(resultado)

def multi(num):

    global operacion

    global resultado

    resultado=int(num*num)

    operacion="multiplica"

#-----------------Funcion el_resultado------------

def el_resultado():

    global resultado

    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    
    resultado=0




# -----------Primera Fila de Botones------------


boton7 = Button(miFrame, text="7", width=9,height=4, command=lambda: NumeroPulsado("7"))
boton7.grid(row=2, column=1,padx=2,pady=2)

boton8 = Button(miFrame, text="8", width=9,height=4, command=lambda: NumeroPulsado("8"))
boton8.grid(row=2, column=2, padx=2, pady=2)

boton9 = Button(miFrame, text="9", width=9,height=4, command=lambda: NumeroPulsado("9"))
boton9.grid(row=2, column=3, padx=2, pady=2)

botonDiv = Button(miFrame, text="/", width=9, height=4 , bg="light blue",fg="red")
botonDiv.grid(row=2, column=4,padx=2,pady=2)

# -----------Segunda Fila de Botones---------------
boton4 = Button(miFrame, text="4", width=9,height=4, command=lambda: NumeroPulsado("4"))
boton4.grid(row=3, column=1,padx=2,pady=2)

boton5 = Button(miFrame, text="5", width=9,height=4, command=lambda: NumeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=9,height=4, command=lambda: NumeroPulsado("6"))
boton6.grid(row=3, column=3,padx=2,pady=2)

botonMult = Button(miFrame, text="X", width=9, height=4, bg="light blue",command=lambda:multi(numeroPantalla.get()))
botonMult.grid(row=3, column=4, padx=2, pady=2)

# -------------Tercera Fila de Botones----------

boton1 = Button(miFrame, text="1", width=9,height=4, command=lambda: NumeroPulsado("1"))
boton1.grid(row=4, column=1,padx=2,pady=2)

boton2 = Button(miFrame, text="2", width=9,height=4, command=lambda: NumeroPulsado("2"))
boton2.grid(row=4, column=2,padx=2,pady=2)

boton3 = Button(miFrame, text="3", width=9,height=4, command=lambda: NumeroPulsado("3"))
boton3.grid(row=4, column=3,padx=2,pady=2)

botonRest = Button(miFrame, text="-", width=9, height=4, bg="light blue", command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4,padx=2,pady=2)

# ------------Cuarta Fila de Botones-------------

boton0 = Button(miFrame, text="0", width=9,height=4, command=lambda: NumeroPulsado("0"))
boton0.grid(row=5, column=1,padx=2,pady=2)

botonComa = Button(miFrame, text=",", width=9, height=4,command=lambda: NumeroPulsado("."))
botonComa.grid(row=5, column=2,padx=2,pady=5)

botonIgual = Button(miFrame, text="=", width=9,height=4,command=lambda:el_resultado())
botonIgual.grid(row=5, column=3,padx=2,pady=2)

botonSum = Button(miFrame, text="+", width=9,height=4,bg="light blue",command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4, padx=2, pady=2)


raiz.mainloop()
