import sys
from typing import Iterable


def get_my_range(n: int) -> Iterable[int]:
    print("#### 1")
    counter: int = 0
    while counter < n:
        print("#### 2")
        yield counter
        print("#### 3")
        counter += 1


print("### before instantiating")
my_range: Iterable[int] = get_my_range(5)
print("### after instantiating")
print(type(my_range))

print("### before loop")
for i in my_range:
    print("### before reading")
    print(f"i = {i}")
    print("### after reading")
