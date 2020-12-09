import math

#Sintaxis del Bucle while
i=1

while i<=10:
    print("Ejecucion de codigo")
    i=i+1

print("Termino la ejecucion")

#Ejercicio 1

print("Programa de Calculo de raiz Cuadrada")

numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")
    
    if intentos==2:
        print("Has consumido muchos intentos")
        break
    numero=int(input("Introduce un numero: "))
    
    if numero<0:
        intentos=intentos+1
        
if intentos<2:
    
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de: " +str(numero)+ " es " +str(solucion))
    