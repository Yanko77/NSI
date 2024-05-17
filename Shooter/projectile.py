import pygame


class Projectile(pygame.sprite.Sprite):  # Classe qui va gérer les projectiles du joueur

    def __init__(self, player):
        super().__init__()  # Initialiser la super-classe
        self.velocity = 10
        self.projectile_type = None

        self.player = player
        self.attack = player.attack
        self.slow_percent = 100
        self.slow_time = 0

        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

        self.origin_image = self.image
        self.angle = 0

    def rotate(self):  # Faire tourner le projectile
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        self.rotate()

        # Collisions
        for monster in self.player.game.check_collisions(self, self.player.game.all_monsters):
            self.remove()  # Supprimer le projectile quand il touche un monstre
            monster.damage(self.attack)
            if self.projectile_type == 'ice':
                monster.slow()

        if self.rect.x > 1080:  # Supprimer le projectile si il sort de l'écran
            self.remove()


class IceProjectile(Projectile):

    def __init__(self, player):
        super().__init__(player)
        self.projectile_type = 'ice'
        self.velocity = 7
        self.image = pygame.image.load('assets/ice_projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.origin_image = self.image
        self.attack = player.attack*2
        self.slow_percent = 40
        self.slow_time = 2

