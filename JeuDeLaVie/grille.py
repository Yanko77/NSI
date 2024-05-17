import pygame
from case import Case


class Grille:  # Uniquement 10x10

    def __init__(self):
        self.grille = []  # Uniquement les têtes des listes chainées de cases de chaque ligne
        self.init_cases()

        self.tour = 0

    def init_cases(self):
        """
        Methode d'initialisation des cases de la grille ainsi que les relations qu'elles ont entre-elles.
        """

        with open('default_grille.txt', 'r') as file:
            file = file.read().split('\n')
            y = 0
            for line in file:
                line = line.split(' ')
                if y == 0:
                    self.grille.append(Case(0, y, int(line[0])))
                else:
                    self.grille.append(Case(0, y, int(line[0]), up=self.grille[y-1]))
                current_case = self.grille[y]
                x = 1
                for value in line[1:]:
                    if y == 0:
                        current_case.right = Case(x, y, int(value), left=current_case)
                    else:
                        current_case.right = Case(x, y, int(value), left=current_case, up=self.grille[y-1].get(x))

                    current_case = current_case.right
                    x += 1

                y += 1

        for case in self.grille:
            current_case = case
            for i in range(10):
                if current_case is not None and current_case.pos.y < 9:
                    current_case.down = self.grille[current_case.pos.y + 1].get(current_case.pos.x)
                current_case = current_case.right

    def update(self, surface):
        """
        Methode d'actualisation de l'affichage des toutes les cases ligne par ligne, de gauche à droite.
        """
        for case in self.grille:
            current_case = case
            while current_case is not None:
                current_case.update(surface)
                current_case = current_case.right

    def next_tour(self):
        """
        Methode qui permet de passer à l'étape suivante de la simulation dans cet ordre :
        - Calcul hypothétique du tour suivant de toutes les cases
        - Application des nouveaux status de chaque case précédemment calculés simultanément
        """
        self.tour += 1
        for case in self.grille:
            for c in case.get_list():
                c.calcul_next_tour()
        for case in self.grille:
            for c in case.get_list():
                c.next_tour()
