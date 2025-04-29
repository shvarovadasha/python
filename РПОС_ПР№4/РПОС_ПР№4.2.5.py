
# Выполнил: Шварова Д.С.
# Группа: МС-32



def is_leap(year):
    """Является ли 'year' високосным годом?

    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.
    """
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def another_date(day, month, year, delta=1):
    """Вернуть день, месяц, год, отличающийся на 'delta' дней.
    """

    def previous_date(day, month, year):
        if day > 1:
            return day - 1, month, year
        else:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            return days(month, year), month, year

    def next_date(day, month, year):
        if day < days(month, year):
            return day + 1, month, year
        else:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
            return day, month, year

    for _ in range(abs(delta)):
        if delta > 0:
            day, month, year = next_date(day, month, year)
        else:
            day, month, year = previous_date(day, month, year)

    return day, month, year

day, month, year = map(int, input("День, месяц, год через пробел: ").split())
delta = int(input("Сдвиг (может быть отрицательным): "))

new_day, new_month, new_year = another_date(day, month, year, delta)
print(f"Новый день: {new_day:02d}/{new_month:02d}/{new_year}")
# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000
