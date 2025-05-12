# Opereciones matemáticas básicas
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

# Cuenta los números pares dentro de un rango
def num_pares(n = 0, y = 0):
    lista = []
    for i in range(n, y + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista

# Cuenta todas las letras 'a' en una cadena
def contar_a(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() == 'a':
            contador += 1
    return contador

# Cuenta todas las vocales dentro de una cadena
def cuenta_vocales(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() in 'aeiou':
            contador += 1
    return contador