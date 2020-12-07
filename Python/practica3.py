print("Asiganaturas optativas 2020")

print("Asignaturas Optativas: Informatica - Manualidades -Artistica")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in("informatica","manualidades","artistica"):
    print("Asignatura escogida: "+asignatura)
else:
    print("La asignatura no esta contemplada")
