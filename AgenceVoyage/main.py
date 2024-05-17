from maps import AMERIQUE_DU_SUD, EUROPE
from path_finder import PathFinder



def main():

    question_region = input('Dans quelle région souhaitez-vous réaliser le voyage de vos rêves ?\n'
                            '- - - - - - -\n'
                            'Régions disponibles via notre compagnie :\n'
                            '--> 1. Amérique du Sud\n'
                            '--> 2. Europe\n\n'
                            'Région souhaitée : ').lower()

    question_region = question_region.replace(" ", "")

    if question_region in ('europe', '2', 'europa', 'eu', 'e'):
        region = EUROPE
    elif question_region in ('ameriquedusud', 'amériquedusud', '1', 'amerique', 'a'):
        region = AMERIQUE_DU_SUD

    robot_booker = PathFinder(map=region)

    pays = ['None', 'None']
    while len(pays) != 2 or pays[0] not in region.countries or pays[1] not in region.countries:
        print("Merci d'indiquer votre pays de départ et votre pays d'arrivée.\n"
              "Exemple: France République-Tchèque\n")
        pays = input('--> ').split(' ')

    depart = pays[0]
    arrivee = pays[1]

    print('Veuillez patienter quelques instants ( peut prendre plusieurs minutes ) ...')

    path = robot_booker.find_path([depart], arrivee)

    if path:
        for country in path:
            print(f'{country}', end="")
            if country != path[-1]:  # Si le pays en cours n'est pas le dernier, alors il faut faire la fleche
                print(' -> ', end="")
    else:
        print('Notre compagnie ne propose que des voyages par voie terrestre...\n'
              'Les pays renseignés ne sont pas atteignables ainsi.\n'
              'Nous vous conseillons de vous tourner vers la compagnie Noam-Airlines qui propose ce type de voyage.')


if __name__ == '__main__':
    main()
