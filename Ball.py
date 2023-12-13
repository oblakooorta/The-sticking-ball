import pygame
import math

BLACK = (0, 0, 0)

class Ball:
    """
    Ball is the main character of our game which has to
    get to a finish line
    """
    def __init__(self, screen: pygame.Surface, x, y):
        """Set starting parameters for ball

        screen: screen, pygame.display
        x: x coordinate, int
        y: y coordinate, int

        """
        self.screen = screen
        self.sx = x
        self.sy = y
        self.x = x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.sticked = False

    def move(self):
        """Move ball if it's not sticked"""
        if  not self.sticked:
            self.x += self.vx
            self.y -= 2 * self.vy
            if self.x <= 1270 and self.x >= 10:
                self.vx = self.vx
            else:
                self.vy =  0.8 * self.vy
                self.vx = -0.8 * self.vx
            if self.y <= 710 and self.y >= 30:
                self.vy -= 1
            else:
                self.vy = -0.8 * self.vy
                self.vx = 0.8 * self.vx
            if self.y < 30:
                self.y = 35
            elif self.y > 710:
                self.y = 715
            if self.x < 10:
                self.x = 15
            elif self.x > 1270:
                self.x = 1265
    
    def stop(self):
        """Stop ball if it reaches the bottom"""
        if abs(self.vx) < 1 and abs(self.vy) < 1 and self.y >= 720 - 2*self.r:
            self.vx = self.vy = 0
            self.sticked = True

    
    def draw(self):
        """Draw a ball"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    
    def jump(self, event, obj):
        """Make ball jump from a platform

        event: mouse click, pygame.MOUSEBUTTONDOWN
        obj: platform, Platform
        """
        if self.sticked and obj.f2_on:
            self.sticked = False
            self.an = math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))
            self.vx = obj.f2_power * math.cos(self.an)
            self.vy = - obj.f2_power * math.sin(self.an)

    def sticking(self):
        """Sticking to normal platform"""
        if self.sticked:
            self.vx = 0
            self.vy = 0

    def jumping_back(self, obj):
        """Jumping back from elastic platform

        obj: platform, Platform
        """
        if self.sticked:
            if abs(self.x - obj.x) <= obj.w/2:
                self.vy = -1.2 * self.vy
            if abs(self.y - obj.y) <= obj.l/2:
                self.vx = -1.2 * self.vx
            self.sticked = False

    def fall(self):
        """Fall from disappearing platform"""
        self.vx = self.vy = 0
        self.sticked = False

    def return_to_start(self):
        """Return to start from deadly platform"""
        self.sticked = False
        self.x = self.sx
        self.y = self.sy
        self.vx = self.vy = 0

    def move_v(self, obj):
        """Move along moving platform vertically

        obj: platform, Platform
        """
        self.sticked = True
        self.y += obj.vy
        if self.y <= obj.y_up or self.y >= obj.y_down:
            self.vy *= -1

    def move_h(self, obj):
        """Move along moving platform horizontally

        obj: platform, Platform
        """
        self.sticked = True
        self.x += obj.vx
        if self.y <= obj.x_left or self.y >= obj.x_right:
            self.vy *= -1

    def move_update(self, obj):
        """Change speed if moving platfrom changes it

        obj: platform, Platform
        """
        self.vx = obj.vx
        self.vy = obj.vy