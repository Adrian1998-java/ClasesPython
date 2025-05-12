def contar_a(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() == 'a':
            contador += 1
    return contador