

class PathFinder:

    def __init__(self, map):
        self.map = map

    def find_path(self, current_path, arrivee):

        if current_path and current_path[-1] == arrivee:
            return current_path
        else:

            # Récupérer les chemins ne passant pas par un pays visité
            simulated_paths = []

            for pays_frontalier in self.map.get_border_countries(current_path[-1]):
                if pays_frontalier not in current_path:
                    simulated_paths.append(self.find_path(current_path + [pays_frontalier], arrivee))

            # Prendre uniquement les chemins finissant à l'arrivée
            possible_paths = []
            for path in simulated_paths:
                if path and path[-1] == arrivee:
                    possible_paths.append(path)

            # S'il n'y en a pas, retourner une liste vide
            if not possible_paths:
                return []
            # Sinon retourner le plus grand
            else:
                max_path = None
                max_path_length = 0
                for path in possible_paths:
                    if len(path) > max_path_length:
                        max_path = path
                        max_path_length = len(path)

                return max_path
