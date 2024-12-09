from datetime import datetime, timedelta


def get_mondays(start_date, end_date):
    """
    Generates a list of all Mondays between two given dates.

    :param start_date: string in 'YYYY-MM-DD' format, starting date
    :param end_date: string in 'YYYY-MM-DD' format, end date
    :return: list of date strings (in 'YYYY-MM-DD' format) that are Mondays
    """
    # Перетворення рядків у об'єкти datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Перехід до першого понеділка після початкової дати (або до неї, якщо це понеділок)
    current_date = start_date
    while current_date.weekday() != 0:  # 0 відповідає понеділку
        current_date += timedelta(days=1)

    # Створення списку понеділків
    mondays = []
    while current_date <= end_date:
        mondays.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(weeks=1)

    return mondays


# Приклади використання
start = "2023-11-01"
end = "2023-12-31"

mondays = get_mondays(start, end)
print(f"All Mondays between {start} and {end}:")
print("\n".join(mondays))
