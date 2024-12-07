import math


def log_iterations(number):
    """
    Determines the number of iterations of the natural logarithm to obtain a value less than 1.

    Parameters:
    number (float): The number for which the number of iterations is calculated.

    Returns:
    int: Number of iterations.
    """
    if number <= 0:
        raise ValueError("The number must be greater than 0!")

    iterations = 0
    while number >= 1:
        number = math.log(number)  # Обчислення натурального логарифма
        iterations += 1
    return iterations


# Основний блок програми з прикладом використання
print("Calculating the number of iterations of the natural logarithm:")

# Заздалегідь задані приклади чисел
numbers = [10, math.e ** 2, 1000, 0.5]

for number in numbers:
    try:
        print(f"\nNumeric: {number}")
        result = log_iterations(number)
        print(f"Number of iterations: {result}")
    except ValueError as e:
        print(f"Error: {e}")
