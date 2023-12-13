import pygame

from Platforms import Platform

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
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
platforms.append(Platform(screen, RED, 640, 710, 1280, 20))
platforms.append(Platform(screen, RED, 640, 10, 1280, 20))
platforms.append(Platform(screen, RED, 10, 360, 20, 720))
platforms.append(Platform(screen, RED, 1270, 360, 20, 720))

platforms.append(Platform(screen, RED, 300, 450, 30, 560))
platforms.append(Platform(screen, RED, 100, 435, 200, 30))

platforms.append(Platform(screen, RED, 200, 570, 200, 30))
platforms.append(Platform(screen, RED, 700, 250, 30, 500))
platforms.append(Platform(screen, RED, 400, 250, 200, 30))
platforms.append(Platform(screen, RED, 540, 650, 30, 100))
platforms.append(Platform(screen, RED, 540, 515, 100, 30))
platforms.append(Platform(screen, RED, 1000, 470, 30, 500))
platforms.append(Platform(screen, RED, 1200, 400, 150, 30))


elastic.append(Platform(screen, GREEN, 750, 515, 150, 30))
elastic.append(Platform(screen, GREEN, 425, 685, 150, 30))
elastic.append(Platform(screen, GREEN, 655, 685, 150, 30))
elastic.append(Platform(screen, GREEN, 840, 685, 150, 30))
elastic.append(Platform(screen, GREEN, 1000, 70, 150, 30))


moving_v.append(Platform(screen, CYAN, 150, 250, 100, 30, y_up=200, y_down=350))
moving_v.append(Platform(screen, CYAN, 750, 300, 30, 100, y_up=100, y_down=400))


moving_h.append(Platform(screen, CYAN, 200, 100, 100, 30, x_left=150, x_right=500))


death.append(Platform(screen, BLACK, 300, 50, 560, 30))
death.append(Platform(screen, BLACK, 550, 485, 270, 30))
death.append(Platform(screen, BLACK, 935, 335, 100, 30))
death.append(Platform(screen, BLACK, 1030, 550, 30, 100))
