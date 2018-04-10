class CFish:
    def __init__(self):
        self.key = 'f'

    def GetUpdated(self, life, x, y):
        neighbors = life.GetNeighbors(x, y)
        if 2 <= neighbors[CFish().key] <= 3:
            return CFish()
        else:
            return CNothing()

class CShrimp:
    def __init__(self):
        self.key = 's'

    def GetUpdated(self, life, x, y):
        neighbors = life.GetNeighbors(x, y)
        if 2 <= neighbors[CShrimp().key] <= 3:
            return CShrimp()
        else:
            return CNothing()


class CRock:
    def __init__(self):
        self.key = 'r'

    def GetUpdated(self, life, x, y):
        return CRock()


class CNothing:
    def __init__(self):
        self.key = 'n'

    def GetUpdated(self, life, x, y):
        neighbors = life.GetNeighbors(x, y)
        if neighbors[CFish().key] == 3:
            return CFish()
        elif neighbors[CShrimp().key] == 3:
            return CShrimp()
        else:
            return CNothing()
