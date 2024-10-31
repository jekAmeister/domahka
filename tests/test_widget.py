import pytest


from src.widget import account_card_disguise,get_data

def test_account_card_disguise():
    assert account_card_disguise("Visa Platinum 8990922113665229") == "Visa Platinum  8990 92** **** 5229"

def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11-07-2018"