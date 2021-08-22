# https://codeforces.com/problemset/problem/363/B
import sys


def get_min_heights_sum_index(planks_qty: int, planks_heights: list) -> int:
    minimun_height: int = sys.maxsize
    starting_index: int = -1
    limit: int = len(planks_heights) - planks_qty + 1
    range_1 = range(limit)
    for i in range_1:
        height: int = 0
        range_2 = range(planks_qty)
        for j in range_2:
            height += planks_heights[i + j]
        if height < minimun_height:
            starting_index = i
            minimun_height = height
    return starting_index + 1


if __name__ == "__main__":
    first_line = input("").split(" ")
    planks_qty: int = int(first_line[1])
    planks_heights: list = list(map(lambda x: int(x), input("").split(" ")))
    print(get_min_heights_sum_index(planks_qty, planks_heights))
