#Polimorfismo

class coche():

    def desplazamiento(self):
        print("Me desplazo en cuatro Ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo en dos Ruedas")

class camion():

    def desplazamiento(self):
        print("Me desplazo en seis Ruedas") 

def desplazaVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=coche()
desplazaVehiculo(miVehiculo)