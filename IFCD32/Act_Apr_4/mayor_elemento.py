'''Define una función llamada mayor_elemento que tome un parámetro lista y devuelva el elemento más grande de la lista.
'''
def mayor_elemento(lista):
    '''Define una función llamada mayor_elemento que tome un parámetro lista y devuelva el elemento más grande de la lista.'''
    if not lista:
        return None
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor

if __name__ == "__main__":
    lista = [3, 5, 7, 2, 8, 6]
    resultado = mayor_elemento(lista)
    print(f"El elemento más grande de la lista {lista} es: {resultado}")