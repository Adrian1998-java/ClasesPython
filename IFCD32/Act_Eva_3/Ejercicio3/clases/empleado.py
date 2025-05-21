

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"
    
    def salario_mensual(self):
        return self.salario
    
    







