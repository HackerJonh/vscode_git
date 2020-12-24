import sys
from termcolor import colored,cprint
#Encapsulacion de metodos



class Coche():
   

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

   
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):

            chequeo=self.chequeo_Interno()

        if(self.__enmarcha and chequeo):

            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo==False):
            cprint ("Algo anda mal en el chequeo","white","on_red")

        else:
            return "El coche esta parado"

    def estado(self):
        
        print("El coche tiene ", self.__ruedas, " ruedas", " Un ancho de: ",
              self.__anchoChasis, " y un largo de: ", self.__largoChasis)
    
    def chequeo_Interno(self):
        cprint("Realizando Chequeo interno","red","on_green")
        self.gasolina="ok"
        self.aceite="no"
        self.puertas="cerradas"

        if(self.gasolina=="ok"and self.aceite=="ok"and self.puertas=="cerradas"):
            return True
        else:
            return False

    # Acceder a las propiedades de la clase


miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print("")

print("----------A continuacion creamos el segundo objeto Instanciado------------")
print("")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
