#Sintaxis de un Diccionario

miDiccionario={"Nombre":"Juan","Apellido":"Silva","Edad":32,"Nacimiento":1988}

print("Mi diccionario es: ",miDiccionario)
print("La clave de Nombre es: ",miDiccionario["Nombre"])
print("La clave apellido es: ",miDiccionario["Apellido"])

#Agregar un elemento al diccionario

miDiccionario["Sexo"]="Masculino"
print(miDiccionario)

#Eliminar un elemento
del miDiccionario["Nacimiento"]
print("Eliminando un elememnto del diccionario queda:",miDiccionario)