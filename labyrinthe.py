import time

class Labyrinthe:
    
    def __init__(self, tab):
        self.tab = tab
        
    def affiche(self):
        for ligne in self.tab:
            print(ligne)
            
    @property
    def nblignes(self):
        return len(self.tab)
    
    @property
    def nbcolonnes(self):
        return len(self.tab[0])
    
    @property
    def depart(self):
        i = 0
        for ligne in self.tab:
            j = 0
            for case in ligne:
                if case == 2:
                    return (i, j)
                j += 1
                
            i += 1
          
    @property
    def arrivee(self):
        i = 0
        for ligne in self.tab:
            j = 0
            for case in ligne:
                if case == 3:
                    return (i, j)
                j += 1
                
            i += 1
            
    def case(self, co):
        x = co[1]
        y = co[0]
        
        return self.tab[y][x]
    
    def est_valide(self, co):
        x = co[0]
        y = co[1]
        
        if 0 <= y <= self.nbcolonnes - 1:
            if 0 <= x <= self.nblignes - 1:
                return True
            
        return False
    
    def nb_cases_vides(self):
        nb_cases = 0
        
        for ligne in self.tab:
            for case in ligne:
                if case != 1:
                    nb_cases += 1
        
        return nb_cases
    
    def est_visite(self, co):
        x = co[1]
        y = co[0]
        
        self.tab[y][x] = 4
        
    def liste_voisines_libres(self, co):
        x = co[1]
        y = co[0]
        
        liste = []
        if x > 0 and self.tab[y][x-1] in (0, 2, 3):
            liste.append((y, x-1))
        if y > 0 and self.tab[y-1][x] in (0, 2, 3):
            liste.append((y-1, x))
        if x < self.nblignes - 1 and self.tab[y][x+1] in (0, 2, 3):
            liste.append((y, x+1))
        if y < self.nbcolonnes - 1 and self.tab[y+1][x] in (0, 2, 3):
            liste.append((y+1, x))
            
        return liste
    
    def case_fausse(self, co):
        x = co[1]
        y = co[0]

        if self.tab[y][x] == 4:
            self.tab[y][x] = 5
            
class SuperRobot:
    
    def __init__(self, labyrinthe: Labyrinthe):
        self.lab = labyrinthe
        
        self.pos = self.lab.depart
        
    def _choose_way(self):
        possible_ways = self.lab.liste_voisines_libres(self.pos)
        # print(possible_ways)
        
        
        if possible_ways == []:
            return None
        else:
            return possible_ways[0]
        
    def find_path(self):
        current_path = [self.pos]
        self.lab.est_visite(self.pos)
        
        path_found = False
        
        while not path_found and len(current_path) > 0:
            
            self.lab.affiche()
            print()
            
            next_case = self._choose_way()
            # print(next_case)
            if next_case is None:
                self.lab.case_fausse(self.pos)
                
                self.pos = current_path.pop()
                
                if self.lab.case(self.pos) == 4 :
                    self.lab.case_fausse(self.pos)
                    
                
            else:
                self.pos = next_case
                current_path.append(self.pos)
                
                if self.pos == self.lab.arrivee:
                    path_found = True
                
                self.lab.est_visite(self.pos)
            
            time.sleep(0.3)
        
        return current_path
            
        
    

    
def main():
    tab1 = [
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 3, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
        ]
    
    lab = Labyrinthe(tab1)
    print(lab.nb_cases_vides())
    print(lab.liste_voisines_libres((1, 5)))
    
    robot = SuperRobot(lab)
    for co in robot.find_path():
        print(co)

if __name__ == '__main__':
    main()
                