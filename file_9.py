def harmonic_sum(n):
    """
    Calculates the sum of the first n terms of a harmonic series.

    Parameters:
    n (int): number of members of the series

    Returns:
    float: sum of the first n terms of the harmonic series
    """
    if n <= 0:
        raise ValueError("The number of terms in the series must be positive!")
    return sum(1 / i for i in range(1, n + 1))

# Приклади використання
try:
    # Заздалегідь задані приклади
    examples = [2, 6, 11, 21]
    print("Results for predefined examples:")
    for n in examples:
        print(f"n = {n} -> Harmonic sum: {harmonic_sum(n):.5f}")

    # Введення від користувача
    print("\nCalculations based on user input:")
    n = int(input("Enter the number of terms in the harmonic series (n): "))
    print(f"Harmonic sum для n = {n}: {harmonic_sum(n):.5f}")
except ValueError as e:
    print(f"Error: {e}")
