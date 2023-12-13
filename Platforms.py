import pygame


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


class Platform:
    """
    This is platform with which will interact ball
    """
    def __init__(self, screen, color, x, y, w, L, y_up=0, y_down=0, x_left=0, x_right=0):
        """Set starting conditions

        screen: screen, pygame.display
        color: color
        x: x coordinate, int
        y: y coordinate, int
        L: length, float
        w: width, float

        Keyword arguments:
        y_up: higher point, int
        y_down: lower point, int
        x_left: leftmost point, int
        x_right: rightmost point, int
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.L = L
        self.w = w
        self.x_left = x_left
        self.x_right = x_right
        self.y_up = y_up
        self.y_down = y_down
        self.vx = 2
        self.vy = 2
        self.color = color

    def precollision(self, obj):
        """Function that checks whether collision be in the next frame

        obj: ball, Ball
        """
        if (self.x - self.w/2 - obj.r + obj.vx < obj.x < self.x - self.w/2 - obj.r and
                self.y + self.L/2 > obj.y-obj.vy/obj.vx*(self.x-self.w/2-obj.r-obj.x) > self.y - self.L/2):
            obj.vx = -1*(self.x - self.w/2 - obj.r - obj.x)
            return True
        elif (self.x + self.w/2 + obj.r + obj.vx > obj.x > self.x + self.w/2 + obj.r and
              self.y + self.L/2 > obj.y-obj.vy/obj.vx*(self.x+self.w/2+obj.r-obj.x) > self.y - self.L/2):
            obj.vx = -1*(self.x + self.w/2 + obj.r - obj.x)
            return True
        elif (self.y - self.L/2 - obj.r + obj.vy < obj.y < self.y - self.L/2 - obj.r and
              self.x + self.w/2 > obj.x-obj.vx/obj.vy*(self.y-self.L/2-obj.r-obj.y) > self.x - self.w/2):
            obj.vy = -1*(self.y - self.L/2 - obj.r - obj.y)
            return True
        elif (self.y + self.L/2 + obj.r + obj.vy > obj.y > self.y + self.L/2 + obj.r and
              self.x + self.w/2 > obj.x-obj.vx/obj.vy*(self.y+self.L/2+obj.r-obj.y) > self.x - self.w/2):
            obj.vy = -1*(self.y - self.L/2 - obj.r - obj.y)
            return True

    def collision(self, obj):
        """Collision with ball

        obj: ball, Ball
        """
        if abs(obj.x - self.x) <= self.w/2 + obj.r and abs(obj.y - self.y) <= self.L/2 + obj.r:
            if (abs(self.x - obj.x) < (self.w/2 + obj.r)) and (abs(self.x - obj.x) > self.w/2):
                obj.x = self.x - (self.w/2 + obj.r) * sign(obj.vx)
            if (abs(self.y - obj.y) < (self.L/2 + obj.r)) and (abs(self.y - obj.y) > self.L/2):
                obj.y = self.y + (self.L/2 + obj.r) * sign(obj.vy)
            obj.sticked = True
            return True
    # FIXME
    # Тут возникает проблема при нулевой скрости и на углах. По какой-то причине шарик не прилипает
    # Иногда случаются баги и шар "проваливается" внутрь платформы

    def draw(self):
        """Draw platform"""
        pygame.draw.rect(self.screen,
                         self.color,
                         (self.x - self.w/2, self.y - self.L/2,
                          self.w, self.L))


class MovingPlatform(Platform):
    """
    Moving platform
    """
    def move_vertically(self):
        """Vertical movement"""
        self.y += self.vy
        if self.y <= self.y_up or self.y >= self.y_down:
            self.vy *= -1

    def move_horizontally(self):
        """Horizontal movement"""
        self.x += self.vx
        if self.x <= self.x_left or self.x >= self.x_right:
            self.vx *= -1
