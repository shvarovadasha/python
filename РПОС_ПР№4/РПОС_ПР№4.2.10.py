
# Выполнил: Шварова Д.С.
# Группа: МС-32

from collections import Counter

def sentence_stats(sentence):
    """Вернуть символьную статистику 'sentence'. Регистр не учитывается.
    """
    sentence = sentence.lower()
    return dict(Counter(sentence))


s = s = input("Введите предложение: ")
stats = sentence_stats(s)
print(stats)
# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}
