def get_mask_card_number(new_card: str) -> str:
    """Функция которая маскирует номер банковской карты"""

    if 16 < len(new_card) < 31:
        text = new_card[-10:-5]
        new_number = "*" * 6
        new_mask_card = new_card.replace(text, new_number)

        old_number = (
            new_mask_card[:-18],
            new_mask_card[-17:-13],
            new_mask_card[-13:-9],
            new_mask_card[-9:-5],
            new_mask_card[-4:],
        )
        result_masking_card = " ".join(old_number)
        return result_masking_card
    else:
        return "Ошибка ввода"


# print(get_mask_card_number("Maestro 1596837868705199"))


def get_mask_account(checking: str) -> str:
    """Функция которая маскирует номер банковского счета"""
    if 20 < len(checking) < 26:

        old_number = checking[-20:-4]
        new_number = "*" * 2
        new_checking = checking.replace(old_number, new_number)

        old_account = (new_checking[:-21], new_checking[-21:])

        result_masking_account = "".join(old_account)
        return result_masking_account
    else:
        return "Не верный ввод данных"


# print(get_mask_account("Счет 64686473678894712456"))


if __name__ == "__masks__":

    assert get_mask_card_number("Visa Platinum 8990922113665229") == "Visa Platinum  8990 92** **** 5229"

    assert get_mask_account("Счет 64686473678894779589") == "Счет **9589"
