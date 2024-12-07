import math


def calculate_factorial(n):
    """
    Calculates the factorial of a number using math.factorial.

    Parameters:
    n (int): The number for which you want to calculate the factorial.

    Returns:
    int: Factorial of a number.
    """
    if n < 0:
        raise ValueError("The factorial is defined only for non-negative numbers!")
    return math.factorial(n)


# Основний блок програми з прикладом використання
print("Calculating factorial using math.factorial:")

# Заздалегідь задані числа для обчислення факторіалів
numbers = [5, 0, -3, 7]  # Числа можна змінити

print(f"Selected numbers: {numbers}")

print("\nCalculation results:")
for num in numbers:
    try:
        result = calculate_factorial(num)
        print(f"The factorial of the number {num} is equal to {result}")
    except ValueError as e:
        print(f"Error for number {num}: {e}")
