"""Realizar la carga de dos nombres de personas distintos.
Mostrar por pantalla luego ordenados en forma alfabética"""
# Introducir los dos nombres
nombre1=int(input("Primer nombre:"))
nombre2=int(input("Segundo nombre:"))

if nombre1>nombre2:
    print(nombre2,"",nombre1)
else:
    print(nombre1,"",nombre2)
