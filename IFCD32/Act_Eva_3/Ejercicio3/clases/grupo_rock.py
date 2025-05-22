

class GrupoRock:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def tocar_intrumento(self):
        return f"{self.nombre} está tocando su instrumento."
    
class Cantante(GrupoRock):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def tocar_intrumento(self):
        return f"{self.nombre} está cantando."
    
class Guitarrista(GrupoRock):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def tocar_intrumento(self):
        return f"{self.nombre} está tocando la guitarra."
    
class Bateria(GrupoRock):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def tocar_intrumento(self):
        return f"{self.nombre} está tocando la batería."







