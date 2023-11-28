n=int(input("Números introducidos:"))
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
for x in range(n):
    cordX=float(input("Coordenada X:"))
    cordY=float(input("Coordenada Y:"))
    if cordX>0 and cordY>0:
        print("Primer cuadrante")
        cuadrante1=cuadrante1+1
    else:
         if cordX<0 and cordY>0:
             print("Segundo cuadrante")
             cuadrante2=cuadrante2+1
         else:
             if cordX<0 and cordY<0:
                 print("Tercer cuadrante")
                 cuadrante3=cuadrante3+1
             else:
                 print("Cuarto cuadrante")
                 cuadrante4=cuadrante4+1
print("Primer cuadrante:",cuadrante1)
print("Segundo cuadrante:",cuadrante2)
print("Tercer cuadrante:",cuadrante3)
print("Cuarto cuadrante:",cuadrante4)
    
