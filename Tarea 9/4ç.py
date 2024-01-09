lista=[]
for x in range(5):
    valor=float(input("Introduce una altura:"))
    lista.append(valor)
suma=0
for x in range(5):
    suma=suma+lista[x]
promedio=suma/5
print("La altura media es",promedio)
supera=0
nosupera=0
for x in range(5):
    if lista[x]>promedio:
        supera=supera+1
    else:
        nosupera=nosupera+1
print("Personas superrior a la media:",supera)
print("Personas inferior a la media:",nosupera)
print()
