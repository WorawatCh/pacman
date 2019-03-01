class Pacman:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pacman = Pacman(self, width // 2, height // 2)

     def update(self, delta):
        self.pacman.update(delta)
