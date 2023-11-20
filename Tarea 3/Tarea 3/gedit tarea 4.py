from math import sqrt
numA=int(input("Introduce el número A:"))
numB=int(input("Introduce el número B:"))
numB=int(input("Introduce el número C:"))
aux=numB*numB-4*numA*numC
if aux<0:
    print("Soluciones complejas")
else:
    raiz=sqrt(aux)
    x1=(-numB+raiz)/2*numA
    x2=(-numB-raiz)/2*numA
    print("Solución 1:",x1)
    print("Solución 2:",x2) 
