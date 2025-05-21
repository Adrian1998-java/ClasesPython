
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_salario_mensual(self):
        return self.salario
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, bonificacion):
        super().__init__(nombre, salario)
        self.bonificacion = bonificacion
    
    def calcular_salario_mensual(self):
        return self.salario + self.bonificacion
    
class Programador(Empleado):
    def __init__(self, nombre, salario, horas_extra):
        super().__init__(nombre, salario)
        self.horas_extra = horas_extra
    
    def calcular_salario_mensual(self):
        return self.salario + (self.horas_extra * 20)  # Suponiendo que cada hora extra se paga a 20 unidades monetarias

