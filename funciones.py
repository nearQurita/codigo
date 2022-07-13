valido = True
import numpy as np
casillero = np.empty(shape=(3,3),dtype=('U',10))

def validar_menu():
    while valido:
        try:
            opcion = int(input("\nIngrese la opcion que desee:\t"))
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                return opcion
            else:
                print("\nError: ingrese opcion 1,2,3,4,5 segun corresponda")
        except ValueError:
            print("\nError: ingrese la opcion como un numero")

def arrendar(casillero):

    while valido:
        print( "\nArrendar casilleros")
        print("---------------------")
        print(" 1- nivel 1: $10.000 ")
        print(" 2- nivel 2: $ 5.000 ")
        print(" 3- nivel 3: $ 3.000 ") 
        try:
            opcion=int(input("\nIngrese un nivel de casillero : "))#fila
            fila = opcion - 1
            casillerosDisponibles(casillero,fila)
            nroCasillero = int(input("\nIngrese el  numero del casillero : "))#columna
            columna = nroCasillero - 1
            while valido:
                nombre = str(input("\nIngrese su nombre : "))
                if len(nombre) >= 10:
                    casillero [fila,columna] = nombre
                    break
                else:
                    print("\nError, ingrese de minimo 10 de largo")
            var =  "a"
            return var
        except:
            print("\nError")
            input("\nPresione enter para continuar: ")

def calcularGanancia (casillero):
  total=0
  fil= 1
  for fila in casillero:
    for columna in fila:
      if columna != "":
        if fil ==1:
          total += 10000
        elif fil ==2:
          total+= 5000
        elif fil ==3:
          total+=3000
    fil += 1
  print("\nEl total es  $ ",total)

def casillerosDisponibles(casillero,fila):
  print("\nCasilleros disponibles " ,fila+1)
  nroCasillero = 1
  for columna in casillero[fila]:
    if columna == "": # aca no está ocupada
      print("\nCasillero ",nroCasillero)
    nroCasillero +=1

def mostrarDisponibles(casillero):
  print("\nCasilleros disponibles ")
  filas = ""
  nroCasillero =1
  valor =""
  for fila in casillero:
    for columna in fila:
      if columna== "":
        valor=str(nroCasillero)
      else:
        valor = "X"
      filas += valor + " "
      nroCasillero +=1
    filas+= "\n"
  print(filas)
  input("\nPresione enter para continuar :")

def mostrarNombres(casillero):
  print("\nClientes en los casilleros \n")
  nroCasillero =1
  for fila in casillero:
    for columna in fila:
        if columna != "":
            print("Casillero : ",nroCasillero, "Nombre :" ,columna)
        else:
            print("Casillero : ",nroCasillero, "Nombre : vacio")
        nroCasillero +=1
  input("\nPresione cualquier tecla para continuar :")