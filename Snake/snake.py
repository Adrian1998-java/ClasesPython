import pygame
import time
import random

# Inicialización de pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho = 800
alto = 600

# Configurar la pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake Game en Python')

# Reloj
reloj = pygame.time.Clock()
velocidad = 15

# Tamaño de la serpiente
tamano_bloque = 20

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)
fuente_puntuacion = pygame.font.SysFont("comicsansms", 35)


def puntuacion(puntos):
    valor = fuente_puntuacion.render("Puntos: " + str(puntos), True, blanco)
    pantalla.blit(valor, [0, 0])


def nuestra_serpiente(tamano_bloque, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamano_bloque, tamano_bloque])


def mensaje(msg, color):
    texto = fuente.render(msg, True, color)
    pantalla.blit(texto, [ancho / 6, alto / 3])


def juego():
    game_over = False
    game_cerrado = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0

    while not game_over:

        while game_cerrado:
            pantalla.fill(negro)
            mensaje("Has perdido. Presiona Q para salir o C para continuar", rojo)
            puntuacion(largo_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamano_bloque
                    x1_cambio = 0

        # Verifica los bordes
        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_cerrado = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tamano_bloque, tamano_bloque])

        cabeza = []
        cabeza.append(x1)
        cabeza.append(y1)
        lista_serpiente.append(cabeza)
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza:
                game_cerrado = True

        nuestra_serpiente(tamano_bloque, lista_serpiente)
        puntuacion(largo_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0
            largo_serpiente += 2

        reloj.tick(velocidad)

    pygame.quit()
    quit()


# Ejecutar el juego
juego()
