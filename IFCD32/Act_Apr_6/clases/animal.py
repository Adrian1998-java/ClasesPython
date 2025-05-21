
class Animal:    
    def __init__(self, name):
        self.name = name
        
    def obtener_nombre(self):
        return self.name

    def hacer_sonido(self):
        print(f"{self.name} makes a sound.")
        
    def moverse(self):
        print(f"{self.name} se mueve.")
        
    def interacturar_con_animal(self):
        self.moverse()
        self.hacer_sonido()
        
class Perro(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def hacer_sonido(self):
        print(f"{self.name} ladra.")
        
    def moverse(self):
        print(f"{self.name} corre.")
        
class Gato(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def hacer_sonido(self):
        print(f"{self.name} maulla.")
        
    def moverse(self):
        print(f"{self.name} salta.")

class Vaca(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def hacer_sonido(self):
        print(f"{self.name} muge.")
    
    def moverse(self):
        print(f"{self.name} camina lentamente.")
        
class Pajaro(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def hacer_sonido(self):
        print(f"{self.name} canta.")
    
    def moverse(self):
        print(f"{self.name} vuela.")