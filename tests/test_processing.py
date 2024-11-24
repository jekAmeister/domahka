from src.processing import filter_by_state,sort_by_date
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



def test_sort_by_date(test_list_by_state,test_execution)->None:
    """Тест для проверки функции которая сортирует список словарей по параметру date, если даты одинаковые"""
    assert sort_by_date(test_list_by_state) == test_execution


@pytest.fixture
def fixture():
   return ["shared fixture"]

@pytest.mark.parametrize("arg,expected", [('by_state_stan','"state" not found'),('test_by_state_stan', '"state" not found')])
def test(arg, expected,fixture):
    """Тест на срабатывание функции при введении данных с ошибкой"""
    assert filter_by_state(fixture,arg) == expected