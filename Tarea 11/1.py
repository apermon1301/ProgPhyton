nombres=[]
sueldos=[]
for x in range(5):
    nombre=input("Introduce un nombre:")
    nombres.append(nombre)
    sueldo=int(input("Introduce un sueldo:"))
    sueldos.append(sueldo)
mayor=0
menor=9999999
posMayor=0
posMenor=0
for x in range(5):
    if sueldos[x]>mayor:
        mayor=sueldos[x]
        posMayor=x
    if sueldos[x]<menor:
        menor=sueldos[x]
        posMenor=x
print("El sueldo mayor es ",mayor," y pertenece a ",nombres[posMayor])
print("El sueldo menor es ",menor," y pertenece a ",nombres[posMenor])

              
