from datetime import datetime, timedelta


def calculate_arrival(start_datetime, duration_hours):
    """
    Calculates the date and time of arrival.

    :param start_datetime: a string with the start date and time in the format 'YYYY-MM-DD HH:MM'
    :param duration_hours: trip duration in hours
    :return: a string with the date and time of arrival in the format 'YYYY-MM-DD HH:MM'
    """
    # Перетворення рядка на об'єкт datetime
    start = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')

    # Додавання тривалості поїздки
    duration = timedelta(hours=duration_hours)
    arrival = start + duration

    # Повертаємо дату й час прибуття у вигляді рядка
    return arrival.strftime('%Y-%m-%d %H:%M')


# Приклади використання
examples = [
    ("2024-12-09 08:30", 5),
    ("2024-12-09 22:45", 7.5),
    ("2024-12-31 23:30", 2),
]

# Виведення результатів для кожного прикладу
for start, duration in examples:
    arrival_time = calculate_arrival(start, duration)
    print(f"Start of the trip: {start}, Duration: {duration} hours -> Arrival time: {arrival_time}")
