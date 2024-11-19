import pytest

@pytest.fixture
def card_number():
    return '7000792289606361'

@pytest.fixture
def mask_account():
    return "73654108430135874305"

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
def test_answer():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def card_disguise():
    return "Visa Platinum  8990 92** **** 5229"


@pytest.fixture
def data_conversion():
    return "11-07-2018"
