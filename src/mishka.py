# https://codeforces.com/problemset/problem/703/A


def get_result(mishkaScore: int, chrisScore: int) -> bool:
    """returns M if mishka won, C if Chris w    on and D if draw."""
    if mishkaScore > chrisScore:
        return "M"
    if mishkaScore < chrisScore:
        return "C"
    return "D"


if __name__ == "__main__":
    rounds: int = int(input(""))
    mishkaWons: int = 0
    chrisWons: int = 0
    for i in range(0, rounds):
        scores: list = list(map(lambda score: int(score), input("").split(" ")))
        result: str = get_result(scores[0], scores[1])

        if result == "M":
            mishkaWons += 1
        elif result == "C":
            chrisWons += 1
    if mishkaWons > chrisWons:
        print("Mishka")
    elif mishkaWons < chrisWons:
        print("Chris")
    else:
        print("Friendship is magic!^^")
