from modulos.operaciones import cuenta_vocales
'''Define una función llamada cuenta_vocales que tome un parámetro palabra y devuelva el número de vocales que contiene.
La función debe considerar las vocales en mayúsculas y minúsculas.'''

palabra = input("Introduce una palabra: ")
resultado = cuenta_vocales(palabra)
print(f"La palabra '{palabra}' contiene {resultado} vocales.")