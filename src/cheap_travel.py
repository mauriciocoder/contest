# https://codeforces.com/problemset/problem/466/A
import math


def find_minimum_cost(
    rides: int, rides_in_set_ticket: int, one_ride_price: int, set_ticket_price: int
) -> int:
    set_tickets_needed: int = rides // rides_in_set_ticket
    one_ride_tickets_needed: int = rides - (set_tickets_needed * rides_in_set_ticket)

    if (
        set_ticket_price / rides_in_set_ticket
    ) > one_ride_price or set_ticket_price > one_ride_price * rides:
        return rides * one_ride_price
    else:
        if set_tickets_needed == 0:
            return set_ticket_price
        if set_ticket_price < one_ride_price:
            return int(math.ceil(rides / rides_in_set_ticket)) * set_ticket_price
        return (set_tickets_needed * set_ticket_price) + (
            one_ride_tickets_needed * one_ride_price
        )


if __name__ == "__main__":
    entry = input("").split(" ")
    entry_int = [int(x) for x in entry]
    print(find_minimum_cost(entry_int[0], entry_int[1], entry_int[2], entry_int[3]))
