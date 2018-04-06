from collections import defaultdict

class CLife:
    NOTHING = 'n'
    FISH = 'f'
    ROCK = 'r'
    SHRIMP = 's'
    good_values = {NOTHING, FISH, ROCK, SHRIMP}
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = [[None]*m for i in range(n)]

    def Set(self, value, x, y):
        if value in CLife.good_values:
            self.map[x][y] = value
        else:
            assert(False)

    def Get(self, x, y):
        return self.map[x][y]

    def Next(self):
        new_map = [[None]*self.m for i in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                new_map[i][j] = self.GetUpdated(i, j)
        self.map = new_map

    def Play(self, turns):
        for i in range(turns):
            self.Next()

    def GetNeighbors(self, x, y):
        res = defaultdict(int)

        for xn in range(x-1, x+2):
            for yn in range(y-1, y+2):
                if 0 <= xn < self.n and 0 <= yn < self.m and (xn, yn) != (x, y):
                    res[self.map[xn][yn]] += 1

        return res

    def GetUpdated(self, x, y):
        neighbors = self.GetNeighbors(x, y)
        now = self.map[x][y]
        if now == CLife.ROCK:
            return CLife.ROCK
        elif now == CLife.FISH:
            if neighbors[CLife.FISH] >= 2 and neighbors[CLife.FISH] <= 3:
                return CLife.FISH
            else:
                return CLife.NOTHING
        elif now == CLife.SHRIMP:
            if neighbors[CLife.SHRIMP] >= 2 and neighbors[CLife.SHRIMP] <= 3:
                return CLife.SHRIMP
            else:
                return CLife.NOTHING
        elif now == CLife.NOTHING:
            if neighbors[CLife.FISH] == 3:
                return CLife.FISH
            elif neighbors[CLife.SHRIMP] == 3:
                return CLife.SHRIMP
            else:
                return CLife.NOTHING
