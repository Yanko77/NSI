from grille import Grille

import pygame
pygame.init()


screen = pygame.display.set_mode((1000, 1000))

grille = Grille()

running = True

while running:
    grille.update(surface=screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grille.next_tour()

pygame.quit()