
# Выполнил: Шварова Д.С.
# Группа: МС-32



LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_base(number, base):
    """Преобразовать десятичное число 'number' в с.с. 'base'.

    Параметры:
        number (int): десятичное число;
        base (int): система счисления.

    Результат:
        str: число в с.с. 'base'."""
    if number == 0:
        return "0"

    digits = []
    while number > 0:
        remainder = number % base
        if remainder < 10:
            digits.append(str(remainder))  # от 0 до 9
        else:
            digits.append(LETTERS_EX[remainder])  # от A до F
        number //= base

    return ''.join(digits[::-1])


def from_base(number, base):
    """Преобразовать число в с.с. 'base' в десятичное число.
    Результат:
        int: число в 10-й с.с."""
    number = number.upper()
    result = 0
    for i, digit in enumerate(number[::-1]):
        if digit.isdigit():
            value = int(digit)
        else:
            value = DIGITS_EX[digit]
        result += value * (base ** i)

    return result

decimal_number = 34
base = 16

#из 10-й системы в 16-ю
converted = to_base(decimal_number, base)
print(f"{decimal_number} в 16-й системе: {converted}")

# из 16-й системы в 10-ю
converted_back = from_base(converted, base)
print(f"{converted} в 10-й системе: {converted_back}")
# --------------
# Пример вывода:
#
# Нет
