import pytest
from datetime import date
from decimal import Decimal, getcontext, setcontext

from calculate_price import calculate_price



def test_calculate_price_1():
    assert calculate_price(Decimal("50.00"), date(2022, 4, 9)) == Decimal("47.50")


def test_calculate_price_2():
    assert calculate_price(Decimal("100.00"), date(2022, 4, 10)) == Decimal("90.00")


def test_calculate_price_3():
    assert calculate_price(Decimal("100.01"), date(2022, 4, 18)) == Decimal("85.00")


def test_calculate_price_4():
    assert calculate_price(Decimal("0.01"), date(2022, 4, 8)) == Decimal("0.01")


def test_calculate_price_5():
    assert calculate_price(Decimal("50.01"), date(2022, 1, 1)) == Decimal("50.01")


def test_calculate_price_6():
    assert calculate_price(Decimal("200.00"), date(2022, 5, 5)) == Decimal("200")


def test_calculate_price_7():
    assert calculate_price(Decimal("50.00"), date(2022, 4, 19)) == Decimal("50.00")


def test_calculate_price_8():
    assert calculate_price(Decimal("100.00"), date(2022, 4, 20)) == Decimal("100.00")


def test_calculate_price_9():
    assert calculate_price(Decimal("100.01"), date(2022, 4, 21)) == Decimal("100.01")


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
    assert calculate_price(Decimal("100.09999"), date(2022, 4, 9)) == Decimal("85.07")


def test_calculate_price_14():
    assert calculate_price(Decimal("100.09999"), date(2022, 4, 20)) == Decimal("100.09")


def test_calculate_price_15():
    assert calculate_price(Decimal("0.00"), date(2022, 4, 11)) == Decimal("0")


def test_calculate_price_16():
    assert calculate_price(Decimal("20"), date(2022, 4, 12)) == Decimal("19")


def test_calculate_price_17():
    assert calculate_price(Decimal("50.01"), date(2022, 4, 17)) == Decimal("45.00")


def test_calculate_price_18():
    assert calculate_price(Decimal("70"), date(2022, 4, 16)) == Decimal("63")


def test_calculate_price_19():
    assert calculate_price(Decimal("120"), date(2022, 4, 18)) == Decimal("102")


def test_calculate_price_20():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(120.09999, date(2022, 4, 9))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError