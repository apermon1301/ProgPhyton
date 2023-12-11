"""El ordenador piensa un número y debes acertarlo en menos de 10 intentos"""
from random import randint
aleatorio=randint(1,100)
# Variable de control para salir del bucle
control=0
# Almacenamos el número de intentos
intentos=0
while intentos<10 and control==0:
    num=int(input("Número:"))
    intentos=intentos+1
    if num<aleatorio:
        print("Debes introducir un número mayor")
    else:
        if num>aleatorio:
            print("Debes introducir un número menor")
        else:
            print("Acertastes en",intentos,"intentos")
            control=1
if control==0:
    print("Esto no es lo tuyo!!")


