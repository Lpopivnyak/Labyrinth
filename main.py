import pygame

import character
import enemy
import gold

import wall

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)
money_taunt = pygame.mixer.Sound("money.ogg")

backgroundImage = pygame.image.load("background.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))

pacman_Ghost = character.Character(50, 550, 50, 50, 10, "hero.png")
pacman_Cyborg_Ghost = enemy.Enemy(850, 350, 50, 50, 10, "cyborg.png", 100, 200, 300, 300)
gold = gold.Gold(500, 500, 50, 50, "treasure.png")

walls = []
walls.append(wall.Wall(120, 525, 200, 10, (0, 0, 0)))
walls.append(wall.Wall(120, 610, 200, 10, (0, 0, 0)))

game = True

while game:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    #оновлення
    pacman_Ghost.movement()

    for wall in walls:
        if pacman_Ghost.hitbox.colliderect(wall.rect):
            game = False

    if pacman_Ghost.hitbox.colliderect(gold.hitbox):
        money_taunt.play()
        gold.hitbox.x = 1000000
        game = False

    #рендер
    window.fill((0, 0, 0))
    window.blit(backgroundImage, (0, 0))

    pacman_Ghost.Render((window))
    pacman_Cyborg_Ghost.Render((window))
    gold.Render(window)

    for wall in walls:
        wall.Render(window)

    pygame.display.flip()
    fps.tick(60)