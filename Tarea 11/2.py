nombres=[]
notas=[]
for x in range(5):
    nombre=input("Introduce un nombre:")
    nombres.append(nombre)
    nota=int(input("Introduce una nota:"))
    notas.append(nota)
print("Alumnos aprobados:")
for x in range(10):
    if notas[x]>=5:
       print(nombres[x],"",notas[x])
print("Alumnos suspensos:")
for x in range(10):
    if notas[x]<5:
        print(nombres[x],"",notas[x])

              
