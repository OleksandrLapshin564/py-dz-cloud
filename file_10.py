import math


def vector_magnitude(v):
    """
    Calculates the length of a vector.

    Parameters:
    v (tuple): vector coordinates (x, y, z)

    Returns:
    float: vector length
    """
    return math.sqrt(sum(coord ** 2 for coord in v))


def dot_product(u, v):
    """
    Calculates the dot product of two vectors.

    Parameters:
    u (tuple): coordinates of the first vector (x, y, z)
    v (tuple): coordinates of the second vector (x, y, z)

    Returns:
    float: scalar product
    """
    return sum(u[i] * v[i] for i in range(len(u)))


def angle_between_vectors(u, v):
    """
    Calculates the angle between two vectors in radians.

    Parameters:
    u (tuple): coordinates of the first vector (x, y, z)
    v (tuple): coordinates of the second vector (x, y, z)

    Returns:
    float: angle between vectors in radians
    """
    mag_u = vector_magnitude(u)
    mag_v = vector_magnitude(v)

    if mag_u == 0 or mag_v == 0:
        raise ValueError("The length of a vector cannot be zero!")

    cos_theta = dot_product(u, v) / (mag_u * mag_v)
    # Обмеження cos_theta для уникнення помилок обчислень (через похибки)
    cos_theta = max(-1, min(1, cos_theta))
    return math.acos(cos_theta)


# Приклади використання
try:
    # Заздалегідь задані приклади
    examples = [
        ((2, 1, 1), (1, 2, 1)),  # Перпендикулярні вектори
        ((2, 2, 1), (2, -2, 1)),  # Кут 90 градусів
        ((2, 3, 4), (5, 6, 7)),  # Загальний випадок
    ]

    print("Results for predefined examples:")
    for u, v in examples:
        angle_rad = angle_between_vectors(u, v)
        angle_deg = math.degrees(angle_rad)
        print(f"Vectors {u} та {v}: Кут = {angle_rad:.4f} radian ({angle_deg:.2f} degrees)")

    # Введення користувачем
    print("\nCalculations based on user input:")
    u = tuple(map(float, input("Enter the coordinates of the first vector (with a space between them): ").split()))
    v = tuple(map(float, input("Enter the coordinates of the second vector (separated by a space): ").split()))
    angle_rad = angle_between_vectors(u, v)
    angle_deg = math.degrees(angle_rad)
    print(f"Angle between vectors: {angle_rad:.4f} radian ({angle_deg:.2f} degrees)")
except ValueError as e:
    print(f"Error: {e}")
