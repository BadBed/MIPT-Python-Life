class Fish:
    def __init__(self):
        self.id = 'f'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Fish().id] <= 3:
            return Fish()
        else:
            return Nothing()


class Shrimp:
    def __init__(self):
        self.id = 's'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Shrimp().id] <= 3:
            return Shrimp()
        else:
            return Nothing()


class Rock:
    def __init__(self):
        self.id = 'r'

    @staticmethod
    def get_updated(life, x, y):
        return Rock()


class Nothing:
    def __init__(self):
        self.id = 'n'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if neighbors[Fish().id] == 3:
            return Fish()
        elif neighbors[Shrimp().id] == 3:
            return Shrimp()
        else:
            return Nothing()
