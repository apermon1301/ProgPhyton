aprobados=0
suspensos=0
x=1
while x<=10:
    nota=int(input("Ingrese una nota:"))
    if nota>=5:
              aprobados=aprobados+1
    else:
        suspensos=suspensos+1
print("Aprobados:",aprobados)
print("Suspensos:",suspensos)
              
