from modulos.operaciones import	suma_pares
'''Define una función llamada suma_pares que tome un parámetro n y devuelva la suma de todos los números pares menores o iguales a n.
'''

n = int(input("Introduce un número: "))
resultado = suma_pares(n)
print(f"La suma de los números pares menores o iguales a {n} es: {resultado}")