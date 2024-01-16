lista1=[]
lista2=[]
lista3=[]
for x in range(4):
    valor=input("Introduce un número a la lista 1:")
    lista1.append(valor)
    valor=input("Introduce un número a la lista 2:")
    lista2.append(valor)
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
print("La lista resultante:",lista3) 
