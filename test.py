from life import CLife

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

def Test1():
    s = [
    ['f', 'f'],
    ['f', 's']]

    f = [
    ['f', 'f'],
    ['f', 'f']]

    Test(s, f, 2)

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

def TestAll():
    Test1()
    Test2()
    Test3()

