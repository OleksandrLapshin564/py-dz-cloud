import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime


def plot_activity(dates):
    """
    Builds a graph of user activity by date.

    :param dates: list of date strings in format 'YYYY-MM-DD'
    """
    # Конвертуємо рядки у об'єкти datetime
    parsed_dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    # Підраховуємо кількість подій для кожного дня
    date_counts = Counter(parsed_dates)

    # Сортуємо дати для правильного відображення
    sorted_dates = sorted(date_counts.keys())
    counts = [date_counts[date] for date in sorted_dates]

    # Формуємо список міток (дата у форматі 'DD-MM')
    labels = [date.strftime('%d-%m') for date in sorted_dates]

    # Будуємо графік
    plt.figure(figsize=(10, 5))
    plt.bar(labels, counts, color='skyblue')
    plt.xlabel('Dates')
    plt.ylabel('Number of events')
    plt.title('User activity by date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Приклад використання
user_activity_dates = [
    "2024-11-05", "2024-11-06", "2024-11-06",
    "2024-11-06", "2024-11-06", "2024-11-07",
    "2024-11-08", "2024-11-07"
]

plot_activity(user_activity_dates)
