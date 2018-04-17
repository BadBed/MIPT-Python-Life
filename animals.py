class Fish:
    def __init__(self):
        self.key = 'f'

    def get_updated(self, life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Fish().key] <= 3:
            return Fish()
        else:
            return Nothing()


class Shrimp:
    def __init__(self):
        self.key = 's'

    def get_updated(self, life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Shrimp().key] <= 3:
            return Shrimp()
        else:
            return Nothing()


class Rock:
    def __init__(self):
        self.key = 'r'

    def get_updated(self, life, x, y):
        return Rock()


class Nothing:
    def __init__(self):
        self.key = 'n'

    def get_updated(self, life, x, y):
        neighbors = life.get_neighbors(x, y)
        if neighbors[Fish().key] == 3:
            return Fish()
        elif neighbors[Shrimp().key] == 3:
            return Shrimp()
        else:
            return Nothing()
