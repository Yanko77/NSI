import pygame
from projectile import Projectile, IceProjectile
from augment import Augment, ManaBonusValue, ManaSpeedBonus, AttackBonus, ProjectileBonus, HealRegen
import animation


class Player(animation.AnimateSprite):  # Classe pour représenter le joueur

    def __init__(self, game):
        super().__init__('player')  # Pour initialiser la super-classe, au moment de l'initialisation du joueur
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 10
        self.attack = 25

        self.fire_stock = 100
        self.max_fire_stock = 100
        self.mana_speed_reload = 0.25

        self.ice_projectile_enabled = True
        self.heal_regen_enabled = True

        self.augment = Augment(self)
        self.augments = {
            'ManaSpeedBonus': ManaSpeedBonus(self),
            'ManaBonusValue': ManaBonusValue(self),
            'AttackBonus': {1: AttackBonus(self, tier=1), 2: AttackBonus(self, tier=2), 3: AttackBonus(self, tier=3)},
            'ProjectileBonus': ProjectileBonus(self),
            'HealRegen': HealRegen(self)
        }

        # self.image --> super-classe
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

        self.all_projectiles = pygame.sprite.Group()

        self.is_in_cooldown = False
        self.time_begin_cd = pygame.time.get_ticks()

    def active_cooldown(self):
        self.is_in_cooldown = True

    def stop_cooldown(self):
        self.is_in_cooldown = False

    def active_augment(self, augment_name, tier=0):
        if tier == 0:
            self.augments[augment_name].activate()
        else:
            self.augments[augment_name][tier].activate()

    def damage(self, amount):
        if self.health - amount > 0:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        if self.heal_regen_enabled and self.health + 0.05 < self.max_health:
            self.health += 0.05

        bar_color = (111, 210, 46)  # Couleur jauge de vie
        back_bar_color = (60, 63, 60)  # Couleur background jauge de vie

        bar_position = [self.rect.x + 50, self.rect.y +20, self.health, 7]  # Position & Dimensions de la jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]  # Position & Dimensions background

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def add_fire(self):
        self.fire_stock += self.mana_speed_reload

    def update_fire_bar(self, surface):
        if self.fire_stock < self.max_fire_stock:
            self.add_fire()

        # Jauges
        if self.fire_stock <= 25:
            bar_color = (255, 70, 0)  # Couleur jauge de feu faible
        elif self.fire_stock <= 75:
            bar_color = (255, 139, 0)  # Couleur jauge de feu moyenne
        else:
            bar_color = (255, 201, 0)  # Couleur jauge de feu haute

        back_bar_color = (60, 63, 60)  # Couleur background jauge de feu

        bar_position = [75, 20, self.fire_stock*3.5, 20]  # Position & Dimensions de la jauge de feu
        back_bar_position = [75, 20, self.max_fire_stock*3.5, 20]  # Position & Dimensions background

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

        # Textes
        fire_stock_text = self.game.font.render(str(int(self.fire_stock)), True, (0, 0, 0))
        if self.fire_stock < 100:
            surface.blit(fire_stock_text, (33, 12))
        else:
            surface.blit(fire_stock_text, (18, 12))

    def move_right(self):
        if not self.game.check_collisions(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.fire_stock -= 10
        self.all_projectiles.add(Projectile(self))  # Creation d'un nouveau projectile + ajout au groupe
        self.start_animation()

    def launch_ice_projectile(self):
        self.all_projectiles.add(IceProjectile(self))  # Creation d'un nouveau ice_projectile + ajout au groupe
        self.start_animation()

