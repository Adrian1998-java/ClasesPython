'''Define una función llamada cuenta_vocales que tome un parámetro palabra y devuelva el número de vocales que contiene.
La función debe considerar las vocales en mayúsculas y minúsculas.'''
def cuenta_vocales(palabra):
    '''Define una función llamada cuenta_vocales que tome un parámetro palabra y devuelva el número de vocales que contiene.
    La función debe considerar las vocales en mayúsculas y minúsculas.'''
    contador = 0
    for letra in palabra:
        if letra.lower() in 'aeiou':
            contador += 1
    return contador

if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    resultado = cuenta_vocales(palabra)
    print(f"La palabra '{palabra}' contiene {resultado} vocales.")