# https://codeforces.com/problemset/problem/1409/B


def minimum_product(
    num1: int, num2: int, num1_limit: int, num2_limit: int, allowed_operations: int
) -> int:
    """Generate the minimun product for the folowing parameters num1, num2
    Args:
        num1 (int): first number
        num2 (int): second number
        num1_limit (int): minimum limit for first number
        num2_limit (int): minimum limit for first number
        allowed_operations (int): amount of reductions allowed
    Returns:
        int: the minimum amount of operations
    """
    if num1 < num1_limit or num2 < num2_limit:
        raise AssertionError("Number below the limit, check arguments")

    allowed_operations_num1: int = num1 - allowed_operations
    if allowed_operations_num1 < num1_limit:
        allowed_operations_num1 = num1 - num1_limit

    allowed_operations_num2: int = num2 - allowed_operations
    if allowed_operations_num2 < num2_limit:
        allowed_operations_num2 = num2 - num2_limit

    num1_minimum_reached: int = 0
    num1_minimum_reached = (
        num1 - allowed_operations_num1
        if allowed_operations_num1 < allowed_operations
        else num1 - allowed_operations
    )
    num2_minimum_reached: int = 0
    num2_minimum_reached = (
        num2 - allowed_operations_num2
        if allowed_operations_num2 < allowed_operations
        else num2 - allowed_operations
    )
    prioritize_num1: bool = num1_minimum_reached <= num2_minimum_reached

    while allowed_operations > 0:
        if prioritize_num1:
            if allowed_operations_num1 > 0:
                num1 -= 1
                allowed_operations_num1 -= 1
            if allowed_operations_num1 == 0:
                prioritize_num1 = False
        if not prioritize_num1:
            if allowed_operations_num2 > 0:
                num2 -= 1
                allowed_operations_num2 -= 1
            if allowed_operations_num2 == 0:
                prioritize_num1 = True
        allowed_operations -= 1
    return num1 * num2
