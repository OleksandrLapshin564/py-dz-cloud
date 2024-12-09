from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_age(birth_date):
    """
    Calculates age in years, months, and days based on date of birth.

    :param birth_date: a string in the format 'YYYY-MM-DD' representing the date of birth
    :return: dictionary with age in years, months and days
    """
    # Перетворення рядка на об'єкт datetime
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    # Поточна дата
    current_date = datetime.now()
    # Обчислення різниці
    difference = relativedelta(current_date, birth_date)

    return {
        'years': difference.years,
        'months': difference.months,
        'days': difference.days
    }


# Приклади використання
examples = [
    "1990-04-15",
    "2000-10-01",
    "2010-06-30",
]

for date in examples:
    age = calculate_age(date)
    print(f"Date of birth: {date}")
    print(f"Age: {age['years']} years, {age['months']} months, {age['days']} days")
    print("-" * 40)
