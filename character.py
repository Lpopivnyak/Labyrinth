import pygame

class Character:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y



    def Render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
        elif keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed