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

# Muestra la secuencia Fibonacci hasta n términos
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Muestra el mayor elemento de una lista
def mayor_elemento(lista):
    if not lista:
        return None
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor

# Dos funciones: Identifica si un número es primo y genera una lista de números primos detro de un rango dado por el usuario
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def lista_primos(n, m):
    '''Crea una función que genere una lista de números primos en un rango específico.'''
    lista = []
    for i in range(n, m + 1):
        if es_primo(i):
            lista.append(i)
    return lista

# Define si una cadena es un palíndromo
# (se lee igual de izquierda a derecha y viceversa).
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return cadena == cadena[::-1]  # Comparar la cadena con su reverso

# Suma todos los número pares desde 0 hasta n
# (incluido n si es par).
def suma_pares(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma

# Genera una tabla de multiplicar para un número dado, hasta un límite especificado.
# La función devuelve una lista de cadenas que representan la tabla de multiplicar.
def tabla_multiplicar(numero, limite):
    tabla = []
    for i in range(1, limite + 1):
        resultado = numero * i
        tabla.append(f"{numero} x {i} = {resultado}")
    return tabla
