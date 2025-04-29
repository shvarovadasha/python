
# Выполнил: Шварова Д.С.
# Группа: МС-32



def is_lucky(num):
    """Является ли 'num' номером счастливого билета?

    Параметры:
        num (int)

    Результат:
        bool: True - да, False - нет.
    """
    even = 0
    odd = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even == odd


def lucky_numbers(a, b):
    """Вернуть список счастливых номеров от 'a' до 'b'.

    Параметры:
         a (int) начальный номер (включительно)
         b (int) конечный

    Результат:
        list of int
    """
    return [i for i in range(a, b + 1) if is_lucky(i)]

a = int(input("Первый номер билета: "))
b = int(input("Последний номер билета: "))

lucky = lucky_numbers(a, b)
print(*lucky)

# --------------
# Пример вывода:
#
# Первый номер билета: 10
# Последний номер билета: 25
# 10 12 14 16 18 21 23 25
