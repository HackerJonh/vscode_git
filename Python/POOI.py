#Sintaxis de una clase

class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    #sintaxis del metodo

    def arrancar(self):
       self.enmarcha=True

    #Creamos otro metodo para comprobar si el coche esta en marcha

    def estado(self):
        
        if(self.enmarcha):

            return "El coche esta en Marcha"

        else:

            return "El coche esta parado"

    #Acceder a las propiedades de la clase

miCoche=Coche()
print("El largo del coche es: ",miCoche.largoChasis)
print("El numero de ruedas del coche es: ",miCoche.ruedas)
miCoche.arrancar()
print(miCoche.estado())

print("----------A continuacion creamos el segundo objeto Instanciado------------")

miCoche2=Coche()
print("El largo del coche es: ",miCoche2.largoChasis)
print("El numero de ruedas del coche es: ",miCoche2.ruedas)
print(miCoche2.estado())

