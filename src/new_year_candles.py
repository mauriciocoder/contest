# https://codeforces.com/problemset/problem/379/A
# {'candles': 0, 'burned': 0, 'hours': 0}


def burn(status: dict):
    candles: int = status["candles"]
    if candles > 0:
        status["candles"] = 0
        status["burned"] += candles
        status["hours"] += candles


def build(status: dict, burned_needed: int):
    burned: int = status["burned"]
    if burned >= burned_needed:
        status["candles"] = status["candles"] + burned // burned_needed
        status["burned"] = burned % burned_needed


# TODO - Change access to dictionary from bracket to dot
def get_hours_with_light(candles_qty: int, burned_needed: int) -> int:
    status: dict = {"candles": candles_qty, "burned": 0, "hours": 0}
    while status["candles"] > 0:
        burn(status)
        build(status, burned_needed)
    return status["hours"]
