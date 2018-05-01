class Animal:
    @staticmethod
    def get_updated(life, x, y):
        assert(False)


class Fish(Animal):
    id = 'f'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Fish().id] <= 3:
            return Fish()
        else:
            return Nothing()


class Shrimp(Animal):
    id = 's'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if 2 <= neighbors[Shrimp().id] <= 3:
            return Shrimp()
        else:
            return Nothing()


class Rock(Animal):
    id = 'r'

    @staticmethod
    def get_updated(life, x, y):
        return Rock()


class Nothing(Animal):
    id = 'n'

    @staticmethod
    def get_updated(life, x, y):
        neighbors = life.get_neighbors(x, y)
        if neighbors[Fish().id] == 3:
            return Fish()
        elif neighbors[Shrimp().id] == 3:
            return Shrimp()
        else:
            return Nothing()
