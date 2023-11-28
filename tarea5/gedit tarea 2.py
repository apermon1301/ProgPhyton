suma=0
producto=1
for x in range(10):
    n=int(input("Número introducido:"))
    if x<5:
        suma=suma+n
    else:
         producto=producto*n
print("Suma de los primeros 5 números es",suma)
print("Producto de los últimos 5 números es",producto)
