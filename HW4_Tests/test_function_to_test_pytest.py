from functions_to_test import *
import pytest

NUM1 = 2
NUM2 = 4
ZERO = 0


@pytest.fixture
def calc():
    return Calculator


def test_add(calc):
    assert calc.add(NUM1, NUM2) == 6


def test_multiply(calc):
    result = calc.multiply(NUM1, NUM2)
    assert result == 8


def test_subtract(calc):
    assert calc.subtract(NUM2, NUM1) == 2


def test_divide(calc):
    assert calc.divide(NUM2, NUM1) == 2


def test_zero_division(calc):
    with pytest.raises(ValueError):
        calc.divide(NUM1, ZERO)

