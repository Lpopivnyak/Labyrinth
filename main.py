import pygame
import character
import enemy

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

backgroundImage = pygame.image.load("background.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))

pacman_Ghost = character.Character(250, 350, 50, 50, 10, "hero.png")
pacman_Cyborg_Ghost = enemy.Enemy(850, 350, 50, 50, 10, "cyborg.png", 100, 200, 300, 300)

game = True

while game:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    #оновлення
    pacman_Ghost.movement()

    #рендер
    window.fill((0, 0, 0))
    window.blit(backgroundImage, (0, 0))

    pacman_Ghost.Render((window))
    pacman_Cyborg_Ghost.Render((window))

    pygame.display.flip()
    fps.tick(60)