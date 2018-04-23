from life import Life


class Test:
    tests = []

    @staticmethod
    def run():
        for i in range(len(Test.tests)):
            print("run test", i)
            Test.tests[i]()
            print("test", i, "done")
        print("all tests done")


def test(f):
    Test.tests.append(f)
    return f


def check(game, arr, n, m):
    for i in range(n):
        for j in range(m):
            if game.get(i, j) != arr[i][j]:
                print(i, j)
                print(game.map)
                print(arr)
                assert(game.get(i, j) == arr[i][j])


def set(game, arr, n, m):
    for i in range(n):
        for j in range(m):
            game.set(arr[i][j], i, j)


def play_testing(start, finish, k):
    n = len(start)
    m = len(start[0])
    game = Life(n, m)
    set(game, start, n, m)
    game.play(k)
    check(game, finish, n, m)


@test
def test_set_get():
    game = Life(3, 3)

    game.set('f', 1, 2)
    assert (game.get(1, 2) == 'f')


@test
def test_play_1():
    s = [
        ['f', 'f'],
        ['f', 's']]

    f = [
        ['f', 'f'],
        ['f', 'f']]

    play_testing(s, f, 2)


@test
def test_play_2():
    s = [
        ['f', 'f', 'f'],
        ['r', 'n', 'n'],
        ['s', 's', 's']]

    f = [
        ['n', 'f', 'n'],
        ['r', 'f', 'n'],
        ['n', 's', 'n']]
    play_testing(s, f, 1)


@test
def test_play_3():
    s = [
        ['s', 's', 's'],
        ['r', 'r', 'r'],
        ['s', 's', 's']]

    f = [
        ['n', 's', 'n'],
        ['r', 'r', 'r'],
        ['n', 's', 'n']]

    play_testing(s, f, 1)


@test
def test_next():
    s = [
        ['s', 's', 's'],
        ['r', 'n', 'r'],
        ['s', 's', 's']]

    f = [
        ['n', 's', 'n'],
        ['r', 'n', 'r'],
        ['n', 's', 'n']]

    game = Life(3, 3)
    set(game, s, 3, 3)
    game.next()
    check(game, f, 3, 3)


@test
def test_fish():
    s = [
        ['f', 'n', 'r', 'f', 'n', 'n', 'n', 'n', 'n'],
        ['f', 'n', 'r', 'f', 'f', 'n', 'n', 'f', 'f'],
        ['f', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n']]

    f = [
        ['n', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n'],
        ['f', 'f', 'r', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n']]

    play_testing(s, f, 1)


@test
def test_shrimp():
    s = [
        ['s', 'n', 'r', 's', 'n', 'n', 'n', 'n', 'n'],
        ['s', 'n', 'r', 's', 's', 'n', 'n', 's', 's'],
        ['s', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n']]

    f = [
        ['n', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n'],
        ['s', 's', 'r', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n']]

    play_testing(s, f, 1)


@test
def test_nothing_and_rock():
    s = [
        ['f', 'n', 's', 'r', 'f', 'f', 'n', 's', 's'],
        ['f', 'n', 's', 'r', 'f', 'n', 'n', 'n', 's'],
        ['f', 'n', 's', 'r', 'f', 'n', 'n', 'n', 'n']]

    f = [
        ['n', 'n', 'n', 'r', 'f', 'f', 'n', 's', 's'],
        ['f', 'f', 's', 'r', 'f', 'n', 'n', 's', 's'],
        ['n', 'n', 'n', 'r', 'n', 'n', 'n', 'n', 'n']]

    play_testing(s, f, 1)
