import pygame
import random


class Comet(pygame.sprite.Sprite):  # Classe pour gérer les comètes

    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event

        self.damage = 33.34

        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 950)
        self.rect.y = - random.randint(0, 800)
        self.velocity = random.randint(3, 8)

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # Verifier si le nb de comètes et de 0
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()  # Reset %tage
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


        if self.comet_event.game.check_collisions(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(self.damage)


