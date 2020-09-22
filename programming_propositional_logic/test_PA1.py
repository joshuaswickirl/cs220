import pytest
from PA1 import iif, make_tt_ins


make_tt_ins_data = [
    (1, [[False], [True]]),
    (2, [[False, False], [False, True], [True, False], [True, True]]),
    (
        3,
        [
            [False, False, False],
            [False, False, True],
            [False, True, False],
            [False, True, True],
            [True, False, False],
            [True, False, True],
            [True, True, False],
            [True, True, True],
        ],
    ),
]


@pytest.mark.parametrize("n, expected", make_tt_ins_data)
def test_make_tt_ins(n, expected):
    r = make_tt_ins(n)
    assert r == expected
