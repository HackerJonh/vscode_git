print("EVALUACION DE SALARIO")
print("")

salarioPresidente=int(input("Introduce el salario del presidente: "))
print("Salario Presidente: ",salarioPresidente)

salarioDirector=int(input("Introduce el salario del Director: "))
print("Salario Director: ",salarioDirector)

salarioJefeArea=int(input("Introduce el salario del Jefe de Area: "))
print("Salario Jefe de Area: ",salarioJefeArea)

salarioAdministrativo=int(input("Introduce el Slario del Administrativo: "))
print("Slario Administrativo",salarioAdministrativo)

def EvaluadorSalarial():
    if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
        print("La empresa Funciona bien")
    else:
        print("Algo anda mal")
  
EvaluadorSalarial()      
