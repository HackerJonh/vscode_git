def evalua_edad(edad):

    if edad<0:
        raise TypeError("No se puedo introducir una edad negativa")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres Joven"
    elif edad<60:
        return "Eres Maduro"
    elif edad<100:
        return "Cudate"
    

print(evalua_edad(-10))