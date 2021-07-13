from src.drinks import get_orange_fraction


def test_get_orange_fraction():
    assert get_orange_fraction(3, (50, 50, 100)) == 66.66666666666666
