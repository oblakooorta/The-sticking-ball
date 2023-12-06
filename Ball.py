import pygame
import math
from random import choice

BLACK = (0, 0, 0)
""" 
Это шарик - основной персонаж нашей игры.
он будет прыгать по платформам и прилипать к ним.
Также он будет менять силу прыжка в зависимости от зажатия мышки.
"""
class Ball:    
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.sticked = False

    def move(self):
        if  not self.sticked:
            self.x += self.vx
            self.y -= 2 * self.vy
            if self.x <= 790 and self.x >= 10:
                self.vx = self.vx
            else:
                self.vy =  0.8 * self.vy
                self.vx = -0.8 * self.vx
            if self.y <= 570 and self.y >=30:
                self.vy -= 1
            else:
                self.vy = -0.8 *self.vy
                self.vx = 0.8 * self.vx
            if self.y < 30:
                self.y = 35
            elif self.y > 570:
                self.y = 575
            if self.x < 10:
                self.x = 15
            elif self.x > 790:
                self.x = 785
    
    def stop(self):
        if abs(self.vx) < 1 and abs(self.vy) < 1 and self.y >= 600 - 2 * self.r:
            self.vx = self.vy = 0
            self.sticked = True

    
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    
    def jump(self, event, obj):
        if self.sticked and obj.f2_on:
            self.sticked = False
            self.an = math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
            self.vx = obj.f2_power * math.cos(self.an)
            self.vy = - obj.f2_power * math.sin(self.an)
    """
    Эта функция для обычной платформы
    """
    def sticking(self):
        if self.sticked:
            self.vx = 0
            self.vy = 0
    
    """
    Это функция для упругой платформы
    """        
    def jumping_back(self, obj):
        if self.sticked:
            if abs(self.x - obj.x) <= obj.w/2:
                self.vy = -1.2 * self.vy
            if abs(self.y - obj.y) <= obj.l/2:
                self.vx = -1.2 * self.vx
            self.sticked = False
            
    """
    Это функция для исчезающей платформы
    """
    def fall(self, obj):
        self.vx = self.vy = 0
        self.sticked = False

    """
    Это функция для смертельной платформы
    """
    
    
    