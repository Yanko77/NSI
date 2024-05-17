import pygame
import random
import animation


class Monster(animation.AnimateSprite):  # Classe pour représenter les monstres

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3

        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()

        self.is_slowed = False

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(3, speed)
        self.origin_velocity = self.velocity

    def slow(self):
        self.is_slowed = True

    def is_slowed(self):
        if self.is_slowed:
            return True
        return False

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)  # Couleur jauge de vie
        back_bar_color = (60, 63, 60)  # Couleur background jauge de vie

        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]  # Position & Dimensions de la jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]  # Position & Dimensions background

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collisions(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


# Définir une classe pour la mummy
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(5)


# Définir une class pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(3)
        self.attack = 0.8