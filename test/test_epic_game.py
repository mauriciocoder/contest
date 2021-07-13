import src.epic_game as src


def test_gdc():
    assert src.gcd(6, 9) == 3
    assert src.gcd(5, 0) == 5
    assert src.gcd(0, 5) == 5
    assert src.gcd(3, 7) == 1


def test_play():
    assert src.play(3, 5, 9) == 0
    assert src.play(1, 1, 100) == 1
