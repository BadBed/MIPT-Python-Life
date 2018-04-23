class Fish:
    def __init__(self):
        self.key = 'f'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Fish().key] <= 3:
            return Fish()
        else:
            return Nothing()


class Shrimp:
    def __init__(self):
        self.key = 's'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Shrimp().key] <= 3:
            return Shrimp()
        else:
            return Nothing()


class Rock:
    def __init__(self):
        self.key = 'r'

    @staticmethod
    def get_updated(life, x, y):
        return Rock()


class Nothing:
    def __init__(self):
        self.key = 'n'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if neighbors[Fish().key] == 3:
            return Fish()
        elif neighbors[Shrimp().key] == 3:
            return Shrimp()
        else:
            return Nothing()
