
import pygame
import math
import sys
from vector import Vector

class Graficador:

    def __init__(self, width = 480, height = 320):

        #Inicializa el graficador recibiéndo como parámetros el tamaño
        #de la pantalla.

        pygame.init()

        self.width = width
        self.height = height
        self.screen_size = Vector(width, height)
        self.screen = pygame.display.set_mode(self.screen_size.toIntegerPair())

        # Definimos constantes
        self.background_color = 0, 0, 0

        self.node_color = 135, 6, 241
        self.node_border_color = 55, 2, 105
        self.node_border_thickness = 2
        self.node_radius = 5

        self.edge_color = 216, 4, 30
        self.edge_thickness = 2

    def _dibujar_texto(self, texto, where):
        #Dibuja texto por pantalla, en la posición especificada
        texto = str(texto)
        font = pygame.font.SysFont('Comic Sans MS', 15)
        texto = font.render(texto, True, (255, 255, 255))
        self.screen.blit(texto, where.toIntegerPair())

    def _dibujar_nodo(self, pos):
        #Dibuja un nodo en la pantalla, en la posición indicada
        pos = pos.toIntegerPair()
        pygame.draw.circle(self.screen, self.node_color,
            pos, self.node_radius)
        pygame.draw.circle(self.screen, self.node_border_color,
            pos, self.node_radius, self.node_border_thickness)

    def _dibujar_arista(self, a, b):
        #Dibuja una arista, desde y hasta las posiciones indicadas
        pygame.draw.line(self.screen, self.edge_color,
            a.toIntegerPair(), b.toIntegerPair(), self.edge_thickness)



    def dibujar_grafo(self, grafo, posiciones):

        #Recibe la descripción de un grafo, junto con un diccionario
        #con la posición de cada nodo (expresado como un vector) y
        #dibuja el grafo en pantalla.

        nodes = grafo[0]
        edges = grafo[1]
        self.screen.fill(self.background_color)

        for edge in edges:
            a = posiciones[edge[0]] * self.screen_size
            b = posiciones[edge[1]] * self.screen_size
            self._dibujar_arista(a, b)

        for node in nodes:
            shift = Vector(self.node_radius, self.node_radius)
            self._dibujar_texto(node, self.screen_size * posiciones[node] + shift)

            where = posiciones[node] * self.screen_size
            self._dibujar_nodo(where)

        pygame.display.flip()

    def permitir_cerrado(self):
        #Comienza a escuchar la acción del usuario de cerrar el programa
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
