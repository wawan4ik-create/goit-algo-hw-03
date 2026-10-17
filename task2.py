import random

def get_numbers_ticket(min, max, quantity):
    if min > max or min < 1 or max < 0 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))  # шість різних відсортованих чисел
print(get_numbers_ticket(10, 20, 5))  # має працювати
print(get_numbers_ticket(1, 5, 5))  # усі числа [1, 2, 3, 4, 5]
print(get_numbers_ticket(2, 3, 3))  # порожній список, без зависання
print(get_numbers_ticket(0, 10, 3))  # порожній список
print(get_numbers_ticket(1, 1001, 3))  # порожній список
print(get_numbers_ticket(5, 1, 2))  # порожній список