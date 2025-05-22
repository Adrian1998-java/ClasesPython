

'''class Animal:
    def hacer_sonido(self):
        pass

    def moverse(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"

    def moverse(self):
        return "Corriendo como un perro"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau miau!"

    def moverse(self):
        return "Saltando como un gato"

class Ave(Animal):
    def hacer_sonido(self):
        return "¡Cucurucú!"

    def moverse(self):
        return "Volando como un ave"

def interactuar_con_animal(animal):
    sonido = animal.hacer_sonido()
    movimiento = animal.moverse()
    print(f"Sonido: {sonido}")
    print(f"Movimiento: {movimiento}")

# Ejemplo de uso
perro1 = Perro()
gato1 = Gato()
ave1 = Ave()

interactuar_con_animal(perro1)
# Sonido: ¡Guau guau!
# Movimiento: Corriendo como un perro

interactuar_con_animal(gato1)
# Sonido: ¡Miau miau!
# Movimiento: Saltando como un gato

interactuar_con_animal(ave1)
# Sonido: ¡Cucurucú!
# Movimiento: Volando como un ave
'''

'''El código presenta una jeraquía de clases, donde 3 de ellas heredan de una clase base llamada Animal, remplezando
el contenido de los métodos hacer_sonido y moverse.
Además, se define una función llamada interactuar_con_animal que toma un objeto de Tipo Animal como argumento y
muestra por pantalla el sonido y el movimiento del animal.

Luego, se crean instancias de las clases Perro, Gato y Ave, y se llama a la función interactuar_con_animal
con cada una de ellas, mostrando el sonido y movimiento correspondiente.
'''

