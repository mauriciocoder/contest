import src.collecting_packages as src


def test_sort_path():
    path: list = [(3, 2), (3, 1), (2, 2), (1, 3)]
    assert src.sort_path(path) == [(1, 3), (2, 2), (3, 1), (3, 2)]
    path = [(5, 2), (5, 3), (3, 3), (2, 3)]
    assert src.sort_path(path) == [(2, 3), (3, 3), (5, 2), (5, 3)]


def test_move_to():
    assert src.move_to((1, 1), (2, 2)) == "RU"
    assert src.move_to((1, 1), (2, 3)) == "RUU"
    assert src.move_to((1, 1), (3, 4)) == "RRUUU"
    assert src.move_to((3, 1), (2, 2)) is None


def test_collect_package():
    assert src.collect_package([(1, 3), (1, 2), (3, 3), (5, 5), (4, 3)]) == "RUUURRRRUU"
    assert src.collect_package([(1, 0), (0, 1)]) is None
    assert src.collect_package([(4, 3)]) == "RRRRUUU"
