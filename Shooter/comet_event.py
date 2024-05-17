import pygame
from comet import Comet


class CometFallEvent:  # Classe qui gère l'evenement Chute de Cometes

    def __init__(self, game):
        self.game = game

        self.percent = 0  # Compteur de %tage de l'evenement
        self.percent_speed = 25

        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):

        for i in range(1, 20):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):

        self.add_percent()

        # Barre noire ( Background )
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # Coordonnées en x
            surface.get_height() - 20,  # Co en y
            surface.get_width(),  # Longueur de la barre
            10  # Epaisseur de la barre
        ])

        # Barre rouge ( 1er plan )
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # Coordonnées en x
            surface.get_height() - 20,  # Co en y
            (surface.get_width() / 100) * self.percent,  # Longueur de la barre
            10  # Epaisseur de la barre
        ])

