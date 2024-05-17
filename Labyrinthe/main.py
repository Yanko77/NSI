from config import GRID as TAB
from labyrinthe import Labyrinthe, PathFinder


def main(tab):
    lab = Labyrinthe(tab)
    robot = PathFinder(lab)

    path = robot.find_path()
    print(path)


if __name__ == '__main__':
    main(tab=TAB)
