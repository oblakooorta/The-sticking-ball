import pygame
from random import choice
import math

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
    def __init__(self, screen, color, x, y, l, w, y_up, y_down, x_left, x_right):
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
        self.phi = choice([math.pi/2, 0])
        self.color = color

    def precollision(self, obj):
        if self.x - self.w/2 - obj.r + obj.vx < obj.x < self.x - self.w/2 - obj.r and self.y + self.l/2 > obj.y-obj.vy/obj.vx*(self.x-self.w/2-obj.r-obj.x) > self.y - self.l/2:
            obj.vx = -1*(self.x - self.w/2 - obj.r - obj.x)
            return True
        elif self.x + self.w/2 + obj.r + obj.vx > obj.x > self.x + self.w/2 + obj.r and self.y + self.l/2 > obj.y-obj.vy/obj.vx*(self.x+self.w/2+obj.r-obj.x) > self.y - self.l/2:
            obj.vx = -1*(self.x + self.w/2 + obj.r - obj.x)
            return True
        elif self.y - self.l/2 - obj.r + obj.vy < obj.y < self.y - self.l/2 - obj.r and self.x + self.w/2 > obj.x-obj.vx/obj.vy*(self.y-self.l/2-obj.r-obj.y) > self.x - self.w/2:
            obj.vy = -1*(self.y - self.l/2 - obj.r - obj.y)
            return True
        elif self.y + self.l/2 + obj.r + obj.vy > obj.y > self.y + self.l/2 + obj.r and self.x + self.w/2 > obj.x-obj.vx/obj.vy*(self.y+self.l/2+obj.r-obj.y) > self.x - self.w/2:
            obj.vy = -1*(self.y - self.l/2 - obj.r - obj.y)
            return True

    def collision(self, obj):
        if abs(obj.x - self.x) <= self.w/2 + obj.r and abs(obj.y - self.y) <= self.l/2 + obj.r:
            if (abs(self.x - obj.x) < (self.w/2 + obj.r)) and (abs(self.x - obj.x) > self.w/2):
                obj.x = self.x - (self.w/2 + obj.r) * sign(obj.vx)
            if (abs(self.y - obj.y) < (self.l/2 + obj.r)) and (abs(self.y - obj.y) > self.l/2):
                obj.y = self.y + (self.l/2 + obj.r) * sign(obj.vy)
            obj.sticked = True
            return True
    #FIXME
    #Тут возникает проблема при нулевой скрости и на углах. По какой-то причине шарик не прилипает
    #Иногда случаются баги и шар "проваливается" внутрь платформы
    def draw(self):
        pygame.draw.rect(self.screen,
                         self.color,
                         (self.x - self.w/2, self.y - self.l/2,
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
