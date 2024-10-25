#
def get_mask_card_number(new_card: str) -> str:
    """Функция которая маскирует номер банковской карты"""
    text = new_card[-10:-5]
    new_number = "*" * 6
    new_mask_card = new_card.replace(text, new_number)

    old_number = (
        new_mask_card[:-17],
        new_mask_card[-17:-13],
        new_mask_card[-13:-9],
        new_mask_card[-9:-5],
        new_mask_card[-4:],
    )

    return " ".join(old_number)


def get_mask_account(checking: str) -> str:
    """Функция которая маскирует номер банковского счета"""
    old_number = checking[-20:-4]
    new_number = "*" * 2
    new_checking = checking.replace(old_number, new_number)

    old_account = (new_checking[:-21], new_checking[-21:])

    return " ".join(old_account)
