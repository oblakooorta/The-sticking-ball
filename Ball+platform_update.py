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

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 1
    else:
        return -1

class Ball:
    """ 
    Это шарик - основной персонаж нашей игры.
    он будет прыгать по платформам и прилипать к ним.
    Также он будет менять силу прыжка в зависимости от зажатия мышки.
    """
    
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
            self.an = math.atan2((event.pos[1] - ball.y), (event.pos[0] - ball.x))
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
        
    
    

class Guidance:
    """
    Это своего рода прицел - стрелка, которая показывает направление прыжка шарика.
    Чем длиннее стрелка, тем с большей скоростью полетит шарик
    """
    
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = False
        self.an = 1
        self.x = ball.x
        self.y = ball.y
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
                
    def update(self):
        self.x = ball.x
        self.y = ball.y
        
    def draw(self):
        pygame.draw.line(
            self.screen, 
            (0, 0, 0), 
            [self.x, self.y], [self.x + 1.8 * math.cos(self.an) * self.f2_power, self.y + 1.8 * math.sin(self.an) * self.f2_power], 
            7
        )

    

class Platform:
    """
    Это платформа. В зависимости от типа она будет обладать разными свойствами
    Самое простое свойство - прилипание
    """
    def __init__(self, screen, color, x=550, y=300, l=100, w=20):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.phi = choice([math.pi/2, 0])
        self.color = color
        
    def collision(self, obj):
        if abs(obj.x - self.x) < self.w/2 + obj.r and abs(obj.y - self.y) < self.l/2 + obj.r:
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
            

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
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


ball = Ball(screen, x = 400, y = 300)
arrow = Guidance(screen, x = 400, y = 300)
platforms.append(Platform(screen, color = RED))
platforms.append(Platform(screen, color = RED, x=400, y=500, w=150, l=20))
elastic.append(Platform(screen, color = GREEN, x = 200, y = 300, w = 100, l = 30))
disappearing.append(Platform(screen, color = BLUE, x = 600, y = 200, w = 100, l = 40))
finished = False

while not finished:
    screen.fill(WHITE)
    arrow.update()
    arrow.draw()
    ball.draw()
    for pl in platforms:
        pl.draw()
    for el in elastic:
        el.draw()
    for dis in disappearing:
        dis.draw()
    pygame.display.update()
    pygame.display.flip()

    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            arrow.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            arrow.fire2_start(event, ball)
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.jump(event, arrow)
            arrow.fire2_end(event)

    ball.move()
    ball.stop()
    for pl in platforms:
        if pl.collision(ball):
            ball.sticking()
    
    for el in elastic:
        if el.collision(ball):
            ball.jumping_back(el)
    
    for dis in disappearing:
        if dis.collision(ball):
            disappearing.remove(dis)
            ball.fall(dis)
    arrow.power_up()

pygame.quit()



