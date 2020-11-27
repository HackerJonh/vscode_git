#TUPLAS 

miTupla=("Ana","Maria","Nathalie","Jacinta")
print(("Mi tupla es: ",miTupla))

#Recorrer elementos de una Tupla

print("El indice numero 2 de mi tupla es: ",miTupla[2])

#Convertir la tupla en una lista

miLista=list(miTupla)
print("Mi tupla convertida en lista es: ",miLista)

#Convertir una lista en una tupla
miLista=tuple(miLista)
print("La lista Convertida en tupla",miLista)

#Consultar si hay un elemento en la tupla
print("¿Juan esta en mi tupla?:", "Juan"in miLista) #milista es una tupla por la conversion de arriba