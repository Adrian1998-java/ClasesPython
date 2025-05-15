

# Promedio de una lista. Escribe un programa que calcule el promedio de una lista (los valores de la lista los has de escoger tú) de números.

tamanio = int(input("¿Cuántos números deseas ingresar? "))
numeros = []
for i in range(tamanio):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
promedio = sum(numeros) / tamanio
print(f"El promedio de la lista es: {promedio}")

# Tuplas como coordenadas. Crea un programa que lea las coordenadas (x, y) de varios puntos y los almacene en una lista de tuplas. Luego, muestra el contenido de la lista.

tamanio = int(input("¿Cuántos puntos deseas ingresar? "))
puntos = []
for i in range(tamanio):
    x = float(input(f"Ingrese la coordenada x del punto {i + 1}: "))
    y = float(input(f"Ingrese la coordenada y del punto {i + 1}: "))
    puntos.append((x, y))
# Convertimos de lista a tupla
puntos_tupla = tuple(puntos)
print(f"Tupla de puntos: {puntos_tupla}")


# Diccionario de estudiantes. Crea un programa que permita ingresar el nombre y la edad de varios estudiantes, y luego muestra un diccionario donde las claves son los nombres y los valores son las edades.

tamanio = int(input("¿Cuántos estudiantes deseas ingresar? "))
estudiantes = {}
for i in range(tamanio):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    estudiantes[nombre] = edad

print("Diccionario de estudiantes:")
for nombre, edad in estudiantes.items():
    print(f"{nombre}: {edad} años")


# Acceder a elementos de un array. Escribe un programa que declare un array de 5 elementos y muestra el valor del tercer elemento.

tamanio = 5
numeros = []
for i in range(tamanio):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
print(f"El tercer elemento del array es: {numeros[2]}")

# Ordenar una lista de manera ascendente. Desarrolla un programa que ordene una lista de números de forma ascendente y muestre el resultado.

tamanio = int(input("¿Cuántos números deseas ingresar? "))
numeros = []
for i in range(tamanio):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
numeros.sort()
print("Lista ordenada de manera ascendente:")
print(numeros)



