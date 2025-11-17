import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до формату:
    +380XXXXXXXXX або +38XXXXXXXXXX

    :param phone_number: сирий номер у довільному форматі
    :return: нормалізований номер як рядок
    """
    
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+"):
          cleaned = "+" + re.sub(r"[^\d]", "", cleaned[1:])
    else:
        cleaned = re.sub(r"[^\d]", "", cleaned)

    if cleaned.startswith("380"):
        cleaned = "+" + cleaned

    elif not cleaned.startswith("+"):
        cleaned = "+38" + cleaned

    return cleaned
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для смсок:", sanitized_numbers)

