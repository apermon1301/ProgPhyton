class Jugador:
    juego=30
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.puntaje=int(input("Ingrese puntos: "))

    def __str__(self):
        cadena=self.nombre+"tiene una puntuación de"+self.puntaje
        if self.puntaje>1000:
            cadena=cadena+"y es Experto"
        else:
            cadena=cadena+"y es Principiante"
        return cadena

jugador1=Jugador()
jugador2=Jugador()
print(jugador1)
print(jugador2)
    
