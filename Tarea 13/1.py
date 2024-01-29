def crearLista():
    lista=[]
    n=int(input("¿Cuantos elementos tiene la lista? "))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

def multiplicar(lista,n):
    for x in range(len(lista)):
        lista[x]=lista[x]*n
    print(lista)

lista=crearLista()
print(lista)
n=int(input("Multiplicando:"))
multiplicar(lista,3)
