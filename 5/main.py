import re

def is_valid_credit_card(card_number):
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'  # Начинается с 4, 5 или 6, и имеет 4 группы по 4 цифры, разделенные дефисами или без них

    if re.match(pattern, card_number):
        if re.search(r'(\d)\1{3,}', card_number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"


n = int(input())
for _ in range(n):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))
