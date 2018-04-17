from collections import defaultdict
import animals


class Life:
    values = {animals.Fish(), animals.Nothing(),
              animals.Shrimp(), animals.Rock()}
    val_by_keys = {u.key: u for u in values}

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = [[None]*m for i in range(n)]

    def set(self, c, x, y):
        assert(c in Life.val_by_keys)
        self.map[x][y] = Life.val_by_keys[c]

    def get(self, x, y):
        return self.map[x][y].key

    def next(self):
        new_map = [[None]*self.m for i in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                new_map[i][j] = self.map[i][j].get_updated(self, i, j)
        self.map = new_map

    def play(self, turns):
        for i in range(turns):
            self.next()

    def get_neighbors(self, x, y):
        res = defaultdict(int)

        for xn in range(x-1, x+2):
            for yn in range(y-1, y+2):
                if 0 <= xn < self.n and 0 <= yn < self.m and (xn, yn) != (x, y):
                    res[self.map[xn][yn].key] += 1

        return res

