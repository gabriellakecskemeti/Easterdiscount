import pytest
from datetime import date
import decimal

from calculate_price import calculate_price


def test_calculate_price_1():
    assert calculate_price(50.00, date(2022, 4, 9)) == decimal(47.50)


def test_calculate_price_2():
    assert calculate_price(100.00, date(2022, 4, 10)) == decimal(90.00)


def test_calculate_price_3():
    assert calculate_price(100.01, date(2022, 4, 18)) == decimal(85.00)


def test_calculate_price_4():
    assert calculate_price(0.01, date(2022, 4, 8)) == decimal(0.01)


def test_calculate_price_5():
    assert calculate_price(50.01, date(2022, 1, 1)) == decimal(50.01)


def test_calculate_price_6():
    assert calculate_price(200.00, date(2022, 5, 5)) == decimal(200.00)


def test_calculate_price_7():
    assert calculate_price(50.00, date(2022, 4, 19)) == decimal(50.00)


def test_calculate_price_8():
    assert calculate_price(100.01, date(2022, 4, 21)) == decimal(100.01)


def test_calculate_price_9():
    assert calculate_price(50.00, date(2022, 4, 9)) == decimal(50.00)


def test_calculate_price_10():
    with pytest.raises(ValueError) as exception_info:
        calculate_price("x", date(2022, 4, 9))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError


def test_calculate_price_11():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(-100.00, date(2022, 4, 10))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError


def test_calculate_price_12():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(100, "xx/xx/xxxx")
    assert str(exception_info.value) == "The day given is not of type date"
    assert exception_info.type == ValueError


def test_calculate_price_13():
    assert calculate_price(100.09999, date(2022, 4, 9)) == decimal(85.07)


def test_calculate_price_14():
    assert calculate_price(100.09999, date(2022, 4, 20)) == decimal(100.09)

