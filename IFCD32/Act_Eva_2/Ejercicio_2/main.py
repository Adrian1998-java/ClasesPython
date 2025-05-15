

# Mayor de tres números. Desarrolla un programa que lea tres números y determine cuál es el mayor de ellos.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

lista_numeros = [numero1, numero2, numero3]
mayor = max(lista_numeros)
print(f"El mayor de los tres números es: {mayor}")

# Suma de números pares. Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

suma_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")


# Números primos. Crea un programa que determine si un número ingresado por el usuario es primo o no.

primo = int(input("Introduce un número para verificar si es primo: "))
is_primo = True
if primo < 2:
    is_primo = False
for i in range(2, int(primo**0.5) + 1):
    if primo % i == 0:
        is_primo = False
if is_primo:
    print(f"{primo} es un número primo.")
else:
    print(f"{primo} NO es un número primo.")

# Números positivos y negativos. Escribe un programa que lea una lista de números y determine cuántos son positivos y cuántos son negativos.

cantidad = int(input("¿Cuántos números deseas ingresar? "))
numeros = []
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

positivos = 0
negativos = 0
for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

# Tabla de multiplicar. Desarrolla un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

numero = int(input("Introduce un número para generar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
tabla = []
for i in range(1, 11):
    resultado = numero * i
    tabla.append(f"{numero} x {i} = {resultado}")
print("\n".join(tabla))


