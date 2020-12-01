#Sintaxis if
print("Programa de evaluacion de Notas")

nota_Alumno=input("Introduce una Nota")


def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Supenso"
    return valoracion
    
print(evaluacion(int(nota_Alumno)))