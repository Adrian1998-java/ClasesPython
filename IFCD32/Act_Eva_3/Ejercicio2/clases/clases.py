# Clase Persona
from pyclbr import Class


class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def mostrar_nombre(self):
        return self.nombre
    def obtener_nombre(self):
        return self.nombre
    
    def mostrar_edad(self):
        return self.edad
    def obtener_edad(self):
        return self.edad
    
    def mostrar_profesion(self):
        return self.profesion
    def obtener_profesion(self):
        return self.profesion
    
# Clase Perro
class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    def mostrar_nombre(self):
        return self.nombre
    def obtener_nombre(self):
        return self.nombre
    
    def mostrar_raza(self):
        return self.raza
    def obtener_raza(self):
        return self.raza
    
    def mostrar_edad(self):
        return self.edad
    def obtener_edad(self):
        return self.edad
    
    def ladrar(self):
        return print(f"{self.nombre} está ladrando ¡Guau Guau!")    
    
# Clase Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, cuenta, saldo, titular):
        self.cuenta = cuenta
        self.saldo = saldo
        self.titular = titular
    
    def mostrar_cuenta(self):
        return self.cuenta
    def obtener_cuenta(self):
        return self.cuenta
    def mostrar_saldo(self):
        return self.saldo
    def obtener_saldo(self):
        return self.saldo
    def mostrar_titular(self):
        return self.titular
    def obtener_titular(self):
        return self.titular
    
    def realizar_deposito(self, cantidad):
        self.saldo += cantidad
        return f"Se ha depositado {cantidad} a la cuenta {self.cuenta}. Nuevo saldo: {self.saldo}"
    
    def realizar_retiro(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes"
        else:
            self.saldo -= cantidad
            return f"Se ha retirado {cantidad} de la cuenta {self.cuenta}. Nuevo saldo: {self.saldo}"
    
# Clase Hotel
class Hotel:
    def __init__(self, nombre, cap_habitaciones, habitaciones_ocupadas):
        self.nombre = nombre
        self.capacidad = cap_habitaciones
        self.habitaciones_ocupadas = habitaciones_ocupadas
        
    def info_hotel(self):
        return f"Nombre: {self.nombre}, Capacidad: {self.capacidad}, Habitaciones ocupadas: {self.habitaciones_ocupadas}"
    
    def hab_reservadas(self):
        return self.habitaciones_ocupadas
    
    def hab_disponibles(self):
        return self.capacidad - self.habitaciones_ocupadas
    
# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, lista_materias):
        self.nombre = nombre
        self.edad = edad
        self.lista_materias = lista_materias
        
    def info_estudiante(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Materias: {', '.join(self.lista_materias)}"
    
    def agregar_materia(self, materia):
        self.lista_materias.append(materia)
        return f"Materia {materia} agregada a la lista de materias de {self.nombre}"
    
    def listar_materias(self):
        return f"Materias de {self.nombre}: {', '.join(self.lista_materias)}"
    
    
    
    
    