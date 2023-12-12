import pygame
from random import choice
import math

from Platforms import Platform

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

WIDTH = 1280
HEIGHT = 720
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
platforms.append(Platform(screen, color=RED, x=640, y=710, w=1280, l=20))
platforms.append(Platform(screen, color=RED, x=640, y=10, w=1280, l=20))
platforms.append(Platform(screen, color=RED, x=10, y=360, w=20, l=720))
platforms.append(Platform(screen, color=RED, x=1270, y=360, w=20, l=720))

platforms.append(Platform(screen, color=RED, x=50, y=700, w=200, l=100))
platforms.append(Platform(screen, color=RED, x=600, y=500, w=20, l=440))
platforms.append(Platform(screen, color=RED, x=600, y=100, w=20, l=200))
platforms.append(Platform(screen, color=RED, x=200, y=420, w=550, l=20))
platforms.append(Platform(screen, color=RED, x=1100, y=650, w=200, l=20))
platforms.append(Platform(screen, color=RED, x=1200, y=560, w=20, l=200))
platforms.append(Platform(screen, color=RED, x=1000, y=200, w=20, l=400))

disappearing.append(Platform(screen, color=BLUE, x=230, y=660, w=80, l=20))
disappearing.append(Platform(screen, color=BLUE, x=330, y=660, w=80, l=20))
disappearing.append(Platform(screen, color=BLUE, x=430, y=660, w=80, l=20))
disappearing.append(Platform(screen, color=BLUE, x=530, y=660, w=80, l=20))
disappearing.append(Platform(screen, color=BLUE, x=533, y=425, w=115, l=30))

death.append(Platform(screen, color=BLACK, x=247.5, y=435, w=456, l=10))
death.append(Platform(screen, color=BLACK, x=370, y=690, w=440, l=20))
death.append(Platform(screen, color=BLACK, x=305, y=30, w=570, l=20))
death.append(Platform(screen, color=BLACK, x=30, y=225, w=20, l=370))
death.append(Platform(screen, color=BLACK, x=935, y=690, w=650, l=20))
death.append(Platform(screen, color=BLACK, x=1250, y=360, w=20, l=680))
death.append(Platform(screen, color=BLACK, x=1020, y=210, w=20, l=380))

elastic.append(Platform(screen, color=GREEN, x=900, y=280, w=40, l=100))

