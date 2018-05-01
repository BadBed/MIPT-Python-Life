from collections import defaultdict
import animals as module_animals


class Life:
    animals = {a() for a in module_animals.Animal.__subclasses__()}
    animal_by_id = {a.id: a for a in animals}

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [[None]*width for i in range(height)]

    def set(self, id, x, y):
        assert(id in Life.animal_by_id)
        self.map[x][y] = Life.animal_by_id[id]

    def get(self, x, y):
        return self.map[x][y].id

    def next_generation(self):
        new_map = [[None]*self.width for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                new_map[i][j] = self.map[i][j].get_updated(self, i, j)
        self.map = new_map

    def play(self, turns):
        for i in range(turns):
            self.next_generation()

    def get_neighbors(self, x, y):
        result = defaultdict(int)

        for neighbor_x in range(x-1, x+2):
            for neighbor_y in range(y-1, y+2):
                if 0 <= neighbor_x < self.height and \
                        0 <= neighbor_y < self.width and\
                        (neighbor_x, neighbor_y) != (x, y):
                    result[self.map[neighbor_x][neighbor_y].id] += 1

        return result
