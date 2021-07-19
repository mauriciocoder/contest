import src.free_icecream as src


def test_get_eod_result():
    assert src.get_eod_result(7, [5, -10, -20, 40, -20]) == (22, 1)
    assert src.get_eod_result(17, [-16, -2, -98, 100, -98]) == (3, 2)
