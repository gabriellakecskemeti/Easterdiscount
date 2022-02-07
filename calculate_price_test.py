import pytest
from datetime import date
from decimal import Decimal, getcontext, setcontext

from chocolate import calculate_price

_test_data_during_easter_holidays = [
    pytest.param(Decimal("50.00"), date(2022, 4, 9), Decimal("47.50"), id="1: discount 5%"),
    pytest.param(Decimal("100.00"), date(2022, 4, 10), Decimal("90.00"), id="2: discount 10%"),
    pytest.param(Decimal("100.01"), date(2022, 4, 18), Decimal("85.01"), id="3: 15% discount"),
    pytest.param(Decimal("100.09999"), date(2022, 4, 9), Decimal("85.08"), id="13: truncation"),
    pytest.param(Decimal("0"), date(2022, 4, 11), Decimal("0"), id="15: boundari 0, in period"),
    pytest.param(Decimal("20"), date(2022, 4, 12), Decimal("19"), id="16: 5% discount"),
    pytest.param(Decimal("50.01"), date(2022, 4, 17), Decimal("45.01"), id="17: 10% discount"),
    pytest.param(Decimal("70"), date(2022, 4, 16), Decimal("63"), id="18: 10% discount"),
    pytest.param(Decimal("120"), date(2022, 4, 18), Decimal("102"), id="19: 15% discount"),
    pytest.param(Decimal("0"), date(2022, 4, 9), Decimal("0"), id="21: 0 on first day")]


@pytest.mark.parametrize("total,day,expected", _test_data_during_easter_holidays)
def test_prices_during_easter_holidays(total: Decimal, day: date, expected: Decimal):
    # Act
    actual = calculate_price(total, day)
    # Assert
    assert actual == expected


_test_data_outside_easter_holidays = [
    pytest.param(Decimal("0.01"), date(2022, 4, 8), Decimal("0.01"), id="4: first tear"),
    pytest.param(Decimal("50.01"), date(2021, 4, 10), Decimal("50.01"), id="5:last year, second tier"),
    pytest.param(Decimal("200.00"), date(2022, 5, 5), Decimal("200"), id="6:third tier"),
    pytest.param(Decimal("50.00"), date(2022, 4, 19), Decimal("50.00"), id="7:first tier"),
    pytest.param(Decimal("100"), date(2022, 4, 20), Decimal("100.00"), id="8:second tier"),
    pytest.param(Decimal("100.01"), date(2022, 4, 21), Decimal("100.01"), id="9:third tier"),
    pytest.param(Decimal("100.09999"), date(2022, 4, 20), Decimal("100.09"), id="14: truncation")]


@pytest.mark.parametrize("total,day,expected", _test_data_outside_easter_holidays)
def test_prices_during_easter_holidays(total: Decimal, day: date, expected: Decimal):
    # Act
    actual = calculate_price(total, day)
    # Assert
    assert actual == expected


_invalid_test_data = [
    pytest.param("x", date(2022, 4, 9), "Given total must be of type Decimal.", id="10: total is not decimal"),
    pytest.param(Decimal("-100.00"), date(2022, 4, 10), "Given total must be positive or zero", id="11: negativ amount"),
    pytest.param(Decimal("100"), "xx/xx/xxxx", "Given day must be of type date", id="12: wrong date"),
    pytest.param(120.09999, date(2022, 4, 9), "Given total must be of type Decimal.", id="20: float instead of decimal")
]


@pytest.mark.parametrize("total,day,my_expected", _invalid_test_data)
def test_invalid_arguments(total: Decimal, day: date, my_expected: str):
    with pytest.raises(ValueError) as exception_info:
        calculate_price(total, day)
    assert str(exception_info.value) == my_expected
    assert exception_info.type == ValueError


def test_calculate_price_10():
    with pytest.raises(ValueError) as exception_info:
        calculate_price("x", date(2022, 4, 9))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError


def test_calculate_price_11():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(Decimal(-100.00), date(2022, 4, 10))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError


def test_calculate_price_12():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(Decimal("100"), "xx/xx/xxxx")
    assert str(exception_info.value) == "Given day must be of type date"
    assert exception_info.type == ValueError


# def test_calculate_price_15():
#    assert calculate_price(Decimal("0.00"), date(2022, 4, 11)) == Decimal("0")


# def test_calculate_price_16():
#    assert calculate_price(Decimal("20"), date(2022, 4, 12)) == Decimal("19")


# def test_calculate_price_17():
#    assert calculate_price(Decimal("50.01"), date(2022, 4, 17)) == Decimal("45.00")


# def test_calculate_price_18():
#    assert calculate_price(Decimal("70"), date(2022, 4, 16)) == Decimal("63")


# def test_calculate_price_19():
#    assert calculate_price(Decimal("120"), date(2022, 4, 18)) == Decimal("102")


def test_calculate_price_20():
    with pytest.raises(ValueError) as exception_info:
        calculate_price(120.09999, date(2022, 4, 9))
    assert str(exception_info.value) == "The total given is not of type Decimal or negativ"
    assert exception_info.type == ValueError
