from typing import Iterable


def fibonnaci() -> Iterable[int]:
    current, previous = 1, 0
    while True:
        current, previous = current + previous, current
        yield current


if __name__ == "__main__":
    fib: Iterable[int] = fibonnaci()
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
