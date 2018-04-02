from collections import Counter
from collections import defaultdict

class CLife:
    NOTHING = 'n'
    FISH = 'f'
    ROCK = 'r'
    SHRIMP = 's'
    good_values = {NOTHING, FISH, ROCK, SHRIMP}
    DX = [1, 1, 1, 0, -1, -1, -1, 0]
    DY = [1, 0, -1, -1, -1, 0, 1, 1]
    def __init__(this, n, m):
        this.n = n
        this.m = m
        this.map = [[None]*m for i in range(n)]

    def Set(this, value, x, y):
        if value in CLife.good_values:
            this.map[x][y] = value
        else:
            assert(False)

    def Get(this, x, y):
        return this.map[x][y]

    def Next(this):
        new_map = [[None]*this.m for i in range(this.n)]

        for i in range(this.n):
            for j in range(this.m):
                new_map[i][j] = this.GetUpdated(i, j)
        this.map = new_map

    def Play(this, turns):
        for i in range(turns):
            this.Next()

    def GetNeighbors(this, x, y):
        res = defaultdict(int)

        for i in range(8):
            xn = x + CLife.DX[i]
            yn = y + CLife.DY[i]
            if xn >= 0 and xn < this.n and yn < this.m and yn >= 0:
                res[this.map[xn][yn]] += 1

        return res

    def GetUpdated(this, x, y):
        neighbors = this.GetNeighbors(x, y)
        now = this.map[x][y]
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
