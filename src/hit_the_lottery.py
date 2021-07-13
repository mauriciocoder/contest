# https://codeforces.com/problemset/problem/996/A


def minimum_bills(money: int, bills: tuple):
    bills_qty = 0
    sorted_bills = sorted(bills, reverse=True)
    money_left = money
    for bill in sorted_bills:
        if money_left >= bill:
            bills_used = money_left // bill
            bills_qty += bills_used
            money_left -= bills_used * bill
        if money_left == 0:
            break

    return bills_qty


if __name__ == "__main__":
    money = int(input("Money: "))
    print(minimum_bills(money, (1, 5, 10, 20, 100)))
