import re

def normalize_phone(phone_number):
    """
    Нормалізує номер телефону до міжнародного формату для України.
    Args:
        phone_number (str): Номер телефону у будь-якому форматі.
    Returns:
        str: Номер телефону у міжнародному форматі aбо None, якщо номер не відповідає очікуваним форматам.
    """
    digits = re.sub(r'\D', '', phone_number)

    if len(digits) == 12 and digits.startswith('380'):
        return '+' + digits
    elif len(digits) == 10 and digits.startswith('0'):
        return '+38' + digits
    elif len(digits) == 11 and digits.startswith('8'):
        return '+3' + digits
    else:
        return None


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "abc0501234567",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
