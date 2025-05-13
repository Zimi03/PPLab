import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (2, 1, 1)])
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (2, 3, 6), (5, 3, 15)])
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    result == expected


@pytest.mark.parametrize("a, b, expected", [(2, 2, 1), (4, 2, 2), (6, 3, 2)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected
