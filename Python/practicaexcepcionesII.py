import math

def calculo_Raiz(num1):

    if num1<0:

        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un numero para el calculo de la raiz: "))

try:
     print(calculo_Raiz(op1))

except ValueError as numeroNegativo:
    
    print(numeroNegativo)