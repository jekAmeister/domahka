def filter_by_state(inform_state: list, state_clue: object = "EXECUTED") -> list:
    """Функция которая принимает на вход список словарей и значение для ключа
    state(опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение."""

    list_state = []

    for key in inform_state:
        if key.get("state") == state_clue:
            list_state.append(key)
    return list_state


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(dictionaries: list, reverse: bool = True) -> list:
    """Функция функцию, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date)"""
    return sorted(dictionaries, key=lambda dictionary: dictionary["date"], reverse=True)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
