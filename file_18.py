from datetime import datetime


def is_birthday_weekend(birth_date, year):
    """
    Checks if a birthday falls on a weekend (Saturday/Sunday) within a given year.

    :param birth_date: string in 'MM-DD' format, date of birth (without year)
    :param year: int, year for verification
    :return: bool, True if the birthday falls on a weekend, otherwise False
    """
    # Формуємо повну дату народження для заданого року
    full_birth_date = f"{year}-{birth_date}"
    birth_date_obj = datetime.strptime(full_birth_date, '%Y-%m-%d')

    # Перевіряємо день тижня (5 — субота, 6 — неділя)
    return birth_date_obj.weekday() in [5, 6]


# Приклад використання
birth_date = "04-07"  # День і місяць народження (07 квітня)
year = 2025

if is_birthday_weekend(birth_date, year):
    print(f"In {year}, the birthday falls on a weekend.")
else:
    print(f"In {year}, the birthday does not fall on a weekend.")
