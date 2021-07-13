# https://codeforces.com/problemset/problem/200/B
from functools import reduce


def get_orange_fraction(drinks_qty: int, fractions: tuple) -> float:
    total_fractions: float = reduce(
        lambda x, y: x + y, map(lambda x: x / 100, fractions)
    )
    return (total_fractions / drinks_qty) * 100
