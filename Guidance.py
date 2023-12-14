import pygame
import math 

RED = 0xFF0000


class Guidance:
    """
    This is an arrow that shows the direction of a jump
    """
    def __init__(self, screen, obj):
        """Set starting conditions

        screen: screen, pygame.display
        obj: ball, Ball
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = False
        self.an = 1
        self.x = obj.x
        self.y = obj.y
        self.color = RED
        
    def fire2_start(self, obj):
        """Start charging

        obj: ball, Ball
        """
        if obj.sticked:
            self.f2_on = True

    def fire2_end(self, obj):
        """Stop charging"""
        self.f2_on = False
        self.f2_power = 10
        obj.sticked = False

    def targetting(self, event):
        """Set a direction of arrow

        event: mouse move, pygame.MOUSEMOTION
        """
        if event:
            self.an = math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
            
    def power_up(self):
        """Continue charging"""
        if self.f2_on:
            if self.f2_power < 30:
                self.f2_power += 0.5
                
    def update(self, obj):
        """Set position of arrow to ball position

        obj: ball, Ball
        """
        self.x = obj.x
        self.y = obj.y
        
    def draw(self):
        """Draw arrow"""
        pygame.draw.line(
            self.screen, 
            (0, 0, 0),
            [self.x, self.y],
            [self.x + 1.8 * math.cos(self.an) * self.f2_power, self.y + 1.8 * math.sin(self.an) * self.f2_power],
            7
        )
