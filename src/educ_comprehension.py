from typing import List

if __name__ == "__main__":
    numbers = [1, 1, 2, 3, 4]
    new_numbers = [number * 2 for number in numbers]
    print(new_numbers)

    set_comprehension = {number * 2 for number in numbers}
    print(set_comprehension)

    name = "Mauricio Lopes Bonetti"
    tokens = [char.upper() for char in name]
    print(tokens)
