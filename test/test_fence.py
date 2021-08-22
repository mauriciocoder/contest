import src.fence as src


def test_get_min_heights_sum_index():
    assert src.get_min_heights_sum_index(3, [1, 2, 6, 1, 1, 7, 1]) == 3
    assert src.get_min_heights_sum_index(3, [1, 2, 6, 1, 1, 1, 1]) == 4
    assert src.get_min_heights_sum_index(3, [1, 2, 6, 2, 1, 1, 1]) == 5
