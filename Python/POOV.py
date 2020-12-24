# HERENCIA

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

    # Sintaxis de la herencia


class Moto(vehiculos):
    hcaballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n",self.hcaballito)
    

class furgoneta(vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


#Sitanxis de Herencia Multiple

class VEelectricos(vehiculos):

    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VEelectricos,vehiculos):
    pass

#Cuando se aplica la herencia Multiple siempre tendra preferencia el constructor que este hacia la izquierda

miMoto = Moto("Corsa", "CBR")
miMoto.caballito()
miMoto.estado()
miFurgoneta=furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
miBici=BicicletaElectrica("Orbea","AC3400")

