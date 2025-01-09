
from typing import Any
from string import digits
from random import choices

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {},
    {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Any:
    """Функция которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for x in transactions:
        if x.get("operationAmount") and x["operationAmount"]["currency"]["code"] == currency:
            yield x


x = filter_by_currency(transactions)
# print(x)

print(next(x))
print(next(x))


def transaction_descriptions(transactions: list[dict]) -> Any:
    '''Генератор который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.'''
    for x in transactions:
        if x.get("description"):
            yield x["description"]


x = transaction_descriptions(transactions)

# print(x)
print(next(x))
print(next(x))
print(next(x))




def card_number_generator():
    cc_digits = choices(digits, k=16)
    cc_number = "".join(cc_digits)
    old_number = cc_number[:4] + " " + cc_number[4:8] + " " + cc_number[8:12] + " " + cc_number[12:16]
    yield old_number

x = card_number_generator()
print(next(x))



if __name__ == "__generators__":
    assert filter_by_currency(transactions) == next(x)
    assert transaction_descriptions(transactions) == next(x)
    assert card_number_generator() == next(x)

    # assert transaction_descriptions(transactions) == Перевод организации
