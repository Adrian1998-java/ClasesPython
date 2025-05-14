#Crea una clase llamada Punto que represente un punto en un plano cartesiano con coordenadas x e y. La clase debe tener métodos para establecer las coordenadas, obtener las coordenadas y calcular la distancia entre dos puntos.

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def establecer_coordenadas(self, x, y):
        self.x = x
        self.y = y

    def obtener_coordenadas(self):
        return (self.x, self.y)

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)