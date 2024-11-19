from src.processing import filter_by_state
import pytest

def test_filter_by_state(test_list_by_state,test_correct_answer) -> None:
    """Тест на срабатывание функции при введении корректных данных"""
    assert filter_by_state(test_list_by_state) == test_correct_answer


@pytest.fixture
def fixture():
   return ["shared fixture"]

@pytest.mark.parametrize("arg,expected", [('by_incorrect_data_state','"state" not found'),('test_by_state_stan', '"state" not found')])
def test(arg, expected,fixture):
    """Тест на срабатывание функции при введении данных с ошибкой"""
    assert filter_by_state(fixture,arg) == expected












# def test_sort_by_date(by_date: list, reverse: bool = True) -> None:
#     assert sort_by_date([
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]) == by_date