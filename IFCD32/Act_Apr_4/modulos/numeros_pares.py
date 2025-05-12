def num_pares(n = 0, y = 0):
    '''Crea una función que genere una lista de números pares en un rango específico.
    La función debe recibir dos parámetros: el inicio y el fin del rango.
    La función debe devolver una lista con los números pares en ese rango.'''
    lista = []
    for i in range(n, y + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista