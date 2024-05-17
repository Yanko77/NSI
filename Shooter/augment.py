import pygame
from projectile import IceProjectile


class Augment:  # Classe pour les augments de niveau

    def __init__(self, player):
        self.player = player

        self.attack_bonus = 0
        self.mana_velocity_bonus = 0
        self.mana_bonus_value = 0
        self.projectile_bonus = False
        self.heal_regen = False

        self.is_enabled = False

    def activate(self):
        self.is_enabled = True
        self.player.attack += self.attack_bonus
        self.player.mana_speed_reload += self.mana_velocity_bonus
        self.player.max_fire_stock += self.mana_bonus_value
        if self.projectile_bonus:
            self.player.ice_projectile_enabled = True
        if self.heal_regen:
            self.player.heal_regen_enabled = True

        print(str(self), 'activé')


class AttackBonus(Augment):

    def __init__(self, player, tier):
        super().__init__(player)
        self.attack_bonus = 10*tier


class ManaSpeedBonus(Augment):

    def __init__(self, player):
        super().__init__(player)
        self.mana_velocity_bonus = 0.10


class ManaBonusValue(Augment):

    def __init__(self, player):
        super().__init__(player)
        self.mana_bonus_value = 30


class ProjectileBonus(Augment):
    
    def __init__(self, player):
        super().__init__(player)
        self.projectile_bonus = True


class HealRegen(Augment):

    def __init__(self, player):
        super().__init__(player)
        self.heal_regen = True