import pygame

from Platforms import Platform, MovingPlatform

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

x_started1 = 150
y_started1 = 680
x_end1 = 1150
y_end1 = 600

platforms_1 = []
elastic_1 = []
disappearing_1 = []
moving_v_1 = []
moving_h_1 = []
death_1 = []

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

platforms_1.append(Platform(screen, RED, 640, 710, 1280, 20))
platforms_1.append(Platform(screen, RED, 640, 10, 1280, 20))
platforms_1.append(Platform(screen, RED, 10, 360, 20, 720))
platforms_1.append(Platform(screen, RED, 1270, 360, 20, 720))

platforms_1.append(Platform(screen, RED, 300, 450, 30, 560))
platforms_1.append(Platform(screen, RED, 100, 435, 200, 30))

platforms_1.append(Platform(screen, RED, 200, 570, 200, 30))
platforms_1.append(Platform(screen, RED, 700, 250, 30, 500))
platforms_1.append(Platform(screen, RED, 400, 250, 200, 30))
platforms_1.append(Platform(screen, RED, 540, 650, 30, 100))
platforms_1.append(Platform(screen, RED, 540, 515, 100, 30))
platforms_1.append(Platform(screen, RED, 1000, 470, 30, 500))
platforms_1.append(Platform(screen, RED, 1200, 400, 150, 30))


elastic_1.append(Platform(screen, GREEN, 750, 515, 150, 30))
elastic_1.append(Platform(screen, GREEN, 425, 685, 150, 30))
elastic_1.append(Platform(screen, GREEN, 655, 685, 150, 30))
elastic_1.append(Platform(screen, GREEN, 840, 685, 150, 30))
elastic_1.append(Platform(screen, GREEN, 1000, 70, 150, 30))

moving_v_1.append(MovingPlatform(screen, CYAN, 150, 250, 100, 30, y_up=200, y_down=350))
moving_v_1.append(MovingPlatform(screen, CYAN, 750, 300, 30, 100, y_up=100, y_down=400))

moving_h_1.append(MovingPlatform(screen, CYAN, 200, 100, 100, 30, x_left=150, x_right=500))


death_1.append(Platform(screen, BLACK, 300, 50, 560, 30))
death_1.append(Platform(screen, BLACK, 935, 335, 100, 30))
death_1.append(Platform(screen, BLACK, 1030, 550, 30, 100))
