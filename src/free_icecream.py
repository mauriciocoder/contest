# https://codeforces.com/problemset/problem/686/A


def get_eod_result(packs_qty: int, people_ice_cream: list) -> tuple:
    frustrated_people_qty: int = 0
    remaining_packs_qty: int = packs_qty
    for person_ice_cream in people_ice_cream:
        # print(f'person ice cream = {person_ice_cream}')
        if person_ice_cream < 0:
            if abs(person_ice_cream) > remaining_packs_qty:
                frustrated_people_qty += 1
            else:
                remaining_packs_qty -= person_ice_cream * -1
        else:
            remaining_packs_qty += person_ice_cream
    return (remaining_packs_qty, frustrated_people_qty)


if __name__ == "__main__":
    first_entry = input("").split(" ")
    # print(first_entry)
    first_entry_int = [int(x) for x in first_entry]
    # print(first_entry_int)
    people = first_entry_int[0]
    packs_qty = first_entry_int[1]

    people_ice_cream = []
    # print(people)
    for people in range(people):
        # print('reading:')
        line = input("").split(" ")
        ice_cream = int(line[1])
        if line[0] == "-":
            ice_cream *= -1
        people_ice_cream.append(ice_cream)
    result = get_eod_result(packs_qty, people_ice_cream)
    print(result[0], result[1])
