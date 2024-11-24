import pytest

from src.widget import mask_account_card,get_data

def test_mask_account_card(test_input_argument: str,test_card_correct: str)-> str:
    """Тест на срабатывание функции при введении номера карты"""
    assert mask_account_card(test_input_argument) == test_card_correct

def test_mask_account_card_1(test_mask_account,test_result_account):
    """Тест на срабатывание функции при введении номера карты"""
    assert mask_account_card(test_mask_account) == test_result_account

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Ошибка данных"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 15968378","Ошибка данных"),
        ("Maestro 1596837868705199","Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658","Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229","Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353","Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(input_data,expected_output) -> None:
    """Тест на срабатывание функции при введении номера карты"""
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_date,expected_output",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2023-06-15T10:30:45.123456", "15.06.2023"),
    ],
)
def test_get_data(input_date,expected_output)-> None:
    assert get_data(input_date) == expected_output







