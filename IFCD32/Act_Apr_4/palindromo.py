'''Crea una función que verifique si una palabra es un palíndromo (se lee igual de izquierda a derecha y viceversa).
'''

cadena = input("Introduce una palabra: ")
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return cadena == cadena[::-1]  # Comparar la cadena con su reverso

if es_palindromo(cadena):
    print(f"La palabra '{cadena}' es un palíndromo.")
else:
    print(f"La palabra '{cadena}' no es un palíndromo.")