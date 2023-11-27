x=1
suma=0
n=int(input("¿Cuántas alturas vas a introducir?"))
while x<=n:
    altura=float(input("Introduce una altura:"))
    x=x+1
    suma=suma+altura
media=suma/n
print("La altura promedio es:",media)
