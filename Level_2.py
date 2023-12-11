import pygame
from random import choice
import math

from Ball import Ball
from Guidance import Guidance
from Goal import Goal

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


"""
Это платформа. В зависимости от типа она будет обладать разными свойствами
Самое простое свойство - прилипание
"""


class Platform:
    def __init__(self, screen, color, x, y, l, w, y_up=0, y_down=0, x_left=0, x_right=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.x_left = x_left
        self.x_right = x_right
        self.y_up = y_up
        self.y_down = y_down
        self.vx = 0.5
        self.vy = 0.5
        self.phi = choice([math.pi / 2, 0])
        self.color = color

    def precollision(self, obj):
        if self.x - self.w / 2 - obj.r + obj.vx < obj.x < self.x - self.w / 2 - obj.r and self.y + self.l / 2 > obj.y - obj.vy / obj.vx * (
                self.x - self.w / 2 - obj.r - obj.x) > self.y - self.l / 2:
            obj.vx = -1 * (self.x - self.w / 2 - obj.r - obj.x)
            return True
        elif self.x + self.w / 2 + obj.r + obj.vx > obj.x > self.x + self.w / 2 + obj.r and self.y + self.l / 2 > obj.y - obj.vy / obj.vx * (
                self.x + self.w / 2 + obj.r - obj.x) > self.y - self.l / 2:
            obj.vx = -1 * (self.x + self.w / 2 + obj.r - obj.x)
            return True
        elif self.y - self.l / 2 - obj.r + obj.vy < obj.y < self.y - self.l / 2 - obj.r and self.x + self.w / 2 > obj.x - obj.vx / obj.vy * (
                self.y - self.l / 2 - obj.r - obj.y) > self.x - self.w / 2:
            obj.vy = -1 * (self.y - self.l / 2 - obj.r - obj.y)
            return True
        elif self.y + self.l / 2 + obj.r + obj.vy > obj.y > self.y + self.l / 2 + obj.r and self.x + self.w / 2 > obj.x - obj.vx / obj.vy * (
                self.y + self.l / 2 + obj.r - obj.y) > self.x - self.w / 2:
            obj.vy = -1 * (self.y - self.l / 2 - obj.r - obj.y)
            return True

    def collision(self, obj):
        if abs(obj.x - self.x) <= self.w / 2 + obj.r and abs(obj.y - self.y) <= self.l / 2 + obj.r:
            if (abs(self.x - obj.x) < (self.w / 2 + obj.r)) and (abs(self.x - obj.x) > self.w / 2):
                obj.x = self.x - (self.w / 2 + obj.r) * sign(obj.vx)
            if (abs(self.y - obj.y) < (self.l / 2 + obj.r)) and (abs(self.y - obj.y) > self.l / 2):
                obj.y = self.y + (self.l / 2 + obj.r) * sign(obj.vy)
            obj.sticked = True
            return True

    # FIXME
    # Тут возникает проблема при нулевой скрости и на углах. По какой-то причине шарик не прилипает
    # Иногда случаются баги и шар "проваливается" внутрь платформы
    def draw(self):
        pygame.draw.rect(self.screen,
                         self.color,
                         (self.x - self.w / 2, self.y - self.l / 2,
                          self.w, self.l))

    """
    Это функция движения по вертикали
    """

    def move_vertically(self):
        self.y += self.vy
        if self.y <= self.y_up or self.y >= self.y_down:
            self.vy *= -1

    """
    Это функция движения по горизонтали
    """

    def move_horizontally(self):
        self.x += self.vx
        if self.x <= self.x_left or self.x >= self.x_right:
            self.vx *= -1


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

ball = Ball(screen, 100, 500)
arrow = Guidance(screen, 100, 100, ball)
finish = Goal(screen, x=1140, y=100)

finished = False
while not finished:
    screen.fill(WHITE)
    for pl in platforms:
        pl.draw()
    for d in death:
        d.draw()
    for m in moving_h:
        m.draw()
        m.move_horizontally()
    for m in moving_v:
        m.draw()
        m.move_vertically()
    for el in elastic:
        el.draw()
    for dis in disappearing:
        dis.draw()
    ball.draw()
    arrow.draw()
    finish.draw()



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

    if finish.collision(ball):
        win = True
        finished = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            arrow.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            arrow.fire2_start(event, ball)
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.jump(event, arrow)
            arrow.fire2_end(event)

    ball.move()
    ball.stop()
    arrow.update(ball)


    pygame.display.update()
    pygame.display.flip()
    arrow.power_up()
pygame.quit()