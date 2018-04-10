from collections import defaultdict
import animals


class CLife:
    values = {animals.CFish(), animals.CNothing(),
              animals.CShrimp(), animals.CRock()}
    val_by_keys = {u.key: u for u in values}

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = [[None]*m for i in range(n)]

    def Set(self, c, x, y):
        assert(c in CLife.val_by_keys)
        self.map[x][y] = CLife.val_by_keys[c]

    def Get(self, x, y):
        return self.map[x][y].key

    def Next(self):
        new_map = [[None]*self.m for i in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                new_map[i][j] = self.map[i][j].GetUpdated(self, i, j)
        self.map = new_map

    def Play(self, turns):
        for i in range(turns):
            self.Next()

    def GetNeighbors(self, x, y):
        res = defaultdict(int)

        for xn in range(x-1, x+2):
            for yn in range(y-1, y+2):
                if 0 <= xn < self.n and 0 <= yn < self.m and (xn, yn) != (x, y):
                    res[self.map[xn][yn].key] += 1

        return res

