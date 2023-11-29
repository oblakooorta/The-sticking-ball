import pygame
import numpy
import math
import random

#Parameters of screen
WIDTH = 800
HEIGHT = 600

#Global variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#All planned types of platforms (None means normal one)
Types = ["Slippery", "Bouncy", "None", "Spiky", "Disappearing"]

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

class Ball:
    """
    Это шарик - основной персонаж нашей игры.
    он будет прыгать по стенам и прилипать к ним.
    Также он будет менять силу прыжка в зависимости от зажатия мышки.
    """
    def __init__(self, screen, x=400, y=300, r=20, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = self.vy = self.vel = self.phi = 0
        self.color = BLACK
        self.ischarging = False
        self.sticked = False
        
    def move(self):
        self.x += self.vx
        self.vy += 0.1
        self.y += self.vy
    
    def stop(self):
        self.vx = self.vy = 0
        
    def chargestart(self):
        if self.sticked:
            self.ischarging = True
        
    def charge(self):
        if self.vel < 10 and self.ischarging:
            self.vel += 0.5
        
    def jump(self):
        if self.ischarging:
            self.phi = math.atan2(event.pos[1] - self.y, event.pos[0] - self.x)
            self.vx = self.vel * math.cos(self.phi)
            self.vy = self.vel * math.sin(self.phi)
            self.vel = 0
            self.ischarging = False
            self.sticked = False
    
    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           [self.x, self.y],
                           self.r)
        
class Platform:
    """
    Это обычная платформа, к ней будет прилипать шарик и прыгать с неё
    """
    def __init__(self, screen, x=550, y=300, l=100, w=20):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.phi = random.choice([math.pi/2, 0])
        self.color = RED
        
    def collision(self, obj):
        if abs(obj.x - self.x) < self.w/2 + obj.r and abs(obj.y - self.y) < self.l/2:
            obj.x = self.x - sign(obj.vx) * (self.w/2 + obj.r)
            obj.sticked = True
            return True
        elif abs(obj.x - self.x) < self.w/2 and abs(obj.y - self.y) < self.l/2 + obj.r:
            obj.y = self.y - sign(obj.vy) * (self.l/2 + obj.r)
            obj.sticked = True
            return True
        
    def draw(self):
        pygame.draw.rect(self.screen,
                         self.color,
                         (self.x - self.w/2, self.y - self.l/2,
                          self.w, self.l))
class Slippery:
    """
    Это скользкая платформа. Можео сказать, что для нее нет сил трения
    """
    def __init__(self, screen, x, y, l, w):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        
        
pygame.init()

#define all parameters
k = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
platforms = []

#define all objects
ball = Ball(screen)
platforms.append(Platform(screen))
platforms.append(Platform(screen, x=400, y=500, w=150, l=20))
platforms.append(Platform(screen, x=200, y=550, w=200, l=100))

#game
while True:
    
    #draw all objects
    screen.fill(WHITE)
    ball.draw()
    for pl in platforms:
        pl.draw()
    pygame.display.update()
    
    #move all objects
    if not ball.sticked:
        ball.move()
        
    #sticking mechanic
    #FIXME some bug where ball cannot jump from platform
    for pl in platforms:
        if pl.collision(ball):
            ball.stop()
            
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
        elif event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball.chargestart()
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.jump()
        
        
        
        #all independent actions
        ball.charge()
        
pygame.quit()