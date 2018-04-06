from life import CLife

class CTest:
    tests = []
    def Run():
        for i in range(len(CTest.tests)):
            print("run test", i)
            CTest.tests[i]()
        print("success")

def test(f):
    CTest.tests.append(f)
    return f

def Check(game, arr, n, m):
    for i in range(n):
        for j in range(m):
            assert(game.Get(i, j) == arr[i][j])

def Set(game, arr, n, m):
    for i in range(n):
        for j in range(m):
            game.Set(arr[i][j], i, j)

def Test(start, finish, k):
    n = len(start)
    m = len(start[0])
    game = CLife(n, m)
    Set(game, start, n, m)
    game.Play(k)
    Check(game, finish, n, m)

@test
def Test1():
    s = [
    ['f', 'f'],
    ['f', 's']]

    f = [
    ['f', 'f'],
    ['f', 'f']]

    Test(s, f, 2)

@test
def Test2():
    s = [
    ['f', 'f', 'f'],
    ['r', 'n', 'n'],
    ['s', 's', 's']]

    f = [
    ['n', 'f', 'n'],
    ['r', 'f', 'n'],
    ['n', 's', 'n']]
    Test(s, f, 1)

@test
def Test3():
    s = [
    ['s', 's', 's'],
    ['r', 'r', 'r'],
    ['s', 's', 's']]

    f = [
    ['n', 's', 'n'],
    ['r', 'r', 'r'],
    ['n', 's', 'n']]

    Test(s, f, 1)

@test
def TestNext():
    s = [
    ['s', 's', 's'],
    ['r', 'n', 'r'],
    ['s', 's', 's']]

    f = [
    ['n', 's', 'n'],
    ['r', 'n', 'r'],
    ['n', 's', 'n']]

    game = CLife(3, 3)
    Set(game, s, 3, 3)
    game.Next()
    Check(game, f, 3, 3)

@test
def TestSetGet():
    game = CLife(4, 4)
    assert(game.Get(1, 1) == None)
    game.Set('f', 1, 2)
    assert (game.Get(1, 2) == 'f')
