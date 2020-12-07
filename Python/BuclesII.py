email = False
miEmail = input("Introduce tu direccion de Email: ")

for i in miEmail:
    
    if i=="@":
        email=True

if email:
    print("Email Correcto")
else:
    print("Email incorrecto")