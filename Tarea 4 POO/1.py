class Cuenta:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.monto=int(input("Ingrese monto: "))

    def imprimir(self):
        print(self.nombre,"tiene un monto de",self.monto)

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()

    def imprimir(self):
        super().imprimir()

class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.intereses=float(input("Interés:"))
        self.imposicion=float(input("Plazo de imposición:"))

    def imprimir(self):
        super().imprimir()
        print("Intereses : ",self.intereses)
        print("Plazo de imposición: ",self.imposicion)

    def ganancia(self):
        ganancia=self.monto*self.intereses/100
        print("Ganancia: ",ganancia)
     
    

caja=CajaAhorro()
caja.imprimir()

plazo=PlazoFijo()
plazo.imprimir()
plazo.ganancia()
