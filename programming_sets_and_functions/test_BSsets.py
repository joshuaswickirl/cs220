import pytest
from BSsets import *

stringn_td = [(2, 1, "11"), (4, "Go", "GoGoGoGo")]


@pytest.mark.parametrize("n,c,expected", stringn_td)
def test_stringn(n, c, expected):
    r = stringn(n, c)
    assert r == expected


next_td = [("00000", 5, "00001"), ("01011", 5, "01100"), ("11111", 5, "00000")]


@pytest.mark.parametrize("bs,n,expected", next_td)
def test_next(bs, n, expected):
    r = next(bs, n)
    assert r == expected


s11x1_td = [
    (2, {"01", "11"}),
    (3, {"001", "011", "101", "110", "111"}),
    (
        4,
        {
            "0001",
            "0011",
            "0101",
            "0111",
            "1001",
            "1011",
            "1100",
            "1101",
            "1110",
            "1111",
        },
    ),
]


@pytest.mark.parametrize("n, expected", s11x1_td)
def test_s11x1(n, expected):
    r = s11x1(n)
    assert r == expected


s11x_td = [
    (2, {"11"}),
    (3, {"110", "111"}),
    (4, {"1100", "1101", "1110", "1111",},),
]


@pytest.mark.parametrize("n, expected", s11x_td)
def test_s11x(n, expected):
    r = s11x(n)
    assert r == expected


sx1_td = [
    (2, {"01", "11"}),
    (3, {"001", "011", "101", "111"}),
    (4, {"0001", "0011", "0101", "0111", "1001", "1011", "1101", "1111",},),
]


@pytest.mark.parametrize("n, expected", sx1_td)
def test_sx1(n, expected):
    r = sx1(n)
    assert r == expected
