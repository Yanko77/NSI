

class Labyrinthe:

    def __init__(self, tab):
        self.tab = tab

    @property
    def nblignes(self):
        return len(self.tab)

    @property
    def nbcolonnes(self):
        return len(self.tab[0])

    @property
    def depart(self):
        """
        Renvoie les coordonnées du départ.
        """
        y = 0
        for row in self.tab:
            x = 0
            for value in row:
                if value == 2:
                    return y, x
                x += 1
            y += 1

    @property
    def arrivee(self):
        """
        Renvoie les coordonnées de l'arrivée.
        """
        y = 0
        for row in self.tab:
            x = 0
            for value in row:
                if value == 3:
                    return y, x
                x += 1
            y += 1

    def _set_value(self, co, value: int):
        """
        Modifie la valeur de la case dont les co sont passées en paramètre.

        @in : tuple, (y, x)
        @in : int
        """
        y = co[0]
        x = co[1]

        self.tab[y][x] = value

    def get_value(self, co):
        """
        Retourne la valeur de la case dont les co sont passées en paramètre.

        @in : tuple, (y, x)
        @out : int
        """
        y = co[0]
        x = co[1]

        return self.tab[y][x]

    def _est_valide(self, co):
        """
        Retourne True si les coordonnées passées en parametre sont valides, False sinon.

        @in : tuple, (y, x)
        @out : bool
        """
        y = co[0]
        x = co[1]

        return 0 <= y < self.nblignes and 0 <= x < self.nbcolonnes

    def _est_libre(self, co):
        """
        Retourne True si la case dont les coordonnées sont passées en parametre est libre, False sinon.

        @in : tuple, (y, x)
        @out : bool
        """
        y = co[0]
        x = co[1]

        return self.tab[y][x] != 1

    @property
    def nb_cases_vides(self):
        """
        Retourne le nombre de cases libres du labyrinthe.

        @out: int
        """
        nb = 0

        for row in self.tab:
            for value in row:
                if value != 1:
                    nb += 1

        return nb

    def visiter(self, co):
        """
        J'ai préféré l'appeler "visiter" plutot que "est_visite" car pour moi une méthode qui commence par "est/ou" doit
        retourner un booléen.
        """

        if self.get_value(co) != 5:
            self._set_value(co, 4)

    def liste_voisines_libres(self, co):
        """
        Retourne la liste des cases libres voisines à la case dont les coordonnées sont passées en paramètre.

        @in : tuple, (y, x)
        @out : list
        """

        y = co[0]
        x = co[1]

        liste = []

        # TOP
        top = (y-1, x)
        if self._est_valide(top) and self._est_libre(top):
            liste.append(top)

        # BOTTOM
        bottom = (y+1, x)
        if self._est_valide(bottom) and self._est_libre(bottom):
            liste.append(bottom)

        # LEFT
        left = (y, x-1)
        if self._est_valide(left) and self._est_libre(left):
            liste.append(left)

        # RIGHT
        right = (y, x+1)
        if self._est_valide(right) and self._est_libre(right):
            liste.append(right)

        return liste

    def case_fausse(self, co):
        """
        Marque une case du labyrithe comme ne menant pas à la sortie.
        """
        self._set_value(co, 5)

    def __str__(self):
        text = ''
        for row in self.tab:
            for value in row:
                text += f'{value} '
            text += '\n'

        return text

    def affiche(self):
        """
        Affiche le labyrinthe.
        """
        print(self.__str__())

    @property
    def copy(self):
        """
        Renvoie une copie du labyrinthe.
        """
        return self.__class__(self.tab)


class PathFinder:
    """
    Classe représentant un robot pouvant parcourir un labyrinthe et en trouver le chemin solution menant à la sortie.
    """

    def __init__(self, lab: Labyrinthe):
        self.lab = lab.copy

        self.pos = (0, 0)

    def _set_pos(self, co):
        self.pos = co

    def _choose_way(self):
        """
        Méthode qui choisit la prochaine case du chemin parcouru par le PathFinder selon sa position dans le labyrinthe.
        Retourne None s'il n'y a plus aucun nouveau chemin et qu'il faut rebrousser chemin.

        @out : tuple or None
        """

        possible_ways = self.lab.liste_voisines_libres(self.pos)

        liste = []
        for way in possible_ways:
            value = self.lab.get_value(way)
            if value == 0:
                liste.append(way)
            elif value == 3:
                return way

        if not liste:
            return None
        else:
            return liste[0]

    def find_path(self):
        """
        Méthode qui retourne le chemin menant à l'arrivée.
        Retourne une liste vide s'il n'existe pas de solution

        @out : list
        """
        self.pos = self.lab.depart

        current_path = [self.pos]  # Pile
        self.lab.visiter(self.pos)

        is_path_found = False

        while not is_path_found and current_path:
            next_pos = self._choose_way()

            if next_pos is None:  # Impasse
                self._set_pos(current_path.pop())
                self.lab.case_fausse(self.pos)

            else:
                self._set_pos(next_pos)
                current_path.append(self.pos)

                if self.pos == self.lab.arrivee:
                    is_path_found = True
                else:
                    self.lab.visiter(self.pos)

        return current_path
