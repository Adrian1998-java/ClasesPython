'''Define una función llamada suma_pares que tome un parámetro n y devuelva la suma de todos los números pares menores o iguales a n.
'''

def suma_pares(n):
    '''Define una función llamada suma_pares que tome un parámetro n y devuelva la suma de todos los números pares menores o iguales a n.'''
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma

if __name__ == "__main__":
    n = int(input("Introduce un número: "))
    resultado = suma_pares(n)
    print(f"La suma de los números pares menores o iguales a {n} es: {resultado}")