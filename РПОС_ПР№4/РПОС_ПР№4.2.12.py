
# Выполнил: Шварова Д.С.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]

def vacant_compartments(data):
    """Вернуть список полностью свободных купе. Нумерация купе идет с 1."""
    return [i + 1 for i, compartment in enumerate(data) if all(value is None for value in compartment.values())]


def vacant_seats(data, compartments_condition=None, seat_condition=None):
    """Вернуть список свободных мест при соблюдении условий 'compartments_condition' и 'seat_condition'."""
    result = []
    for i, compartment in enumerate(data):
        if compartments_condition and not compartments_condition(compartment):
            continue
        for seat, value in compartment.items():
            if seat_condition and seat_condition(seat, value):
                result.append((i + 1, seat))
    return result

def is_same_sex_and_vacant(compartment, sex):
    """Вернуть True, если в купе 'compartment' есть хотя бы одно свободное место,
    а все остальные заняты только пассажирами указанного пола 'sex'."""

    if any(value is None for value in compartment.values()):
        return all(value == sex or value is None for value in compartment.values())
    return False

# cписок полностью свободных купе
print(vacant_compartments(data))  # [5, 7]
# cписок свободных мест в вагоне
print(vacant_seats(data))  # [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (7, 4), (8, 3), (9, 2), (9, 3)]
# cписок свободных нижних мест (места с нечетными номерами)
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 0))  # [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# cписок свободных верхних мест (места с четными номерами)
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 == 0))  # [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# cписок свободных мест в купе с исключительно мужской компанией
print(vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "м")))  # [(5, 1), (5, 3), (6, 1), (6, 3), (7, 1), (7, 3), (9, 1), (9, 3)]
# cписок свободных мест в купе с исключительно женской компанией
print(vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "ж")))  # [(8, 3)]

# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]
