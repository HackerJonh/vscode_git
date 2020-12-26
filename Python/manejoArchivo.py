# Sintaxis para trabajar con archivos externos que sirven para guardar datos
from io import open

# Para crear el archivo en modo escritura usamos la sig sintaxis:
# Se usa "w" para write "r" para read y "a" para agregar
archivo_texto = open("Archivo.txt", "w")

frase = "Estupendo dia para estudar python"
# write si el archivo esta vacio y se quiere escribir en el caso contrario se usa read() para leer
archivo_texto.write(frase)

archivo_texto.close()

