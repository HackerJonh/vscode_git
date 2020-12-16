print("SISTEMA DE OPERACIONES MATEMATICAS")

print("")

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplica(num1,num2):
    return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:

        print("No se puede divider entre cero")

        return "Operacion erronea"
while True:
    try:    
        opt1=int(input("Introduce el primer Numero: "))

        opt2=int(input("Introduce el segundo numero: "))

        break

    except ValueError:

        print("Los valores introducidos no son correctos. Intentalo de Nuevo")


operacion=input("Introduce la operacion a Realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(opt1,opt2))
    
elif operacion=="resta":
    print(suma(opt1,opt2))

elif operacion=="multiplica":
    print(multiplica(opt1,opt2))

elif operacion=="divide":
    print(divide(opt1,opt2))
else:
    print("Operacion no contemplada")
