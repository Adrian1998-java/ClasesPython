# Crea una clase llamada Persona que represente a una persona con nombre y edad. La clase debe tener métodos para obtener y establecer el nombre y la edad, así como un método para saludar.

class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def establecer_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.edad = edad

    def obtener_edad(self):
        return self.edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."