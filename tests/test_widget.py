import pytest


from src.widget import account_card_disguise,get_data

def test_account_card_disguise(card_disguise):
    assert account_card_disguise("Visa Platinum 8990922113665229") == card_disguise


def test_get_data(data_conversion):
    assert get_data("2018-07-11T02:26:18.671407") == data_conversion