#
# Выполнил: Шварова Д.С.
# Группа: МС-32



def sgn(x):

    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

x = float(input("Введите x: "))
y = float(input("Введите y: "))

numerator = sgn(x) + y**2
denominator = sgn(y) - abs(x)**0.5

if denominator == 0:
    print("Ошибка: деление на ноль.")
else:
    z = numerator / denominator
    print("Ответ:", round(z, 2))

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33
