# Esta clase main está disponible probar los ejercicios de la carpeta Act_Apr_5
# Se probaran los 5 ejercicios de la carpeta Act_Apr_5
# Se importan las clases de los ejercicios

# Ejercicio 1
import Ejer_1_1.main as ejer1
# Ejercicio 2   
import Ejer_1_2.main as ejer2
# Ejercicio 3
import Ejer_1_3.main as ejer3
# Ejercicio 4
import Ejer_1_4.main as ejer4
# Ejercicio 5
import Ejer_1_5.main as ejer5

if __name__ == "__main__":
    
    # Pruebas de Ejercicio 1 
    print("Ejercicio 1")
    punto1 = ejer1.Punto(3, 4)
    punto2 = ejer1.Punto(6, 8)
    print(f"Coordenadas del punto 1: {punto1.obtener_coordenadas()}")
    print(f"Coordenadas del punto 2: {punto2.obtener_coordenadas()}")
    distancia = punto1.calcular_distancia(punto2)
    print(f"Distancia entre los puntos: {distancia}")
    print()
    # Pruebas de Ejercicio 2
    print("Ejercicio 2")
    rectangulo = ejer2.Rectangulo(5, 10)
    print(f"Dimensiones del rectángulo: {rectangulo.obtener_dimensiones()}")
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
    print()
    # Pruebas de Ejercicio 3
    print("Ejercicio 3")
    persona = ejer3.Persona("Juan", 30)
    print(persona.saludar())
    persona.establecer_nombre("Pedro")
    persona.establecer_edad(25)
    print(persona.saludar())
    print()
    # Pruebas de Ejercicio 4
    print("Ejercicio 4")
    coche = ejer4.Coche("Toyota", "Corolla", 2020)
    print(coche.imprimir_informacion())
    coche.establecer_marca("Honda")
    coche.establecer_modelo("Civic")
    coche.establecer_año(2021)
    print(coche.imprimir_informacion())
    print()
    # Pruebas de Ejercicio 5
    print("Ejercicio 5")
    cuenta = ejer5.CuentaBancaria(1000)
    cuenta.imprimir_saldo()
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.imprimir_saldo()
    cuenta.retirar(2000)  # Intento de retirar más de lo que hay en la cuenta
    cuenta.depositar(-100)  # Intento de depositar una cantidad negativa
    cuenta.imprimir_saldo()
    print()
    # Fin de las pruebas
    print("Fin de las pruebas")
    
    
    