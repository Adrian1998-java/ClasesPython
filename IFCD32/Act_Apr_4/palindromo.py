from modulos.operaciones import es_palindromo
'''Crea una función que verifique si una palabra es un palíndromo (se lee igual de izquierda a derecha y viceversa).
'''

cadena = input("Introduce una palabra: ")

if es_palindromo(cadena):
    print(f"La palabra '{cadena}' es un palíndromo.")
else:
    print(f"La palabra '{cadena}' no es un palíndromo.")