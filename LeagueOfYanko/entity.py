import pygame
import pyscroll


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, name: str, x: int, y: int):
        super().__init__()
        self.name = name
        self.sprite_sheet = pygame.image.load(f'{self.name}.png')
        self.sprite_frame = 0
        self.clock = 0

        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96),
        }
        self.image = self.images['up'][self.sprite_frame]

        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.w * 0.7, 12)

        self.pos = [x, y]
        self.old_pos = self.pos.copy()

        self.next_moves = {
            'right': 0,
            'left': 0,
            'up': 0,
            'down': 0,
        }
        self.remaining_steps = 0

        self.speed = 5

    def update_sprite(self):
        self.move()

        self.rect.topleft = self.pos
        self.feet.midbottom = self.rect.midbottom

    def save_pos(self): self.old_pos = self.pos.copy()

    def set_direction(self, direction: str): self.image = self.images[direction][self.sprite_frame]

    def start_moving(self, dist_x, dist_y):
        self.stop_moving()

        dist = (dist_x**2 + dist_y**2)**0.5
        self.remaining_steps = dist // self.speed

        if self.remaining_steps > 0:
            if dist_x > 0:
                self.next_moves["left"] = abs(dist_x / self.remaining_steps)
            else:
                self.next_moves["right"] = abs(dist_x / self.remaining_steps)

            if dist_y > 0:
                self.next_moves["up"] = abs(dist_y / self.remaining_steps)
            else:
                self.next_moves["down"] = abs(dist_y / self.remaining_steps)

    def stop_moving(self):
        self.remaining_steps = 0
        self.next_moves = {
            'right': 0,
            'left': 0,
            'up': 0,
            'down': 0,
        }

    def move(self):
        if self.remaining_steps > 0:
            self.pos[0] += self.next_moves['right']
            self.pos[0] -= self.next_moves['left']
            self.pos[1] -= self.next_moves['up']
            self.pos[1] += self.next_moves['down']

            self.remaining_steps -= 1

            self.animate()

    def move_back(self):
        self.stop_moving()

        self.pos = self.old_pos
        self.rect.topleft = self.pos
        self.feet.midbottom = self.rect.midbottom

    def animate(self):
        self.clock += self.speed*8

        if self.clock > 150:
            self.sprite_frame += 1
            if self.sprite_frame > 2:
                self.sprite_frame = 0

            self.clock = 0

        next_direction = self._get_next_direction()

        if next_direction is not None:
            self.set_direction(next_direction)

    def _get_next_direction(self):
        max_value = 0
        max_direction = None
        for direction in self.next_moves:
            if self.next_moves[direction] > max_value:
                max_direction = direction
                max_value = self.next_moves[direction]

        return max_direction

    def get_images(self, y):
        return [self._get_image(i*32, y) for i in range(3)]

    def _get_image(self, x, y):
        image = pygame.Surface((32, 32))
        image.fill((1, 0, 0))
        image.blit(self.sprite_sheet,
                   (0, 0),
                   (x, y, 32, 32))
        image.set_colorkey((1, 0, 0))
        return image


class Entity(AnimatedSprite):

    def __init__(self, name: str, group, x, y):
        self.name = name
        super().__init__(name, x, y)

        self.group = group

        # Defense
        self.pv = 100
        self.health = self.pv

        self.armor = 10
        self.magic_resist = 10

        # Attack
        self.ap = 15
        self.ad = 10

        # Mobility
        self.speed = 5
        self.range = 20

        # Spells
        self.spells = []

    @property
    def is_alive(self):
        return self.health > 0

    def update(self):
        self.update_sprite()

    def damage(self, amount: int):
        self.health -= amount

        if self.health < self.pv:
            self.health = 0
