print("Verificacion de Acceso")

edadUsuario=int(input("Introduce tu edad: "))

if edadUsuario<18:
    print("No puedes pasar")
elif edadUsuario>100:
    print("Edad Incorrecta")
else:
    print(("Puedes pasar"))
