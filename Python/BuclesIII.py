# Notacion Especial

for i in range(5):
    print(f"El valor de i es {i}")


# Range tambien admite otros valores como por ejemplo el inicio del conteo, el final del coneteo, y de cuanto va hacer el conteo

for a in range(5, 50, 3):
    print(f"El conteo de a es: {a}")

# La funcion len devuelve la longitud de un string

valido = False

email = input("Introduce tu email: ")

for b in range(len(email)):

    if email[b] =="@":

        valido = True

if valido:

    print("El email es correcto")
else:

    print("Email incorrecto")
