from funciones import *
import numpy as np
casillero = np.empty(shape=(3,3),dtype=('U',10))
menu = True
var = None
while menu:
    print("*"*40)
    print( "ARRIENDO DE CASILLEROS")
    print("-"*40)
    print("1- Arrendar casilleros ")
    print("2- Mostrar disponibles ")
    print("3- Lista de nombres de cliente ")
    print("4- Ganancias totales ")
    print("5- Salir del sistema" )
    print("*"*40)
    opcion = validar_menu()
    if opcion == 1:
        var = arrendar(casillero)
    elif opcion == 2:
        if var != None:
            mostrarDisponibles(casillero)
        else:
            print("\nError: no hay usuarios registrados, ingrese a la opcion 1")
    elif opcion == 3:
        if var != None:
            mostrarNombres(casillero)
        else:
            print("\nError: no hay usuarios registrados, ingrese a la opcion 1")
    elif opcion == 4:
        calcularGanancia(casillero)
    elif opcion == 5:
        print("\nSaliendo del programa..\nAutor: Gonzalo Ulloa\nVersion: 1.0")
        break

print("\nQue tenga un buen dia")
