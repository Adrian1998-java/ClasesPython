'''Crea una función que genere los primeros n términos de la secuencia Fibonacci.
'''

def fibonacci(n):
    '''Crea una función que genere los primeros n términos de la secuencia Fibonacci.'''
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

n = int(input("Introduce el número de términos de la secuencia Fibonacci que deseas generar: "))
fibonacci_sequence = fibonacci(n)
print(f"Los primeros {n} términos de la secuencia Fibonacci son: {fibonacci_sequence}")