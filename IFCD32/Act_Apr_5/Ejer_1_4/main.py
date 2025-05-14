# Crea una clase llamada Coche que represente un coche con marca, modelo y año. La clase debe tener métodos para obtener y establecer la marca, el modelo y el año del coche, así como un método para imprimir la información del coche.
class Coche:
    def __init__(self, marca="", modelo="", año=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_marca(self):
        return self.marca

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_modelo(self):
        return self.modelo

    def establecer_año(self, año):
        if año < 1886:  # El primer coche fue inventado en 1886
            raise ValueError("El año no puede ser anterior a 1886.")
        self.año = año

    def obtener_año(self):
        return self.año

    def imprimir_informacion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"