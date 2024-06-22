from src.masks import get_mask_card_number, get_mask_account


def account_card_disguise(string: str) -> any:
    if 'Счет' in string:
        return get_mask_account(string)
    else:
        return get_mask_card_number(string)


print(account_card_disguise('Visa Platinum 8990922113665229'))




