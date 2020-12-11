#Instrucciones pass ,continue y else

#Continue lo que hace es saltar a la siguiente instruccion en el bucle

nombre= "Python Informatico"

contador=0

for i in nombre:
    
    if i==" ":
        continue
    contador=contador+1

print(contador)

#La instruccion pass retorna nulo y se usa para cuando se quiere completar una instruccion mas tarde
    
 #Else dentro de un bucle es una herramienta mas que se puede usar dentro de un bucle para evaluar instrucciones

email=input("Introduce tu meail: ")

for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False 

print(arroba) 