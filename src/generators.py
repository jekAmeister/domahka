from typing import Any

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


# for x in filter_by_currency(transactions):
#
#     print(x)
x=filter_by_currency(transactions)

print(next(x))
print(next(x))
#
#
# def transaction_descriptions(transactions: list[dict]) -> Any:
#     """Генератор который принимает список словарей с транзакциями
#     и возвращает описание каждой операции по очереди."""
#     for x in transactions:
#         if x.get("description"):
#             yield x["description"]
#
#
# # for x in transaction_descriptions(transactions):
# #     print(x)
# x = transaction_descriptions(transactions)
# print(next(x))
# print(next(x))
# print(next(x))
#
# def card_number_generator(start: int, stop: int) -> Any:
#     """Функция которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты.
#     Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
#      Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
#     for number in range(start, stop + 1):
#         number_str = "0" * (16 - len(str(number))) + str(number)
#         old_number = number_str[:4] + " " + number_str[4:8] + " " + number_str[8:12] + " " + number_str[12:16]
#         result = old_number
#         yield result
#
#
# for x in card_number_generator(1, 5):
#     print(x)
#
#
# if __name__ == "__generators__":
#
#     assert filter_by_currency(transactions) == next(x)
#     assert transaction_descriptions(transactions) == next(x)
#     assert card_number_generator(1, 5) == next(x)
