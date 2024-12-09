from datetime import datetime, timedelta


def is_document_older_than_10_years(creation_date):
    """
    Checks if more than 10 years have passed since the document was created.

    :param creation_date: a string in the format 'YYYY-MM-DD' representing the date the document was created
    :return: True, if the document is older than 10 years, otherwise False
    """
    # Перетворення рядка на об'єкт datetime
    doc_date = datetime.strptime(creation_date, '%Y-%m-%d')
    # Поточна дата
    current_date = datetime.now()
    # Перевірка різниці у часі
    return (current_date - doc_date).days > 365 * 10


# Приклади використання
examples = [
    "2010-12-09",  # Документ створений більше 10 років тому
    "2015-06-01",  # Менше 10 років
    "2020-01-15",  # Недавно створений
]

for date in examples:
    result = is_document_older_than_10_years(date)
    print(f"Is the document from {date} older than 10 years? {'Yes' if result else 'No'}")
