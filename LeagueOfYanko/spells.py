import pygame

import configs

import pyscroll


class AnimatedSpell(pygame.sprite.Sprite):

    def __init__(self, name, entity, sprite_size=(32, 32)):
        self.name = name
        super().__init__()

        self.entity = entity

        self.sprite_sheet = pygame.image.load(f'{self.name}.png')
        self.sprite_size = sprite_size
        self.nb_sprites = 3
        self.sprite_frame = 0
        self.clock = 0

        self.images = [
            self.get_image(self.sprite_size[0] * i) for i in range(self.nb_sprites)
        ]
        self.image = self.get_current_image()

        self.holding_pos = list(self.entity.rect.topleft)  # Relating to entity rect : Spell Holding position ( Useless if holding_visible is False )
        self.holding_visible = False
        self.pos = list(self.holding_pos)
        self.rect = self.image.get_rect()

        self._next_moves = {
            'right': 0,
            'left': 0,
            'up': 0,
            'down': 0,
        }
        self._remaining_steps = 0

        self.cooldown = 2.
        self.cooldown_clock = self.cooldown
        self.is_in_cd = False
        self.is_activated = False

        self.target = None

        self.damage = 0
        self.speed = 5

    def update_sprite(self):
        if self.is_activated:
            self.reach_target()
        else:
            self.pos = [self.entity.pos.copy()[0] + self.holding_pos[0],
                        self.entity.pos.copy()[1] + self.holding_pos[1]]

        self.rect.topleft = self.pos

    def move(self):
        if self._remaining_steps > 0:
            self.pos[0] += self._next_moves['right']
            self.pos[0] -= self._next_moves['left']
            self.pos[1] -= self._next_moves['up']
            self.pos[1] += self._next_moves['down']

            self._remaining_steps -= 1

            self.animate()

        else:
            if self.is_activated:
                self.is_activated = False

    def reach_target(self):
        dist_x = self.rect.center[0] - self.target.rect.center[0]
        dist_y = self.rect.center[1] - self.target.rect.center[1]

        if self.rect.colliderect(self.target.rect):
            self.stop_moving()
            return True
        else:
            self.start_moving(dist_x, dist_y)
            return False

    def start_moving(self, dist_x, dist_y):
        self.stop_moving()

        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
        self._remaining_steps = dist // self.speed

        if self._remaining_steps > 0:
            if dist_x > 0:
                self._next_moves["left"] = abs(dist_x / self._remaining_steps)
            else:
                self._next_moves["right"] = abs(dist_x / self._remaining_steps)

            if dist_y > 0:
                self._next_moves["up"] = abs(dist_y / self._remaining_steps)
            else:
                self._next_moves["down"] = abs(dist_y / self._remaining_steps)

    def stop_moving(self):
        self._remaining_steps = 0
        self._next_moves = {
            'right': 0,
            'left': 0,
            'up': 0,
            'down': 0,
        }

    def animate(self):
        self.clock += self.speed*8

        if self.clock > 150:
            self.sprite_frame += 1
            if self.sprite_frame >= self.nb_sprites:
                self.sprite_frame = 0

            self.clock = 0

        self.image = self.get_current_image()

    def get_current_image(self):
        return self.images[self.sprite_frame]

    def get_image(self, x):
        image = pygame.Surface(self.sprite_size)
        image.fill((1, 0, 0))
        image.blit(self.sprite_sheet,
                   (0, 0),
                   (x, 0, self.sprite_size[0], self.sprite_size[1]))
        image.set_colorkey((1, 0, 0))
        return image


class AutoAttack(AnimatedSpell):

    def __init__(self, entity):
        super().__init__(
            name=f'{entity.name}-AutoAttack',
            entity=entity,
            sprite_size=(8, 8)
        )
        self.holding_visible = True
        self.entity.group.add(self)

        self.speed = 5.1

    def update(self):
        self.update_sprite()
        if self.is_in_cd:
            self.update_cooldown()

        self.move()

    def activate(self, target):
        if not self.is_in_cd:
            self.target = target
            self.is_activated = True
            self.is_in_cd = True
            self.cooldown_clock = self.cooldown
            self.start_moving(
                self.entity.pos[0] - target.pos[0],
                self.entity.pos[1] - target.pos[1]
            )

    def update_cooldown(self):
        self.cooldown_clock -= 1 / configs.FPS

        if self.cooldown_clock < 0:
            self.is_in_cd = False


class MinionsAutoAttack(AutoAttack):

    def __init__(self, entity):
        super().__init__(
            entity=entity
        )

        self.holding_pos = [26, 3]

