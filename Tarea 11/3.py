productos=[]
precios=[]
for x in range(5):
    producto=input("Introduce un producto:")
    productos.append(producto)
    precio=float(input("Introduce un precio:"))
    precios.append(precio)
print("El precio del primer producto,",productos[0]," es ",precios[0])
print("Los productos con el precio superior son:")
for x in range(1,5):
    if (precios[x]>precios[0]):
       print(productos[x],"",precios[x])
