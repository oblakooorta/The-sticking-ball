import pygame
import math 
"""
Это своего рода прицел - стрелка, которая показывает направление прыжка шарика.
Чем длиннее стрелка, тем с большей скоростью полетит шарик
"""
RED = 0xFF0000


class Guidance: 
    def __init__(self, screen, x, y, obj):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = False
        self.an = 1
        self.x = obj.x
        self.y = obj.y
        self.color = RED
        
    def fire2_start(self, event, obj):
        if obj.sticked:
            self.f2_on = True

    def fire2_end(self, event):
        self.f2_on = False
        self.f2_power = 10

    def targetting(self, event):
        if event:
            self.an = math.atan2((event.pos[1] -self.y), (event.pos[0] -self.x))
            
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 50:
                self.f2_power += 0.5
                
    def update(self, obj):
        self.x = obj.x
        self.y = obj.y
        
    def draw(self):
        pygame.draw.line(
            self.screen, 
            (0, 0, 0), 
            [self.x, self.y], [self.x + 1.8 * math.cos(self.an) * self.f2_power, self.y + 1.8 * math.sin(self.an) * self.f2_power], 
            7
        )
