import pygame


class Pos:
    """
    Classe de représentation des coordonnées sur une grille
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Case:
    """
    Classe définissant chacune des cases de la grille indépendemment.
    """

    def __init__(self, x, y, value=0, up=None, right=None, down=None, left=None):
        self.pos = Pos(x, y)
        self.status = value

        self.up = up
        self.right = right
        self.left = left
        self.down = down

        self.future_value = self.status

    def update(self, surface):
        """
        Methode d'actualisation d'affichage du fond et du contour de la case.
        """
        pygame.draw.rect(surface,
                         (255 ** abs(1-self.status), 255 ** abs(1-self.status), 255 ** abs(1-self.status)),
                         pygame.Rect(self.pos.x*100, self.pos.y*100, 100, 100),)
        pygame.draw.rect(surface,
                         (0, 0, 0),
                         pygame.Rect(self.pos.x * 100, self.pos.y * 100, 100, 100),
                         width=1)

    def get(self, x):
        """
        Methode permettant d'accéder à une des cases à droite de celle-ci.
        @in: x, nombre de case à parcourir pour trouver la case recherchée.
        """
        i = 0
        current_case = self
        while i != x:
            current_case = current_case.right
            i += 1
        return current_case

    def get_list(self):
        """
        Methode qui renvoie la liste de toutes les cases à droite de celle-ci.
        @out: list
        """
        liste = []
        case = self
        while case is not None:
            liste.append(case)
            case = case.right
        return liste

    def compter_voisins(self):
        """
        Methode permettant de compter le nombre de cellules actives autour de celle-ci.
        @out: nb, int
        """
        nb = 0
        if self.up is not None:
            nb += self.up.status
            if self.up.right is not None:
                nb += self.up.right.status
        if self.right is not None:
            nb += self.right.status
            if self.right.down is not None:
                nb += self.right.down.status
        if self.down is not None:
            nb += self.down.status
            if self.down.left is not None:
                nb += self.down.left.status
        if self.left is not None:
            nb += self.left.status
            if self.left.up is not None:
                nb += self.left.up.status

        return nb

    def calcul_next_tour(self):
        """
        Methode calculant hypothetiquement la valeur futur de la cellule, a l'etape suivante de la simulation.
        """
        nb = self.compter_voisins()
        if nb < 2:
            self.future_value = 0
        elif nb == 2:
            self.future_value = self.status
        elif nb == 3:
            self.future_value = 1
        else:
            self.future_value = 0

    def next_tour(self):
        """
        Methode qui permet de passer à l'etape suivante de la simulation en appliquant la valeur future à la valeur courante.
        """
        self.status = self.future_value
