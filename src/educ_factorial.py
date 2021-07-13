from functools import reduce
from typing import Iterable


def factorial() -> Iterable[int]:
    counter: int = 1
    while True:
        yield reduce(lambda x, y: x * y, range(1, counter), 1)
        counter += 1


if __name__ == "__main__":
    fat: Iterable[int] = factorial()
    print(next(fat))
    print(next(fat))
    print(next(fat))
    print(next(fat))
    print(next(fat))
    print(next(fat))
