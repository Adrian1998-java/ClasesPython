'''Crea una función que genere la tabla de multiplicar de un número hasta un límite especificado.
'''

def tabla_multiplicar(numero, limite):
    '''Crea una función que genere la tabla de multiplicar de un número hasta un límite especificado.'''
    tabla = []
    for i in range(1, limite + 1):
        resultado = numero * i
        tabla.append(f"{numero} x {i} = {resultado}")
    return tabla

numero = int(input("Introduce el número del que deseas generar la tabla de multiplicar: "))
limite = int(input("Introduce el límite hasta el cual deseas generar la tabla: "))

tabla = tabla_multiplicar(numero, limite)
print(f"Tabla de multiplicar del {numero} hasta el {limite}:")

for linea in tabla:
    print(linea)