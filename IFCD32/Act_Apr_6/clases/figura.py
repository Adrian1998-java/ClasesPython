
class Figura:
    def __init__(self, area):
        self.area = area

    def calcular_area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        super().__init__(self.calcular_area())

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(self.calcular_area())

    def calcular_area(self):
        return self.base * self.altura


