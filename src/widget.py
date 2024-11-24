from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_argument: str) -> str:
    if "Счет" in input_argument:
        return get_mask_account(input_argument)
    elif 16 < len(input_argument) < 31:
        return get_mask_card_number(input_argument)
    else:
        return "Ошибка данных"


# print(mask_account_card("Maestro 15968378"))


def get_data(date_str: str) -> str:
    """Функция преобразует строку из формата 2018-07-11T02:26:18.671407 в формат 11.07.2018"""
    date_part = date_str.split("T")[0]  # Разделяем строку по символу "T"
    year, month, day = date_part.split("-")  # Разделяем дату через "-"
    return f"{day}.{month}.{year}"  # Возвращаем строку в нужном формате


# print(get_data("2023-06-15T10:30:45.123456"))

if __name__ == "__widget__":
    assert mask_account_card("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert get_data("2018-07-11T02:26:18.671407") == "11-07-2018"
