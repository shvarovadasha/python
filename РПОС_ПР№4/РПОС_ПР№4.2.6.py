
# Выполнил: Шварова Д.С.
# Группа: МС-32

import math

def gcd(first, second):
    """Вернуть НОД целых чисел 'first' и 'second'."""
    return math.gcd(first, second)


def lcm(first, second):
    """Вернуть НОК целых чисел 'first' и 'second'."""
    return abs(first * second) // math.gcd(first, second)


def gcd_nums(nums):
    """Вернуть НОД чисел из списка 'nums'.

    Параметры:
       nums (list of int)

    Результат:
        int
    """
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result


def lcm_nums(nums):
    """Вернуть НОК чисел из списка 'nums'.

    Параметры:
         nums (list of int)

    Результат:
         int
    """
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result


nums = list(map(int, input("Введите числа через пробел: ").split()))

gcd_result = gcd_nums(nums)
lcm_result = lcm_nums(nums)

print(f"НОД = {gcd_result}")
print(f"НОК = {lcm_result}")

# --------------
# Пример вывода:
#
# Введите числа через пробел: 8 10 14
# НОД = 2
# НОК = 280
#
# Введите числа через пробел: 6 8 24 16
# НОД = 2
# НОК = 48
