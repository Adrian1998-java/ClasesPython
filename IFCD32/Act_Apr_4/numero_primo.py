'''Crea una función que genere una lista de números primos en un rango específico.
'''

n = int(input("Introduce el inicio del rango: "))
m = int(input("Introduce el fin del rango: "))
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

primos = lista_primos(n, m)
print(f"Los números primos entre {n} y {m} son: {primos}")