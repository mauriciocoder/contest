import src.woodcutters as src


def test_get_max_trees_cut():
    assert (
        src.get_max_trees_cut(
            [
                [7, 12],
                [10, 2],
                [12, 2],
                [15, 1],
                [19, 2],
                [20, 1],
                [53, 25],
                [63, 10],
                [75, 12],
                [87, 1],
            ]
        )
        == 9
    )
