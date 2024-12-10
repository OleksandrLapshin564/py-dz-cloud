from datetime import datetime, timedelta


def calculate_working_hours(start_date, end_date):
    """
    Calculates the number of working hours between two dates.

    :param start_date: Start date in format 'YYYY-MM-DD HH:MM:SS'
    :param end_date: End date in format 'YYYY-MM-DD HH:MM:SS'
    :return: Number of working hours
    """
    # Перетворення рядків у об'єкти datetime
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    # Якщо початкова дата пізніше кінцевої, повернути 0
    if start_datetime >= end_datetime:
        return 0

    # Робочий день триває з 9:00 до 18:00 (9 годин)
    work_start_hour = 9
    work_end_hour = 18
    work_hours_per_day = work_end_hour - work_start_hour

    # Лічильник робочих годин
    total_work_hours = 0

    # Поточна дата, з якої починаємо обчислення
    current_datetime = start_datetime

    while current_datetime < end_datetime:
        # Якщо це не вихідний (пн-пт)
        if current_datetime.weekday() < 5:  # 0-4 — будні дні
            # Визначення меж робочого дня
            day_start = current_datetime.replace(hour=work_start_hour, minute=0, second=0)
            day_end = current_datetime.replace(hour=work_end_hour, minute=0, second=0)

            # Знаходимо фактичний початок і кінець робочого часу для поточного дня
            actual_start = max(day_start, current_datetime)
            actual_end = min(day_end, end_datetime)

            # Розрахунок робочих годин для поточного дня
            if actual_start < actual_end:
                total_work_hours += (actual_end - actual_start).seconds // 3600

        # Переходимо до наступного дня
        current_datetime += timedelta(days=1)
        current_datetime = current_datetime.replace(hour=0, minute=0, second=0)

    return total_work_hours


# Приклад використання
start = "2024-11-28 17:00:00"
end = "2024-12-06 12:37:00"
working_hours = calculate_working_hours(start, end)
print(f"Number of working hours between {start} and {end}: {working_hours}")
