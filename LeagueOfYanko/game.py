import pygame
import pytmx
import pyscroll

import random

import configs
from cursor import Cursor

from entity import Entity
from player import Player
from monsters import Minion

MAP_ZOOM = 2


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("JeuYanko")

        self.cursor = Cursor()

        self.mouse_pressed = {
            1: False,
            2: False,
            3: False
        }

        self.pressed = {pygame.K_RIGHT: 0,
                        pygame.K_LEFT: 0,
                        pygame.K_UP: 0,
                        pygame.K_DOWN: 0}

        # Map loading
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = MAP_ZOOM

        self.group = pyscroll.PyscrollGroup(self.map_layer, default_layer=4)

        # Joueur
        player_spawnpoint = tmx_data.get_object_by_name("Player")
        self.player = Player(self.group, player_spawnpoint.x, player_spawnpoint.y)

        self.group.add(self.player)

        # Liste des elements de collision
        self.walls = [
            pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            for obj in tmx_data.objects
            if obj.type == "walls"
        ]

        self.river = [
            pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            for obj in tmx_data.objects
            if obj.type == "collision"
        ]
        self.collisions_objects = self.walls + self.river

    def update(self):
        self.update_cursor_pos()

        self.spawn_monsters()

        self.group.update()

        if self.mouse_pressed[3]:
            self.move_player(self.cursor.pos)

        # Gestion des collisions
        for sprite in self.group.sprites():
            if isinstance(sprite, Entity):
                if sprite.feet.collidelist(self.collisions_objects) > -1:
                    sprite.move_back()

    def move_player(self, pos):

        dist_x = self.player.feet.center[0] - pos.x
        dist_y = self.player.feet.center[1] - pos.y

        self.player.start_moving(dist_x, dist_y)

    def update_cursor_pos(self):
        x = pygame.mouse.get_pos()[0] * 1 / MAP_ZOOM + self.group.view.x
        y = pygame.mouse.get_pos()[1] * 1 / MAP_ZOOM + self.group.view.y

        self.cursor.set_pos((x, y))

    def spawn_monsters(self):
        # Minions
        nb_minions = 0
        for entity in self.group.sprites():
            if type(entity) == Minion:
                nb_minions += 1

        for i in range(3 - nb_minions):
            new_minion = Minion(
                    group=self.group,
                    x=self.player.pos[0] + self.player.rect.center[0] + random.randint(-400, 400),
                    y=self.player.pos[1] + self.player.rect.center[1] + random.randint(-400, 400)
                )

            new_minion.set_target(self.player)

            self.group.add(new_minion)

    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_pos()
            self.update()

            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed[event.button] = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pressed[event.button] = False

                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

            clock.tick(configs.FPS)

        pygame.quit()
