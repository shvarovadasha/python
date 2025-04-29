direction = input("Выберите направление (encrypt/decrypt): ").strip()
language = input("Выберите язык алфавита (en/ru): ").strip()
shift = int(input("Введите шаг сдвига: "))
text = input("Введите текст: ")

if language == 'ru':
    lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upper = lower.upper()
    alphabet_size = 32
else:
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    alphabet_size = 26

if direction == 'decrypt':
    shift = -shift

result = ''
for char in text:
    if char in lower:
        idx = lower.index(char)
        new_idx = (idx + shift) % alphabet_size
        result += lower[new_idx]
    elif char in upper:
        idx = upper.index(char)
        new_idx = (idx + shift) % alphabet_size
        result += upper[new_idx]
    else:
        result += char

print("Результат:", result)
