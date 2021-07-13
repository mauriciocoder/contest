import src.new_year_candles as src


def test_burn():
    status: dict = {"candles": 2, "burned": 0, "hours": 0}
    expected_status: dict = {"candles": 0, "burned": 2, "hours": 2}
    src.burn(status)
    assert status == expected_status


def test_build_1():
    burned_needed: int = 2
    status: dict = {"candles": 2, "burned": 3, "hours": 0}
    expected_status: dict = {"candles": 3, "burned": 1, "hours": 0}
    src.build(status, burned_needed)
    assert status == expected_status


def test_build_2():
    burned_needed: int = 1
    status: dict = {"candles": 2, "burned": 3, "hours": 0}
    expected_status: dict = {"candles": 5, "burned": 0, "hours": 0}
    src.build(status, burned_needed)
    assert status == expected_status


def test_build_3():
    burned_needed: int = 4
    status: dict = {"candles": 2, "burned": 3, "hours": 0}
    expected_status: dict = {"candles": 2, "burned": 3, "hours": 0}
    src.build(status, burned_needed)
    assert status == expected_status


def test_build_4():
    burned_needed: int = 2
    status: dict = {"candles": 0, "burned": 2, "hours": 0}
    expected_status: dict = {"candles": 1, "burned": 0, "hours": 0}
    src.build(status, burned_needed)
    assert status == expected_status


def test_get_hours_with_light():
    hours_with_light: int = src.get_hours_with_light(4, 2)
    assert 7 == hours_with_light
    hours_with_light: int = src.get_hours_with_light(6, 3)
    assert 8 == hours_with_light
