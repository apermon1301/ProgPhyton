class Jugador:
    juego=30
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.puntaje=int(input("Ingrese puntos: "))

    def imprimir(self):
        print(self.nombre,"tiene los siguientes puntos",self.puntaje)
        print("El tiempo que queda es: ",Jugador.juego)
    def pasarTiempo(self):
        Jugador.juego=Jugador.juego-1


jugador1=Jugador()
jugador2=Jugador()
for x in range(10):
    jugador1.pasarTiempo()
jugador1.imprimir()
while Jugador.juego>0:
    jugador2.imprimir()
    jugador2.pasarTiempo()
