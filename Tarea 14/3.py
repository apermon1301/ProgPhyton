def cargar_empleados():
    empleados=[]
    for x in range(5):
        nombre=input("Introduce un nombre: ")
        sueldo1=int(input("Introduce el primer sueldo: "))
        sueldo2=int(input("Introduce el segundo sueldo: "))
        sueldo3=int(input("Introduce el tercer sueldo: "))
        empleado=[]
        empleado.append(nombre)
        empleado.append((sueldo1,sueldo2,sueldo3))
        empleado.append(empleado)
    return empleados

def visualizar(empleados):
    for empleado in empleados:
        total=0
        for sueldo in empleados[1]:
            total=total+sueldo
            print(empleado[0],"tiene un sueldo trimestral de",total)

def visualizarSuperior(empleados):
    print("Los empleados con un monto trimestral superior a 10000 son: ")
    for empleado in empleados:
        total=0
        for sueldo in empleados[1]:
            total=total+sueldo
            if total>10000:
                print(empleado[0],"tiene un sueldo trimestral de",total)

empleados=cargar_empleados()
visualizar(empleados)
visualizarSuperior(empleados)
