from modulos import numeros_pares

'''Crea una función que genere una lista de números pares en un rango específico.
La función debe recibir dos parámetros: el inicio y el fin del rango.
La función debe devolver una lista con los números pares en ese rango.'''

a = int(input("Introduce el inicio del rango: "))
b = int(input("Introduce el fin del rango: "))
pares = numeros_pares.num_pares(a, b)

print(f"Los números pares entre {a} y {b} son: {pares}")
