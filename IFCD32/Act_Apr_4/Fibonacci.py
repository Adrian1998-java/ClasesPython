from modulos.operaciones import fibonacci
'''Crea una función que genere los primeros n términos de la secuencia Fibonacci.
'''

n = int(input("Introduce el número de términos de la secuencia Fibonacci que deseas generar: "))
fibonacci_sequence = fibonacci(n)
print(f"Los primeros {n} términos de la secuencia Fibonacci son: {fibonacci_sequence}")