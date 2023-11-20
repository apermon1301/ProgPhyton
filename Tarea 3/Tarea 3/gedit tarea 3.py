cordX=int(input("Introduce una coordenada X:"))
cordY=int(input("Introduce una coordenada Y:"))
if cordX>0 and cordY>0:
    print("Está en el primer cuadrante")
if cordX<0 and cordY>0:
    print("Está en el segundo cuadrante")
if cordX<0 and cordY<0:
    print("Está en el tercer cuadrante")
if cordX>0 and cordY<0:
    print("Está en en el cuarto cuadrante")

