# HERENCIA SUPER()

class persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "\nEdad: ", self.edad,
              "\nResidencia: ", self.lugar_residencia)


class Empleado(persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        #El metodo super indica que ademas de los atributos de la clase empleado va heredar los de la clase persona

        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

        #Esto soluciona poder implementar ademas de los atributos propios de la clase empleado poder heredar los de la clase persona
        
        #Ahora hacemos lo mismo con el metodo descripcion
    def descripcion(self):

        super().descripcion()

        print("Salario: ",self.salario,"\nAntiguedad: ",self.antiguedad)



Antonio=Empleado(1500,15,"Antonio",55,"Colombia")

Antonio.descripcion()
