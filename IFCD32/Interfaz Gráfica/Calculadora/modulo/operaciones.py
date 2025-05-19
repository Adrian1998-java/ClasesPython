# Operaciones aritméticas para la calculadora

def suma(a=0,b=0):
    return a + b

def resta(a=0,b=0):
    return a - b

def multiplicacion(a=0,b=0):
    return a * b

def division(a=0,b=1):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b



