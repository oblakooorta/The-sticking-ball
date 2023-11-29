import math
from random import choice
import sys
import pygame
import time

FPS = 30

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
GAME_COLORS = [RED, BLUE, WHITE]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.live = 30

    def move(self):
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
            
    def is_stopped(self):
        return (self.vx ** 2 + self.vy ** 2) < 0.1
    
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    
    def jump(self, event):
        self.an = math.atan2((event.pos[1] - ball.y), (event.pos[0] - ball.x))
        ball.vx = arrow.f2_power * math.cos(self.an)
        ball.vy = - arrow.f2_power * math.sin(self.an)

class Guidance:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = ball.x
        self.y = ball.y
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            self.an = math.atan2((event.pos[1] -self.y), (event.pos[0] -self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK

    def draw(self):
        pygame.draw.line(
            self.screen, 
            (0, 0, 0), 
            [self.x, self.y], [self.x + 1.5 * math.cos(self.an) * self.f2_power, self.y + 1.5 * math.sin(self.an) * self.f2_power], 
            7
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
    def update(self):
        self.x = ball.x
        self.y = ball.y

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ball = Ball(screen, x = 400, y = 300)
arrow = Guidance(screen, x = 400, y = 300)
finished = False

clock = pygame.time.Clock()
while not finished:
    screen.fill(WHITE)
    arrow.update()
    arrow.draw()
    ball.draw()
      
    pygame.display.update()
    pygame.display.flip()

    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            arrow.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            arrow.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            arrow.fire2_end(event)
            ball.jump(event)

    
    ball.move()
    
    arrow.power_up()

pygame.quit()



