from life import Life


class Test:
    tests = []

    @staticmethod
    def run():
        for i in range(len(Test.tests)):
            print("run test", Test.tests[i].__name__)
            Test.tests[i]()
            print("test", Test.tests[i].__name__, "done")
        print("all tests done")


def test(func):
    Test.tests.append(func)
    return func


def check_game(game, expected_map, height, width):
    for i in range(height):
        for j in range(width):
            if game.get(i, j) != expected_map[i][j]:
                print(i, j)
                print(game.map)
                print(expected_map)
                assert(game.get(i, j) == expected_map[i][j])


def set_game(game, arr, height, width):
    for i in range(height):
        for j in range(width):
            game.set(arr[i][j], i, j)


def play_testing(game_map, result, k):
    height = len(game_map)
    width = len(game_map[0])
    game = Life(height, width)
    set_game(game, game_map, height, width)
    game.play(k)
    check_game(game, result, height, width)


@test
def test_set_get():
    game = Life(3, 3)

    game.set('f', 1, 2)
    assert (game.get(1, 2) == 'f')


@test
def test_fish_1():
    game_map = [
        ['f', 'n'],
        ['f', 'n']]

    result = [
        ['n', 'n'],
        ['n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_fish_2():
    game_map = [
        ['f', 'f', 'n'],
        ['f', 'f', 'f']]

    result = [
        ['f', 'n', 'f'],
        ['f', 'n', 'f']]

    play_testing(game_map, result, 1)


@test
def test_fish_3():
    game_map = [
        ['f', 'f', 'f']]

    result = [
        ['n', 'f', 'n']]

    play_testing(game_map, result, 1)


@test
def test_shrimp_1():
    game_map = [
        ['s', 'n'],
        ['s', 'n']]

    result = [
        ['n', 'n'],
        ['n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_shrimp_2():
    game_map = [
        ['s', 's', 'n'],
        ['s', 's', 's']]

    result = [
        ['s', 'n', 's'],
        ['s', 'n', 's']]

    play_testing(game_map, result, 1)


@test
def test_shrimp_3():
    game_map = [
        ['s', 's', 'n'],
        ['s', 's', 's']]

    result = [
        ['s', 'n', 's'],
        ['s', 'n', 's']]

    play_testing(game_map, result, 1)


@test
def test_nothing_1():
    game_map = [
        ['s', 'n', 'f'],
        ['s', 'n', 'f'],
        ['s', 'n', 'f']]

    result = [
        ['n', 'n', 'n'],
        ['s', 'f', 'f'],
        ['n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_nothing_2():
    game_map = [
        ['s', 's', 'f'],
        ['s', 'n', 'f'],
        ['s', 'f', 'f']]

    result = [
        ['s', 's', 'n'],
        ['s', 'n', 'f'],
        ['n', 'f', 'f']]

    play_testing(game_map, result, 1)


@test
def test_nothing_3():
    game_map = [
        ['n', 's', 'n'],
        ['n', 'n', 's'],
        ['s', 'n', 'n']]

    result = [
        ['n', 'n', 'n'],
        ['n', 's', 'n'],
        ['n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_nothing_4():
    game_map = [
        ['n', 's', 'n'],
        ['n', 'n', 's'],
        ['f', 'n', 'f']]

    result = [
        ['n', 'n', 'n'],
        ['n', 'n', 'n'],
        ['n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_rock():
    game_map = [
        ['n', 's', 'r'],
        ['r', 's', 'n'],
        ['r', 's', 'n']]

    result = [
        ['n', 'n', 'r'],
        ['r', 's', 's'],
        ['r', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_play_1():
    game_map = [
        ['f', 'f'],
        ['f', 's']]

    result = [
        ['f', 'f'],
        ['f', 'f']]

    play_testing(game_map, result, 2)


@test
def test_play_2():
    game_map = [
        ['f', 'f', 'f'],
        ['r', 'n', 'n'],
        ['s', 's', 's']]

    result = [
        ['n', 'f', 'n'],
        ['r', 'f', 'n'],
        ['n', 's', 'n']]
    play_testing(game_map, result, 1)


@test
def test_play_3():
    game_map = [
        ['s', 's', 's'],
        ['r', 'r', 'r'],
        ['s', 's', 's']]

    result = [
        ['n', 's', 'n'],
        ['r', 'r', 'r'],
        ['n', 's', 'n']]

    play_testing(game_map, result, 1)


@test
def test_play_4():
    game_map = [
        ['f', 'n', 'r', 'f', 'n', 'n', 'n', 'n', 'n'],
        ['f', 'n', 'r', 'f', 'f', 'n', 'n', 'f', 'f'],
        ['f', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n']]

    result = [
        ['n', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n'],
        ['f', 'f', 'r', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'r', 'f', 'f', 'n', 'n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_play_5():
    game_map = [
        ['s', 'n', 'r', 's', 'n', 'n', 'n', 'n', 'n'],
        ['s', 'n', 'r', 's', 's', 'n', 'n', 's', 's'],
        ['s', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n']]

    result = [
        ['n', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n'],
        ['s', 's', 'r', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'r', 's', 's', 'n', 'n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_play_6():
    game_map = [
        ['f', 'n', 's', 'r', 'f', 'f', 'n', 's', 's'],
        ['f', 'n', 's', 'r', 'f', 'n', 'n', 'n', 's'],
        ['f', 'n', 's', 'r', 'f', 'n', 'n', 'n', 'n']]

    result = [
        ['n', 'n', 'n', 'r', 'f', 'f', 'n', 's', 's'],
        ['f', 'f', 's', 'r', 'f', 'n', 'n', 's', 's'],
        ['n', 'n', 'n', 'r', 'n', 'n', 'n', 'n', 'n']]

    play_testing(game_map, result, 1)


@test
def test_next():
    game_map = [
        ['s', 's', 's'],
        ['r', 'n', 'r'],
        ['s', 's', 's']]

    result = [
        ['n', 's', 'n'],
        ['r', 'n', 'r'],
        ['n', 's', 'n']]

    game = Life(3, 3)
    set_game(game, game_map, 3, 3)
    game.next_generation()
    check_game(game, result, 3, 3)
