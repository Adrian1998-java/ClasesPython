from modulos import contar_a

'''Crea una función que cuente la cantidad de letras "a" en una cadena de texto.'''

cadena = input("Introduce una cadena de texto: ")

cantidad_a = contar_a.contar_a(cadena)
print(f"La cantidad de letras 'a' en la cadena es: {cantidad_a}")