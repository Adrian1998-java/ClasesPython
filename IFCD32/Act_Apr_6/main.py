from clases.vehiculo import Automovil
from clases.animal import Perro, Gato, Vaca, Pajaro
from clases.figura import Circulo, Rectangulo 
from clases.musica import Guitarra, Piano

# Primero probamos con un vehiculo y clases relacionadas con el mismo
Automovil1 = Automovil("Toyota", "Corolla", 2020, "Automatica")
# Inprimimos los datos por pantallla del vehiculo creado
print(Automovil1.obtener_marca())
print(Automovil1.obtener_modelo())
print(Automovil1.obtener_anio())
print(Automovil1.transmision)

# Segundo, ahora probamos con animales
Perro1 = Perro("Firulais")
Gato1 = Gato("Mauricio")
Vaca1 = Vaca("Lola")
# Mostarmos por pantalla el sonido que hace cada animal
print("Este animal se llama:", Perro1.obtener_nombre())
Perro1.hacer_sonido()
print("Este animal se llama:", Gato1.obtener_nombre())
Gato1.hacer_sonido()
print("Este animal se llama:", Vaca1.obtener_nombre())
Vaca1.hacer_sonido()


# Tercero, probramos con figuras
Circulo1 = Circulo(5)
Rectangulo1 = Rectangulo(4, 6)

# Mostramos por pantalla el area de cada figura
print("El area del circulo es:", Circulo1.calcular_area())
print("El area del rectangulo es:", Rectangulo1.calcular_area())

#Cuarto, intrumentos de musica
Guitarra1 = Guitarra("Guitarra Acustica")
Piano1 = Piano("Piano de Cola")
# Mostramos por pantalla el sonido que hace cada instrumento
print("El instrumento es:", Guitarra1.nombre)
Guitarra1.tocar()
print("El instrumento es:", Piano1.nombre)
Piano1.tocar()

# Quinto, probamos otra vez con animales
ave1 = Pajaro("Loro")
# Hacemos que interactuen los animales
Perro1.interacturar_con_animal()
Gato1.interacturar_con_animal()
Vaca1.interacturar_con_animal()
ave1.interacturar_con_animal()





