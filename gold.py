import pygame

class Gold:
    def __init__(self, x, y, w, h, texture):
        self.texture = pygame.image.load(texture)
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))

    def Render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))
