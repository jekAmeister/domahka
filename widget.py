from src.masks import get_mask_card_number, get_mask_account


def account_card_disguise(string: str) -> any:

    ''' Функция которая маскирует номер карты и счета '''

    if 'Счет' in string:

        return get_mask_account(string)
    else:
        return get_mask_card_number(string)


print(account_card_disguise
      ('Visa Platinum 8990922113665229'))


def get_data(data_string:str) -> str:
    ''' Функция преобразования даты '''


    data_conversion = (
    data_string[-18:-16],
    data_string[-22:-18],
    data_string[:-22])

    return "".join(data_conversion)


print(get_data('2018-07-11T02:26:18.671407'))

