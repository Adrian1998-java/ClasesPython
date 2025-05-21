

class Intrumento_Musical:
    def __init__ (self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        print(f"El {self.nombre} está sonando.")
        
class Guitarra(Intrumento_Musical):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def tocar(self):
        print(f"El {self.nombre} está tocando acordes con las cuerdas.")
        
class Piano(Intrumento_Musical):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def tocar(self):
        print(f"El {self.nombre} está tocando melodías con las teclas.")