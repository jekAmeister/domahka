# Проект "Домашняя работа"

## Описание:

Проект "Домашняя работа" - это веб-приложение на Python для маскировки счетов банковских счетов,карт и сортировки данных.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:jekAmeister/domahka.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

## Тестирование:

1.Чтобы установить pytest, используйте команды:
'''
poetry add --group dev pytest
'''

2.Пример результатов тестирования:
'''
(domahka-py3.13) PS C:\Users\User\Downloads\domahka> pytest
test session starts 
platform win32 -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\User\Downloads\domahka
configfile: pyproject.toml
plugins: cov-6.0.0
collected 23 items                                            

tests\test_masks.py ......                              [ 26%]
tests\test_processing.py ....                           [ 43%]
tests\test_widget.py .............                      [100%]

===================== 23 passed in 0.09s =====================
(domahka-py3.13) PS C:\Users\User\Downloads\domahka>
'''


3.Тестирование функций filter_by_currency,transaction_descriptions,card_number_generator:

Для запуска тестирования и вывода результатов по покрытию тестами в формате html,
надо в терминале ввести команду pytest --cov=src --cov report html, таким образом
вы получите отчет по тестированию функций во всей папке src, отчет будет сгенерирован
в папке htmlcov`

3.1 Пример результатов тестирования.
platform win32 -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\User\Downloads\domahka
configfile: pyproject.toml
plugins: cov-6.0.0
collected 32 items                                                                                                               

tests\test_generators.py .........                                                                                         [ 28%]
tests\test_masks.py ......                                                                                                 [ 46%]
tests\test_processing.py ....                                                                                              [ 59%]
tests\test_widget.py .............                                                                                         [100%]

---------- coverage: platform win32, python 3.13.0-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\generators.py             29      3    90%
src\masks.py                  22      2    91%
src\processing.py             17      3    82%
src\widget.py                 14      2    86%
tests\__init__.py              0      0   100%
tests\conftest.py             74     12    84%
tests\test_generators.py      30      0   100%
tests\test_masks.py           16      0   100%
tests\test_processing.py      18      2    89%
tests\test_widget.py          12      1    92%
----------------------------------------------
TOTAL                        232     25    89%

Этот проект является простым инструментом для обработки данных и может быть расширен дополнительными функциями по мере необходимости.




