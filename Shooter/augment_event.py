import pygame
import random


class AugmentEvent:

    def __init__(self, game):
        self.game = game

        self.augment_mode = False
        self.default_augments_choice = ['ManaSpeedBonus', 'Attackbonus', 'HealRegen']
        self.augments_choice = self.default_augments_choice

    def randomize_current_augments(self):
        current_dispo_augments = list(self.game.player.augments.keys())
        if not self.game.round < 2:
            pick1 = random.choice(current_dispo_augments)
            del current_dispo_augments[current_dispo_augments.index(pick1)]
            pick2 = random.choice(current_dispo_augments)
            del current_dispo_augments[current_dispo_augments.index(pick2)]
            pick3 = random.choice(current_dispo_augments)
            del current_dispo_augments[current_dispo_augments.index(pick3)]
        else:
            pick1 = self.default_augments_choice[0]
            pick2 = self.default_augments_choice[1]
            pick3 = self.default_augments_choice[2]

        augment_picks = [pick1, pick2, pick3]

        return augment_picks

    '''def update_choice(self, surface, augment_picks):
        for augment in augment_picks:
            self.game.'''