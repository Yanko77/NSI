import pygame


class Cursor:
    """
    Classe qui gère le curseur de souris
    """

    def __init__(self):
        pygame.mouse.set_cursor(*pygame.cursors.load_xbm("cursor.xbm", "cursor_mask.xbm"))

        self._pos = Pos(0, 0)

    @property
    def pos(self): return self._pos

    def set_pos(self, pos):
        self.pos.x, self.pos.y = pos[0], pos[1]


class Pos:
    """
    Classe représentant des coordonnés
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
