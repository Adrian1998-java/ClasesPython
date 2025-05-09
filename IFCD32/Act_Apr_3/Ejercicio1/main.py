from geometria.area import area_circulo, area_cuadrado
from geometria.perimetro import perimetro_cuadrado, perimetro_circulo

from matematicas import factorial

# Medir el area y perimetro de un cuadrado y un circulo
cuadrado = 5
circulo = 3

print("Area y perimetro de un cuadrado:\n", "Area:", area_cuadrado(cuadrado), "Perimetro:", perimetro_cuadrado(cuadrado))
print("Area y perimetro de un circulo:\n", "Area:", area_circulo(circulo), "Perimetro:", perimetro_circulo(circulo))


factorial()
