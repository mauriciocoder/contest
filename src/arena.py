# https://codeforces.com/problemset/problem/1487/A


def get_possible_winners(player_levels) -> int:
    player_levels = sorted(player_levels)
    possible_winners: int = 0
    weaker: int = player_levels[0]
    for player_level in player_levels:
        if player_level > weaker:
            possible_winners += 1
    return possible_winners


if __name__ == "__main__":
    test_cases: int = int(input(""))
    results: list = []
    for i in range(test_cases):
        players: int = int(input(""))
        player_levels: list = input("").split(" ")
        results.append(get_possible_winners(player_levels))
    for i in range(test_cases):
        print(results[i])
