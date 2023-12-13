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

platforms = []
elastic = []
disappearing = []
moving_v = []
moving_h = []
death = []

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

platforms.append(Platform(screen, RED, 640, 710, 1280, 20))
platforms.append(Platform(screen, RED, 640, 10, 1280, 20))
platforms.append(Platform(screen, RED, 10, 360, 20, 720))
platforms.append(Platform(screen, RED, 1270, 360, 20, 720))

platforms.append(Platform(screen, RED, 50, 700, 200, 100))
platforms.append(Platform(screen, RED, 600, 500, 20, 440))
platforms.append(Platform(screen, RED, 600, 100, 20, 200))
platforms.append(Platform(screen, RED, 200, 420, 550, 20))
platforms.append(Platform(screen, RED, 1100, 650, 200, 20))
platforms.append(Platform(screen, RED, 1200, 560, 20, 200))
platforms.append(Platform(screen, RED, 1000, 200, 20, 400))

disappearing.append(Platform(screen, BLUE, 230, 660, 80, 20))
disappearing.append(Platform(screen, BLUE, 330, 660, 80, 20))
disappearing.append(Platform(screen, BLUE, 430, 660, 80, 20))
disappearing.append(Platform(screen, BLUE, 530, 660, 80, 20))
disappearing.append(Platform(screen, BLUE, 533, 425, 115, 30))

death.append(Platform(screen, BLACK, 247.5, 435, 456, 10))
death.append(Platform(screen, BLACK, 370, 690, 440, 20))
death.append(Platform(screen, BLACK, 305, 30, 570, 20))
death.append(Platform(screen, BLACK, 30, 225, 20, 370))
death.append(Platform(screen, BLACK, 935, 690, 650, 20))
death.append(Platform(screen, BLACK, 1250, 360, 20, 680))
death.append(Platform(screen, BLACK, 1020, 210, 20, 380))

elastic.append(Platform(screen, GREEN, 900, 280, 40, 100))
