
# Выполнил: Шварова Д.С.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте значения 'votes', при необходимости измените его для
# проверки правильности решения

votes = [
    2, 3, -1, 2, 5, 1, 1, 4, 1, 1, 1, 3, 1, 3, 5, -1, 5, 2, 5, 5,
    3, 3, 2, 3, 3, 2, 2, 1, 3, 2, 5, 2, 2, 4, 1, 1, 3, 2, 2, 3, 3,
    3, 1, 4, 2, 1, 4, 2, 3, 3, 3, -1, 5, 3, 1, 4, 5, 1, 1, 3, 3,
    3, -1, 5, 3, 3, 2, 5, 1, 1, 5, -1, 1, 2, 2, 3, -1, 4, 2, 5, 4,
    2, -1, 3, 1, 4, 3, 5, 4, 1, 5, 3, 2, 4, 2, 1, 3, 4, 1, 1, 3, 4
]

parties = {
    1: "Партия №1", 2: "Партия №2", 3: "Партия №3",
    4: "Партия №4", 5: "Партия №5", -1: "Испорчено"
}


def parties_votes(parties, votes):
    """Вернуть информацию о голосах 'votes', отданных за партии 'parties'.
    Испорченные бланки также присутствуют в результате.

    Параметры:
        - parties (dict): информация о партиях (номер голоса: название);
        - votes (list): номера голосов.

    Результат:
        dict: название: кол-во отданных голосов."""
    results = {party: 0 for party in parties}
    total_votes = len(votes)

    for vote in votes:
        if vote in parties:
            results[vote] += 1

    return results


def print_results(votes_for_p):
    """Вывести результаты голосования в формате:

    1. Партия №2 | 1111 | 58.21%
    2. Партия №4 |  999 | 38.14%

    Параметры:
        - votes_for_p (dict): результат функции parties_votes().
    """
    sorted_results = sorted(votes_for_p.items(), key=lambda x: x[1], reverse=True)

    total_votes = sum(votes_for_p.values())

    for i, (party_id, votes_count) in enumerate(sorted_results, start=1):
        party_name = parties[party_id]
        percentage = (votes_count / total_votes) * 100
        print(f"{i}. {party_name} | {votes_count} | {percentage: .2f}%")

votes_for_parties = parties_votes(parties, votes)
print_results(parties_votes(parties, votes))

# --------------
# Пример вывода:
#
# 1. Партия №3 | 27 | 26.47%
# 2. Партия №1 | 22 | 21.57%
# 3. Партия №2 | 20 | 19.61%
# 4. Партия №5 | 14 | 13.73%
# 5. Партия №4 | 12 | 11.76%
# 6. Испорчено |  7 |  6.86%
