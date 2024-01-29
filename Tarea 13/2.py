def crearLista():
    lista=[]
    n=int(input("¿Cuantos elementos tiene la lista? "))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

def mascaracteres(lista):
    palabra=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x]>len(palabras)):
            palabra=lista[x]
    return palabra

palabras=crearLista()
print(palabras)
print("Palabra con mas caracteres:",mascaracteres(palabras))
