
# Выполнил: Шварова Д.С.
# Группа: МС-32

import re

def has_digits(sentence):
    """Проверяет, содержит ли предложение хотя бы одну цифру."""
    return bool(re.search(r'\d', sentence))


def sentences_with_digits_count(sentences):
    """Возвращает количество предложений, содержащих хотя бы одну цифру."""
    count = 0
    for sentence in sentences:
        if has_digits(sentence):
            count += 1
    return count


n = int(input("Введите количество предложений: "))
sentences = []

for i in range(1, n + 1):
    sentence = input(f"Введите предложение №{i}:\n")
    sentences.append(sentence)

result = sentences_with_digits_count(sentences)

print(f"Предложений с цифрой = {result}")
# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1
