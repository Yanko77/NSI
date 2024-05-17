import pygame


class KeyBind:

    def __init__(self, image_path, keybind):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.key = keybind


keybind_projectile = KeyBind('assets/keybind_projectile.png', 'a')
keybind_projectile_pressed = KeyBind('assets/keybind_projectile_pressed.png', 'a')
keybind_iceprojectile = KeyBind('assets/keybind_ice_projectile.png', 'z')
keybind_iceprojectile_pressed = KeyBind('assets/keybind_ice_projectile_pressed.png', 'z')
