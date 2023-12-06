import pygame

""" Это цель. По достижении нее начинается новый уровень
"""

class Goal:
    def __init__(self, screen, x = 20, y = 20):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.color = GREY
    
    def collision(self, obj):
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5 < self.r + obj.r:
            return True
    
    def draw(self):
        pygame.draw.polygon(self.screen,
                            self.color,
                            [[self.x - self.r * 3**0.5 / 2, self.y - self.r / 2],
                             [self.x + self.r * 3**0.5 / 2, self.y - self.r / 2],
                             [self.x, self.y + self.r]])