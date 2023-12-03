import pygame

class Enemy:
    def __init__(self, x, y, w, h, speed, texture, x1, y1, x2, y2):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def Render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def movement(self):
        pass