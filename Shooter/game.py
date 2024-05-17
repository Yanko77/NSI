import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from keybind import keybind_projectile, keybind_projectile_pressed, keybind_iceprojectile, keybind_iceprojectile_pressed
from augment_event import AugmentEvent


class Game:  # Classe du jeu

    def __init__(self):
        self.is_playing = False  # Status du jeu
        self.round = 0

        self.all_players = pygame.sprite.Group()  # Pour les collisions
        self.player = Player(self)  # Génération du joueur
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)
        self.augment_event = AugmentEvent(self)

        self.pressed = {}  # Touches appuyées actuellement

        self.font = pygame.font.Font('assets/fonts/(Unranked) Bdeogale.ttf', 30)

    def start(self):
        self.round += 1

        augment_selected = False
        self.augment_event.augment_mode = True
        augment_picks = self.augment_event.randomize_current_augments()

        '''while self.augment_event.augment_mode:
            if augment_selected:
                self.augment_event.augment_mode = False
            else:
                self.augment_event.update_choice(screen, augment_picks)'''


        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        if self.round > 1:
             self.spawn_monster(Mummy)
        if self.round > 3:
            self.spawn_monster(Mummy)
        if self.round > 5:
            self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.fire_stock = self.player.max_fire_stock
        self.comet_event.reset_percent()
        self.is_playing = False
        self.round = 0

    def update(self, screen):

        # Affichages
        screen.blit(self.player.image, self.player.rect)  # Sprite du joueur
        self.player.update_health_bar(screen)  # Barre de vie du joueur
        self.player.update_fire_bar(screen)  # Barre de stock de feu joueur
        self.comet_event.update_bar(screen)

        self.player.update_animation()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            if monster.is_slowed:
                monster.velocity = monster.origin_velocity * 55 / 100
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)  # Tous les projectiles, un par un
        self.all_monsters.draw(screen)  # Tous les monstres
        self.comet_event.all_comets.draw(screen)

        # Gestion du mouvement du joueur
        if self.pressed.get(pygame.K_RIGHT):  # Touche de Droite
            if (self.player.rect.x + self.player.rect.width) < screen.get_width():  # Ne sort pas de l'écran à Droite
                self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT):  # Touche de Gauche
            if self.player.rect.x > 0:  # Ne sort pas de l'écran à Gauche
                self.player.move_left()

        if self.player.fire_stock < 10:
            screen.blit(keybind_projectile_pressed.image, (990, 10))
        else:
            screen.blit(keybind_projectile.image, (990, 10))

        if self.player.ice_projectile_enabled:
            if self.player.is_in_cooldown:
                screen.blit(keybind_iceprojectile_pressed.image, (890, 10))
            else:
                screen.blit(keybind_iceprojectile.image, (890, 10))

        if self.player.is_in_cooldown:
            if pygame.time.get_ticks() >= self.player.time_begin_cd + 1500:
                self.player.is_in_cooldown = False

    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

