#Serializar Objetos
import pickle
class vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.acelera = False
        self.enmarcha = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1 = vehiculos("Mazda", "MX5")

coche2 = vehiculos("Seat", "Leon")

coche3 = vehiculos("Renault", "Megane")

#Serializacion de objetos

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

#-------Abrir el fichero serializado-------------

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:

    print(i.estado())

