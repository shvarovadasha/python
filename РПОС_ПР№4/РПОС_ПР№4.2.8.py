
# Выполнил: Шварова Д.С.
# Группа: МС-32



def print_with_border(string, char):
    """Рисует рамку вокруг строки из символа char."""

    border = char * (len(string) + 2)

    print(border)
    print(f"{char}{string}{char}")
    print(border)

s = input("Введите строку: ")
k = input("Введите символ: ")

print_with_border(s, k)
# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++
