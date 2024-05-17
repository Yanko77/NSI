import pygame


class AnimateSprite(pygame.sprite.Sprite):  # Classe qui va s'occuper des animations

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load('assets/' + sprite_name + '.png')  # Attribut obligatoire car super-classe Sprite
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # Commencer à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # Methode pour démarer l'animation
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):

        if self.animation:
            # Passer à l'image suivante
            self.current_image += 1
            if self.current_image >= len(self.images):  # Verifier si on a atteint la fin de l'animation
                self.current_image = 0

                if not loop:  # Si l'animation n'est pas une boucle, on désactive
                    self.animation = False  # Désactiver l'animation

            # Actualiser l'image
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


def load_animation_images(sprite_name):
    # Charger les 24 images du sprite
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"  # Chemin de l'image

    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images


animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}


