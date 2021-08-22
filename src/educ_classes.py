class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year


c: Car = Car("Ford", 2020)
print(f"c.model = {c.model}")
