from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Невірний формат дати. Використовуй 'YYYY-MM-DD'.")

    today = datetime.today().date()
    delta = today - target_date
    return delta.days

user_date = input("Введи дату у форматі YYYY-MM-DD: ")

try:
    result = get_days_from_today(user_date)
    print(result)
except ValueError as e:
    print(e)
