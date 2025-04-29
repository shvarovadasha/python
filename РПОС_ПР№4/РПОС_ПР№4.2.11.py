
# Выполнил: Шварова Д.С.
# Группа: МС-32



def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.

    Результат:
        str: измененная строка."""
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    letter_count = len(letters)

    def shift_char(char, shift):
        if char.isalpha():
            idx = letters.index(char.lower())
            new_idx = (idx + shift) % letter_count
            new_char = letters[new_idx]
            return new_char.upper() if char.isupper() else new_char
        else:
            return char

    return ''.join(shift_char(char, shift) for char in text)

text = input("Введите предложение: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift)
print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++
