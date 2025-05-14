# Crea una clase llamada Rectángulo que represente un rectángulo con un ancho y una altura. La clase debe tener métodos para calcular el área y el perímetro del rectángulo. Se debe validar que se trata de un rectángulo.

class Rectangulo:
    def __init__(self, ancho=1, alto=1):
        self.ancho = ancho
        self.alto = alto

    def establecer_dimensiones(self, ancho, alto):
        if ancho <= 0 or alto <= 0:
            raise ValueError("Las dimensiones deben ser mayores que cero.")
        self.ancho = ancho
        self.alto = alto

    def obtener_dimensiones(self):
        return (self.ancho, self.alto)

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)