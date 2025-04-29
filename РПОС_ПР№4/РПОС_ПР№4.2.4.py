
# Выполнил: Шварова Д.С.
# Группа: мс-32



def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        .

    Результат:
        bool: True - да, False - нет.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def previous_date(day, month, year):
    if day > 1:
        day -= 1
    else:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = days(month, year)
    return day, month, year

def next_date(day, month, year):
    if day < days(month, year):
        day += 1
    else:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year


day, month, year = map(int, input("День, месяц, год через пробел: ").split())

prev_d, prev_m, prev_y = previous_date(day, month, year)
next_d, next_m, next_y = next_date(day, month, year)
print(f"Предыдущий день: {prev_d:02}/{prev_m:02}/{prev_y}")
print(f"Следующий день: {next_d:02}/{next_m:02}/{next_y}")
# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: 29/02/2000
# Следующий день: 02/03/2000
