from _ast import arg
from typing import Any, Type

import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import test_input_argument, test_card_correct


def test_get_mask_card_number(test_input_argument:list[Any],test_card_correct:str) -> None:
    """Тест на срабатывание функции при введении номера карты"""
    assert get_mask_card_number(test_input_argument) == test_card_correct


"""Параметризация функции get_mask_card_number"""
@pytest.mark.parametrize(
    "value,expected",
    [
        ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
        ('', 'Ошибка ввода'),],)

def test_get_mask_card_number_different_data(value: str, expected: str) -> None:
    """Тест на срабатывание функции при введении различных некоректных данных"""
    assert get_mask_card_number(value) == expected


def test_get_mask_account(test_mask_account,test_result_account) -> None:
    assert get_mask_account(test_mask_account) == test_result_account


@pytest.mark.parametrize(
    "value,expected",
    [
        ("", "Не верный ввод данных"),("Счет 64686473678894779589", "Счет **9589")
        ])

def test_get_mask_account_different_data(value: str, expected: str) -> None:
    """Тест на срабатывание функции при введении различных некоректных данных"""
    assert get_mask_account(value) == expected
