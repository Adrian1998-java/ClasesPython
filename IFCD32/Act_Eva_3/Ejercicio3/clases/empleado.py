

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"
    
    def salario_mensual(self):
        return self.salario
    
    
class Administrativo(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        
    def __str__(self):
        return f"Administrativo: {self.nombre}, Salario: {self.salario}"
    def salario_mensual(self):
        return self.salario * 12
    
class Tecnico(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        
    def __str__(self):
        return f"Técnico: {self.nombre}, Salario: {self.salario}"
    
    def salario_mensual(self):
        return (self.salario * 12) + (self.salario * 12) * 0.2







