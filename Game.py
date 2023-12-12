import pygame

import math
from random import choice
import sys
import time

import Level_1

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

WIDTH = 1280
HEIGHT = 720

from Ball import Ball
from Guidance import Guidance
from Platforms import Platform
from Goal import Goal
from Menu import Menu


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
"""
Это обычные платформы.
"""
from Level_1 import platforms
"""
Это упругие платформы
"""
from Level_1 import elastic
"""
Это исчезающие платформы
"""
from Level_1 import disappearing

"""
Это движущиеся вертикально платформы
"""

from Level_1 import moving_v

"""
Это двигающиеся горизонтально платформы
"""

from Level_1 import moving_h

from Level_1 import x_started, y_started, x_end, y_end

ball = Ball(screen, x_started, y_started)
arrow = Guidance(screen, x_started, y_started, obj=ball)
finish = Goal(screen, x_end, y_end)

start_button = Menu(540, 310, 200, 100, RED, "Начать")
pause_button = Menu(1150, 30, 80, 40, RED, "Пауза")
win_text = Menu(540, 260, 200, 100, RED, "Победа!")
next_level = Menu(540, 450, 200, 100, RED, "Следующий уровень")

finished = False
game_started = False
game_paused = False
win = False
points = 0

while not finished:
    screen.fill(WHITE)
    if not game_started:
        start_button.draw(screen)
    else:
        pause_button.draw(screen)
    if win:
        points += 1
    if game_started:
        arrow.update(ball)
        arrow.draw()
        ball.draw()
        finish.draw()

        for mov in moving_v:
            mov.draw()
            mov.move_vertically()
            mov.precollision(ball)
            if mov.collision(ball):
                ball.sticking()
                ball.move_v(mov)

        for mov in moving_h:
            mov.draw()
            mov.move_horizontally()
            mov.precollision(ball)
            if mov.collision(ball):
                ball.sticking()
                ball.move_h(mov)

        for pl in platforms:
            pl.draw()
            pl.precollision(ball)
            if pl.collision(ball):
                ball.sticking()

        for el in elastic:
            el.draw()
            el.precollision(ball)
            if el.collision(ball):
                ball.jumping_back(el)

        for dis in disappearing:
            dis.draw()
            dis.precollision(ball)
            if dis.collision(ball):
                disappearing.remove(dis)
                ball.fall(dis)

        if finish.collision(ball):
            win = True
            finished = True

    if game_paused:
        game_started = not game_started
        game_paused = not game_paused

    pygame.display.update()
    pygame.display.flip()

    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            arrow.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            arrow.fire2_start(event, ball)
            if start_button.rect.collidepoint(event.pos):
                game_started = True
            if pause_button.rect.collidepoint(event.pos):
                game_paused = True
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.jump(event, arrow)
            arrow.fire2_end(event)
    arrow.power_up()
    ball.move()
    ball.stop()

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