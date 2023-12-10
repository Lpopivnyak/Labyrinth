import pygame

class Wall:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.rect.Rect(x, y, w, h)
        self.color = color

    def Render(self, window):
        pygame.draw.rect(window, self.color, self.rect)