import calendar


def generate_month_calendar(year, month):
    """
    Generates a text calendar for the given month and year.

    :param year: year (integer)
    :param month: month (integer, from 1 to 12)
    :return: line with text calendar
    """
    # Створення об'єкта текстового календаря
    cal = calendar.TextCalendar()
    # Генерація календаря
    return cal.formatmonth(year, month)


# Приклади використання
examples = [
    (2024, 12),  # Грудень 2024
    (2024, 2),  # Лютий 2024 (високосний рік)
    (2023, 5),  # Травень 2023
]

for year, month in examples:
    print(f"Calendar for {year}-{month:02d}:\n")
    print(generate_month_calendar(year, month))
    print("-" * 30)
