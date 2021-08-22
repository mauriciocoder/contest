import src.cheap_travel as src


def test_find_minimum_cost():
    assert src.find_minimum_cost(6, 2, 1, 2) == 6
    assert src.find_minimum_cost(5, 2, 2, 3) == 8
    assert src.find_minimum_cost(3, 3, 1, 4) == 3
    assert src.find_minimum_cost(1, 1, 1, 1) == 1
    assert src.find_minimum_cost(10, 3, 1, 2) == 7
    assert src.find_minimum_cost(10, 3, 5, 1) == 4
    assert src.find_minimum_cost(9, 3, 3, 10) == 27
    assert src.find_minimum_cost(1, 1000, 1, 2) == 1
