
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def obtener_marca(self):
        return self.marca
    def obtener_modelo(self):
        return self.modelo
    def obtener_anio(self):
        return self.anio
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, transmision):
        super().__init__(marca, modelo, anio)
        self.transmision = transmision






