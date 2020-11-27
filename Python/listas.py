#LISTAS

mascotas=["Perro", "Gato","Gallina","Caballo","Pato"]

print(mascotas[:])
print("La primera posicion de mi lista es: ",mascotas[0])
print("La segunda Posicion de mi lista es: ",mascotas[1])
print ("La tercera Posicion de mi lista esÇ:  ",mascotas[2])
print("La cuarta Posicion de mi lista es:  ",mascotas[3])
print("La ultima Posicion de mi lista es: ",mascotas[4])


#Acceder a una porcion de la lista

print("Los 3 primeros animales de mi lista son: ",mascotas[0:3])

#Agregar elementos a una lista

mascotas.append("Loro")
print("Despues de agregar otro animal la lista queda en: ",mascotas[:])

#Agregando un elemento en una posicion especifica

mascotas.insert(2,"Oso")
print("Insertando otro animal en una posicion especifica: ",mascotas[:])

#Agregando varios elementos a la lista ya existente
mascotas.extend(["Tigre","Leon","Venado"])
print("La lista de animales extendida queda en: ",mascotas[:])

#Preguntar en que indice se encuentra un elemento
print("¿En que indice se encuentra tigre? :",mascotas.index("Tigre"))

#Consultar si un elemento se encuentra en la lista
print("¿Lobo se enecuentra en mi lista?: ", "Lobo" in mascotas)

#Eliminando un elemento de la lista
mascotas.remove("Loro")
print("Eliminando Loro de la lista: ",mascotas)

#Eliminando el ultimo elemento de una lista
mascotas.pop()
print("Eliminando el ultimo elemento de mi lista",mascotas)

    




