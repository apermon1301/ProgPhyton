class Socio:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del socio: ")
        sel.antiguedad=int(input("Ingrese la antigüedad: "))
        
    def imprimir(self):
        print(self.nombre,"tiene un antigüedad en años de ",self.antiguedad)

    def verAntiguedad(self):
        return self.antiguedad

class Club:
    def __init__(self):
        self.listaSocio=[]

    def agregarSocio(self):
        socio=Socio()
        self.socios.append(socio)

    def mostrarSocios(self):
        for socio in self.socios:
            socio.imprimir()

    def mostrarUnSocio(self):
        pos=int(input("Introduce la posición del socio a visualizar: "))
        if (pos<len(self.socios)):
            self.socios[pos].imprimir()

    def mostrarMayorAntiguedad(self):
        mayor=self.socios[0]
        for socio in self.socios:
            if socio.verAntiguedad>mayor.verAntiguedad:
                mayor=socio
        print("Socio de mayor antigüedad: ")
        mayor.imprimir()

club=Club()
club.agregarSocio()
club.agregarSocio()
club.agregarSocio()
club.mostrarSocios()
club.mostrarUnSocio()
club.mostrarMayorAntiguedad()
