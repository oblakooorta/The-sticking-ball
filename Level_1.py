import pygame
from random import choice
import math

from Platforms import Platform

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
WHITE  = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

WIDTH = 1280
HEIGHT = 720

x_started = 150
y_started = 670
x_end = 1150
y_end = 600

"""
Это обычные платформы
"""
platforms = []
"""
Это упругие платформы
"""
elastic = []
"""
Это исчезающие платформы
"""
disappearing = []

"""
Это движущиеся вертикально платформы
"""

moving_v = []

"""
Это двигающиеся горизонтально платформы
"""
moving_h = []


"""
Это платформы смерти
"""

death = []

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""
Границы
"""
platforms.append(Platform(screen, color = RED, x = 640, y = 710, w = 1280, l = 20, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 640, y = 10, w = 1280, l = 20, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 10, y = 360, w = 20, l = 720, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 1270, y = 360, w = 20, l = 720, x_left = 0, x_right = 0, y_up = 0, y_down = 0))

platforms.append(Platform(screen, color = RED, x = 300, y = 450, w = 30, l = 560, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 100, y = 435, w = 200, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))

platforms.append(Platform(screen, color = RED, x = 200, y = 570, w = 200, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 700, y = 250, w = 30, l = 500, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 400, y = 250, w = 200, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 540, y = 650, w = 30, l = 100, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 540, y = 515, w = 100, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 1000, y = 470, w = 30, l = 500, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
platforms.append(Platform(screen, color = RED, x = 1200, y = 400, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))


elastic.append(Platform(screen, color = GREEN, x = 750, y = 515, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
elastic.append(Platform(screen, color = GREEN, x = 425, y = 685, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
elastic.append(Platform(screen, color = GREEN, x = 655, y = 685, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
elastic.append(Platform(screen, color = GREEN, x = 840, y = 685, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
elastic.append(Platform(screen, color = GREEN, x = 1000, y = 70, w = 150, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))


moving_v.append(Platform(screen, color = CYAN, x = 150, y = 250, w = 100, l = 30, x_left = 0, x_right = 0, y_up = 200, y_down = 350))
moving_v.append(Platform(screen, color = CYAN, x = 750, y = 300, w = 30, l = 100, x_left = 0, x_right = 0, y_up = 100, y_down = 400))


moving_h.append(Platform(screen, color = CYAN, x = 200, y = 100, w = 100, l = 30, x_left = 150, x_right = 500, y_up = 0, y_down = 0))


death.append(Platform(screen, color = BLACK, x = 300, y = 50, w = 560, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
death.append(Platform(screen, color = BLACK, x = 550, y = 485, w = 270, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
death.append(Platform(screen, color = BLACK, x = 935, y = 335, w = 100, l = 30, x_left = 0, x_right = 0, y_up = 0, y_down = 0))
death.append(Platform(screen, color = BLACK, x = 1030, y = 550, w = 30, l = 100, x_left = 0, x_right = 0, y_up = 0, y_down = 0))


