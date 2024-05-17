import pygame
import math
from game import Game
pygame.init()

# Definir une clock
clock = pygame.time.Clock()
FPS = 60


# Fenetre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))  # renvoie une surface

# Background
background = pygame.image.load('assets/bg.jpg')

# Bannière d'accueil
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Bouton JOUER
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Charger le jeu
game = Game()

running = True
while running:

    # Affichages
    screen.blit(background, (0, -200))  # Background

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (banner_rect.x, 0))


    # Mise à jour de l'écran
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Fermeture de fenetre
            running = False

        if event.type == pygame.KEYDOWN:  # Touche appuyée
            game.pressed[event.key] = True

            if event.key == pygame.K_a:
                if game.player.fire_stock >= 10:
                    game.player.launch_projectile()

            elif event.key == pygame.K_z:
                if game.player.ice_projectile_enabled:
                    if not game.player.is_in_cooldown:
                        game.player.launch_ice_projectile()
                        game.player.time_begin_cd = pygame.time.get_ticks()
                        game.player.active_cooldown()

            elif event.key == pygame.K_m:
                print(game.augment_event.randomize_current_augments())

        if event.type == pygame.KEYUP:  # Touche lachée
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
    # Fixer le nombre de FPS sur la clock
    clock.tick(FPS)
pygame.quit()
