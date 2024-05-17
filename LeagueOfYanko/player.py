from entity import Entity


class Player(Entity):

    def __init__(self, group, x, y):
        super().__init__(
            name="Player",
            group=group,
            x=x,
            y=y
        )


