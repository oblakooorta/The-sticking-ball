import pygame

import math
from random import choice
import sys
import time

FPS = 30

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

WIDTH = 800
HEIGHT = 600

from Ball import Ball
from Guidance import Guidance
from Platforms import Platform
from Goal import Goal

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
"""
Это обычные платформы.
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

ball = Ball(screen, x=400, y=300)
arrow = Guidance(screen, x=400, y=300, obj=ball)
finish = Goal(screen)
platforms.append(Platform(screen, color=RED))
platforms.append(Platform(screen, color=RED, x=400, y=500, w=150, l=40))
elastic.append(Platform(screen, color=GREEN, x=200, y=300, w=100, l=30))
disappearing.append(Platform(screen, color=BLUE, x=600, y=200, w=100, l=40))
moving_v.append(Platform(screen, color=BLACK, x=20, y=400, w=100, l=30))
moving_h.append(Platform(screen, color=CYAN, x=400, y=400, w=100, l=30))
finished = False

while not finished:
    screen.fill(WHITE)
    arrow.update(ball)
    arrow.draw()
    ball.draw()
    finish.draw()
    for pl in platforms:
        pl.draw()
    for el in elastic:
        el.draw()
    for dis in disappearing:
        dis.draw()
    for mov in moving_v:
        mov.draw()
        mov.move_vertically(y_up=300, y_down=500)
        mov.precollision(ball)
        if mov.collision(ball):
            ball.sticking()
    for mov in moving_h:
        mov.draw()
        mov.move_horizontally(x_left=300, x_right=500)
        mov.precollision(ball)
        if mov.collision(ball):
            ball.sticking()
    pygame.display.update()
    pygame.display.flip()

    clock.tick(FPS)

    for pl in platforms:
        pl.precollision(ball)
        if pl.collision(ball):
            ball.sticking()

    for el in elastic:
        el.precollision(ball)
        if el.collision(ball):
            ball.jumping_back(el)

    for dis in disappearing:
        dis.precollision(ball)
        if dis.collision(ball):
            disappearing.remove(dis)
            ball.fall(dis)
    arrow.power_up()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            arrow.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            arrow.fire2_start(event, ball)
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.jump(event, arrow)
            arrow.fire2_end(event)

    ball.move()
    ball.stop()

    if finish.collision(ball):
        win = True
        finished = True

esc = False
if win:
    screen.fill(WHITE)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
else:
    screen.fill(BLACK)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
pygame.quit()