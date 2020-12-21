class Coche():
    # En algunos casos vamos a necesitar que nuestras propiedades tengan un estado inicial para ello tenemos que hacer un constructor

    #Sintaxis del metodo constructor

    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        #Aveces necesitaremos que ciertas propiedades no puedan ser modificadas desde el exterior para ello necesitaremos colocar __en la propiedad en cuestion
        self.__ruedas = 4
        self.enmarcha = False

    # sintaxis del metodo

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if(self.enmarcha):

            return "El coche esta en marcha"
        else:

            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas", " Un ancho de: ",
              self.anchoChasis, " y un largo de: ", self.largoChasis)

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
