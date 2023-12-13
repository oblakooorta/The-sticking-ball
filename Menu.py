import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Menu:
    """
    A starting and pause menu
    """
    def __init__(self, x, y, width, height, color, text):
        """Set menu parameters

        x:
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
