from datetime import datetime

def get_days_from_today(date):
    """
    Функція обчислює кількість днів від сьогоднішньої дати до введеної дати.
    Args:
        date (str): Дата у форматі "YYYY-MM-DD".
    Returns:
        int: Кількість днів від сьогоднішньої дати до введеної дати. Якщо формат дати неправильний, повертає None.
    """
    current_date = datetime.today().date()

    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (current_date - input_date).days
    except ValueError:
        return None

if __name__ == "__main__":
    while True:
        date_input = input("Введіть дату в форматі (YYYY-MM-DD): ")
        result = get_days_from_today(date_input)

        if result is None:
            print("Невірний формат дати. Будь ласка, введіть дату у форматі (YYYY-MM-DD).")
        else:
            print(f"Кількість днів від сьогодні до {date_input}: {result} днів.")
            break