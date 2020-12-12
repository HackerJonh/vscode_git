#GENERADORES SINTAXIS

#Funcion Basica sin usar Genrador:

def generaPares(limite):
    num=1
    
    miLista=[]
    
    while num<limite:
        miLista.append(num*2)
        
        num=num+1
        
    return miLista

print(generaPares(10))

#Usando el Generador


def generaPares2(limite):
    num = 1

    while num < limite:
        yield num*2
        num = num+1

devuelvePres=generaPares2(10)

for i in devuelvePres:
    print(i)





