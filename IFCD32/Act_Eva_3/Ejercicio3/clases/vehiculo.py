# Clase Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def mostrar_marca(self):
        return self.marca
    def definir_marca(self, marca):
        self.marca = marca
    def mostrar_modelo(self):
        return self.modelo
    def definir_modelo(self, modelo):
        self.modelo = modelo
    def mostrar_cilindrada(self):
        return self.cilindrada
    def definir_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada
        
class automovil(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, conbustible):
        super().__init__(marca, modelo, cilindrada)
        self.combvustible = conbustible

    def mostrar_combustible(self):
        return self.combvustible
    def definir_combustible(self, combustible):
        self.combvustible = combustible
        






