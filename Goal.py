import pygame

GREY = 0x7D7D7D


class Goal:
    """
    This is a thing that yoy have to touch to win
    """
    def __init__(self, screen, x, y):
        """Set starting conditions

        screen: screen, pygame.display
        x: x coordinate, int
        y: y coordinate, int
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        self.color = GREY
    
    def collision(self, obj):
        """collision with ball

        obj: ball, Ball
        """
        if ((self.x-obj.x)**2 + (self.y-obj.y)**2)**0.5 < self.r + obj.r:
            return True
    
    def draw(self):
        """Draw a goal"""
        pygame.draw.polygon(self.screen,
                            self.color,
                            [[self.x - self.r * 3**0.5 / 2, self.y - self.r / 2],
                             [self.x + self.r * 3**0.5 / 2, self.y - self.r / 2],
                             [self.x, self.y + self.r]])
