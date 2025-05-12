def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

# def factorial():
#     n = int(input("Ingrese un número entero positivo: "))
#     if n < 0:
#         print("El factorial no está definido para números negativos.")
#         return
#     resultado = 1
#     for i in range(1, n + 1):
#         resultado *= i
#     print(f"El factorial de {n} es {resultado}")

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)