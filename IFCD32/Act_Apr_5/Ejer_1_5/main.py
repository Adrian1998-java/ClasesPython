# Crea una clase llamada CuentaBancaria que represente una cuenta bancaria con un saldo y métodos para depositar y retirar dinero. La clase debe tener un método para imprimir el saldo actual.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a retirar debe ser mayor que cero y menor o igual al saldo actual.")

    def imprimir_saldo(self):
        print(f"Saldo actual: {self.saldo}")

