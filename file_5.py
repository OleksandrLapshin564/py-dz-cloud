import math


def solve_quadratic(a, b, c):
    """
    Finds the roots of a quadratic equation ax^2 + bx + c = 0.

    Parameters:
    a (float): The coefficient at x^2.
    b (float): The coefficient at x.
    c (float): Free member.

    Returns:
    tuple: Roots of the equation or message if there are no roots.
    """
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b ** 2 - 4 * a * c  # Формула для дискримінанта
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,  # Один корінь повертається як кортеж
    else:
        return "There are no roots (discriminant is less than 0)"


# Основний блок програми з прикладом використання
print("Solving a quadratic equation ax^2 + bx + c = 0:")

# Заздалегідь задані коефіцієнти
coefficients = [
    (2, -4, 3),  # Два корені
    (2, 3, 2),  # Один корінь
    (2, 1, -5),  # Два корені
    (2, 2, 2)  # Немає коренів
]

for a, b, c in coefficients:
    try:
        print(f"\nEquation: {a}x^2 + {b}x + {c} = 0")
        result = solve_quadratic(a, b, c)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
