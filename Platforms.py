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
        self.vx = 2
        self.vy = 2
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
        if abs(obj.x - self.x) <= self.w/2 + obj.r and abs(obj.y - self.y) <=  self.l/2 + obj.r:
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