import src.minimum_product as src


def test_minimum_product():
    assert src.minimum_product(10, 10, 8, 5, 3) == 70
    assert src.minimum_product(12, 8, 8, 7, 2) == 77
    assert src.minimum_product(12343, 43, 4543, 39, 123212) == 177177
    assert src.minimum_product(1000000000, 1000000000, 1, 1, 1) == 999999999000000000
    # assert src.minimum_product(1000000000, 1000000000, 1, 1, 1000000000) == 999999999
    assert src.minimum_product(10, 11, 2, 1, 5) == 55
    assert src.minimum_product(10, 11, 9, 1, 10) == 10
