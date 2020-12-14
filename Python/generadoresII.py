#Yield from para usar en bucles anidados

def devuelveCiudades(*ciudades):
    
    for elemento in ciudades:
        
        yield from elemento
        
ciudades_devueltas=devuelveCiudades("Maracay","Valencia","Caracas","Barcelona")

print(next(ciudades_devueltas))
    