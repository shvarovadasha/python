# Выполнил: Шварова Д.С.
# Группа: МС-32



def avg(data):
    """Вернуть среднее значение 'data'.

    Параметры:
         data (list of int): чистый список темп

    Результат:
        float: ср знач
    """
    return sum(data) / len(data)


def cleared_data(data):
    """Вернуть список без значений None.

    Параметры:
        data (list): список с темп и None

    Результат:
        list
    """
    return [x for x in data if x is not None]


n = int(input("Кол-во измерений: "))
data = []
for i in range(n):
    val = input(f"Измерение {i+1}-е: ")
    if val == "-":
        data.append(None)
    else:
        data.append(int(val))

clean = cleared_data(data)
average = avg(clean)

print(f"Средняя температура: {average:.2f}")
# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00
