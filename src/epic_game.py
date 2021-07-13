def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    highest: int = a if a > b else b
    gcd_num: int = 1
    for i in range(1, highest):
        if a % i == 0 and b % i == 0:
            gcd_num = i
    return gcd_num


def play(simon_stones: int, antisimon_stones: int, heap_stones: int) -> int:
    heap = heap_stones
    winner = 0
    while heap > 0:
        to_be_removed = gcd(simon_stones, heap)
        if to_be_removed <= heap:
            heap -= to_be_removed
            winner = 0
        to_be_removed = gcd(antisimon_stones, heap)
        if to_be_removed <= heap:
            heap -= to_be_removed
            winner = 1
    return winner
