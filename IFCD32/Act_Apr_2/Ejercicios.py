# Ejercicio 1: Averiguar si un número que introducimos es par o impar
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
# Ejercicio 2: Debemos de introducir 3 números y debemos de calcular el máximo de los tres números.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

print("El número máximo es:", max(numero1, numero2, numero3))
    
'''
Ejercicio 3: Se nos pide que introduzcamos la nota de un alumno, admitiendo decimales, y se nos devuelva la calificación en texto obtenida, siguiendo el siguiente esquema:
< 5 Insuficiente
< 6 Suficiente
< 7 Bien
< 9 Notable
< 10 Sobresaliente
'''
    
nota = float(input("Introduce la nota del alumno: "))
if nota >= 0 or nota <= 10:
    if nota < 5:
        calificacion = "Insuficiente"
    elif nota < 6:
        calificacion = "Suficiente"
    elif nota < 7:
        calificacion = "Bien"
    elif nota < 9:
        calificacion = "Notable"
    elif nota <= 10:
        calificacion = "Sobresaliente"
else:
    calificacion = "Nota no válida"

print("La calificación es:", calificacion)


    
# Ejercicio 4: Debemos de introducir un año y decirnos si es un año bisiesto o no

anio = int(input("Introduce un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
    
'''
Ejercicio 5: Explica que hace el siguiente código:

lado1 = float(input("Introduce el primer lado del triángulo: "))
lado2 = float(input("Introduce el segundo lado del triángulo: "))
lado3 = float(input("Introduce el tercer lado del triángulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Es un triángulo válido")
else:
    print("No es un triángulo válido")
'''

# El código verifica si tres lados dados pueden formar un triángulo válido. Para que tres lados formen un triángulo, la suma de las longitudes de dos lados debe ser mayor que la longitud del tercer lado. Si se cumple esta condición, se imprime "Es un triángulo válido", de lo contrario, se imprime "No es un triángulo válido".


