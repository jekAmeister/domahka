import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions: list[dict], test_result_filter_by_currency: list[dict]) -> None:
    """Тест на срабатывание функции при введении корректных данных"""
    assert list(filter_by_currency(test_transactions)) == list(test_result_filter_by_currency)


@pytest.fixture
def fixture() -> list[str]:
    return ["shared fixture"]


@pytest.mark.parametrize(
    "arg,expected",
    [
        ("test_filter_by_currency_incorrect_data", "Список транзакций пуст"),
        ("test_transactions_wrong", "Операции в заданной валюте не найдены"),
    ],
)
def test(arg: str, expected: str, fixture: list[dict]) -> None:
    """Тест на срабатывание функции при введении данных в другой валюте и пустом списке транзакции"""
    with pytest.raises(AttributeError):
        assert list(filter_by_currency(fixture, arg)) == expected


def test_transaction_descriptions(
    test_transactions: list[dict], test_result_transaction_descriptions: list[dict]
) -> None:
    """Тест на срабатывание функции при введении корректных данных"""
    assert list(transaction_descriptions(test_transactions)) == list(test_result_transaction_descriptions)


#
def test_transaction_descriptions_incorrect_data(
    test_different_input_data: list[dict], test_result_different_input_data: list[dict]
) -> None:
    with pytest.raises(AssertionError):
        """Тест на срабатывание функции при введении пустого списка"""
        assert list(transaction_descriptions(test_different_input_data)) == list(test_result_different_input_data)


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator(start: int, stop: int, expected_numbers: list[str]) -> None:
    """Тест на срабатывание функции при введении корректных данных"""
    number = list(card_number_generator(1, 5))
    assert number == expected_numbers


def test_card_number_generator_1() -> None:
    """Тест на срабатывание функции"""
    number = list(card_number_generator(9999999999999988, 9999999999999999))
    assert number == number


def test_card_number_generator_2() -> None:
    """Тест на срабатывание функции"""
    number = list(card_number_generator(9999999999123456, 9999999999999999))
    assert number == number


def test_card_number_generator_3() -> None:
    """Тест на срабатывание функции"""
    number = list(card_number_generator(9999999999999991, 9999999999999999))
    assert number == number
