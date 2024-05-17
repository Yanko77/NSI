from entity import Entity
from spells import MinionsAutoAttack


class Minion(Entity):
    
    def __init__(self, group, x, y):
        super().__init__(
            name="Minion",
            group=group,
            x=x,
            y=y
        )

        self.target = None

        self.pv = 40
        self.health = self.pv

        self.armor = 5
        self.magic_resist = 5

        self.ap = 10
        self.ad = 5

        self.speed = 1
        self.range = 100

        self.auto_attack = MinionsAutoAttack(self)

    def update(self):
        if self.target is not None:
            if self.reach_target():
                self.attack()

        self.update_sprite()

    def reach_target(self):
        dist_x = self.rect.center[0] - self.target.rect.center[0]
        dist_y = self.rect.center[1] - self.target.rect.center[1]

        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5

        if dist <= self.range:
            self.stop_moving()
            return True
        else:
            self.start_moving(dist_x, dist_y)
            return False

    def attack(self):
        self.auto_attack.activate(self.target)

    def set_target(self, entity: Entity):
        self.target = entity

