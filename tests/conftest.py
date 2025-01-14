from random import choices

import pytest

@pytest.fixture
def test_mask_account():
    return "Счет 64686473678894779589"

@pytest.fixture
def test_result_account():
    return 'Счет **9589'

@pytest.fixture
def test_list_by_state():
    return  [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},]

@pytest.fixture
def test_correct_answer():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def by_state_stan():
    return [
            { "date"},
            { "date"},
            { "date"},
            { "date"}]

@pytest.fixture
def test_empty_list():
    return '"state" not found'



@pytest.fixture
def by_incorrect_data_state():
    return [
            { "date": "2019-07-03T18:35:29.512364"},
            { "date": "2018-06-30T02:08:58.425572"},
            { "date": "2018-09-12T21:27:25.241689"},
            { "date": "2018-10-14T08:21:33.419441"}]




@pytest.fixture
def test_execution():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def test_card_correct():
    return "Visa Platinum 8990 92** **** 5229"


@pytest.fixture
def test_input_argument():
    return "Visa Platinum 8990922113665229"

@pytest.fixture
def test_data_conversion():
    return "11-07-2018"

@pytest.fixture
def test_input_data():
    return "2018-07-11T02:26:18.671407"

@pytest.fixture
def test_list_adaptations():
    return 'test_input_argument','test_mask_account'

@pytest.fixture
def test_list_answer():
    return 'test_card_correct','test_result_account'

@pytest.fixture
def test_transactions():
    return [
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

@pytest.fixture
def test_transactions_wrong():
    return [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
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
        "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

@pytest.fixture
def test_result_filter_by_currency():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572','operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
            {'id': 142264269, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878','operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]

@pytest.fixture
def test_filter_by_currency_incorrect_data():
    return []


@pytest.fixture
def test_different_input_data():
    return []


@pytest.fixture
def test_result_transaction_descriptions():
    return ['Перевод организации',
           'Перевод со счета на счет',
           'Перевод со счета на счет']


@pytest.fixture
def test_result_different_input_data():
    return 'Список описания транзакций пуст'


@pytest.fixture
def test_expected_numbers():
    return ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
            ]

@pytest.fixture
def test_expected_numbers_incorrect_data():
    return []

@pytest.fixture
def test_expected_numbers_input_data():
    return 'Список пуст'