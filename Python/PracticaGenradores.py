# Genarar numeros pares

def generador(limite):

    num = 1

    while num < limite:
        yield num*2
        num=num+1
    
duvuelvepares=generador(20)

for i in duvuelvepares:
    print(i)
    
    #Si lo que queremos es que nos imprima uno a uno la lista usamos la sintaxist sig:
    
    #print(next(devuelvepares))
