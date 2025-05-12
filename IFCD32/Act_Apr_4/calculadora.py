from modulos.operaciones import suma, resta, multiplicacion, division

'''Crea una calculadora que realice operaciones básicas (suma, resta, multiplicación y división) a partir de dos números ingresados por el usuario.'''
n = 99
while(n != 0):
    print("Elige una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    n = int(input())
    if(n == 0):
        print("Saliendo de la calculadora.")
        break
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    
    if(n == 1):
        print(f"La suma de {a} y {b} es: {suma(a, b)}")
    elif(n == 2):
        print(f"La resta de {a} y {b} es: {resta(a, b)}")
    elif(n == 3):
        print(f"La multiplicación de {a} y {b} es: {multiplicacion(a, b)}")
    elif(n == 4):
        try:
            print(f"La división de {a} y {b} es: {division(a, b)}")
        except ValueError as e:
            print(e)
