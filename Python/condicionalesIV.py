#Operador and y OR

print("Evaluador de becas 2020")

distanciaEscuela=int(input("Introduce la distancia a la escuela en KM"))
print("Distancia a la escuela: "+distanciaEscuela)

numerosHermanos=int(input("Introduce el numero de hermanos que tienes"))
print("Numero de hermanos: "+numerosHermanos)

salarioFamiliar=int(input("Introduce cuanto es el salario bruto anual"))
print("Salario Familiar: "+salarioFamiliar)

if distanciaEscuela>40 and numerosHermanos>2 or salarioFamiliar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a una beca")
