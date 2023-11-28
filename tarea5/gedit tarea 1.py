n=int(input("¿Cuantos triángukos?"))
for x in range(n):
    base=float(input("Base del triángulo:"))
    altura=float(input("Altura del triángulo:"))
    Superficie=base*altura/2
    print("El triángulo cuya base es",base, "y la altura",altura, "tiene una superficie:",superficie)
    if superficie>12:
        cantidad=cantidad+1
print("Cantidad de triángulos cuya superficie es superior a 12:",cantidad)
