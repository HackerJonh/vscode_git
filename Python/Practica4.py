import math
print("CALCULO DE RAIZ CUADRADA")

numero = int(input("Introduce un numero: "))

contador=0

while numero<0:
    print("No se puede hayar la raiz de un numero negativo")
    
    if contador==2:
        print("Has consumido el numero maximo de intentos")
        break
    numero = int(input("Introduce un numero: "))
    
    if numero<0:
        contador=contador+1
    
if contador<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de "+str(numero)+" es: "+str(solucion))
    
    
