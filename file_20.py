import time
from datetime import datetime, timedelta


def countdown_timer(target_date):
    """
    Countdown timer to a specified date and time.

    :param target_date: date and time in format 'YYYY-MM-DD HH:MM:SS'
    """
    # Перетворюємо рядок дати у об'єкт datetime
    target_datetime = datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')

    print(f"Countdown to: {target_datetime}")

    while True:
        # Поточний час
        now = datetime.now()

        # Різниця між заданою датою та поточним часом
        remaining_time = target_datetime - now

        # Якщо час минув, завершити цикл
        if remaining_time <= timedelta(0):
            print("\nThe time has come!")
            break

        # Розрахунок днів, годин, хвилин, секунд
        days, seconds = divmod(remaining_time.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        # Вивід зворотного відліку
        print(f"\rRemaining: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds",
              end="")

        # Затримка перед оновленням
        time.sleep(1)


# Приклад використання
countdown_timer("2024-12-31 23:59:59")
