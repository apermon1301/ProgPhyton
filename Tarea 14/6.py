def cargar_productos():
    productos=[]
    for x in range(5):
        producto=input("Introduce un producto: ")
        precio=int(input("Precio del producto: "))
        productos.append((producto,precio))
    return productos

def visualizar_productos(productos):
    print("Listado de todos los productos")
    for producto in productos:
        print(producto[0],"tiene un precio: ",producto[1])
        
        
def visualizar_productos_oferta(productos):
    print("Listado de los productos entre 10 y 15")
    for producto in productos:
        prod=producto[1]
        if(prod>=10 and prod<=15):
            print(producto[0],"tiene un precio: ",producto[1])        

productos=cargar_productos()
visualizar_productos(productos)
visualizar_productos_oferta(productos)
