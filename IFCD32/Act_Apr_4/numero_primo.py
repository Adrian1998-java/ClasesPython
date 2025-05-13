from modulos.operaciones import lista_primos
'''Crea una función que genere una lista de números primos en un rango específico.
'''

n = int(input("Introduce el inicio del rango: "))
m = int(input("Introduce el fin del rango: "))

primos = lista_primos(n, m)
print(f"Los números primos entre {n} y {m} son: {primos}")