import math

def arc_length(radius, angle_in_radians):
    """
    Calculates the length of a circle arc for a given radius and angle in radians.

    Parameters:
    radius (float): Circle radius.
    angle_in_radians (float): Angle in radians.

    Returns:
    float: Arc length of a circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative!")
    if angle_in_radians < 0 or angle_in_radians > 2 * math.pi:
        raise ValueError("The angle must be between 0 and 2π radians!")
    return radius * angle_in_radians

# Основний блок програми з прикладом використання
print("Calculating the length of a circle arc:")

# Заздалегідь задані приклади радіусів і кутів
examples = [
    (5, math.pi / 2),  # Радіус 5, кут π/2
    (10, math.pi),     # Радіус 10, кут π
    (7, 2 * math.pi),  # Радіус 7, повний оберт
    (3, -math.pi / 4)  # Радіус 3, некоректний кут
]

for radius, angle in examples:
    try:
        print(f"\nRadius: {radius}, Angle in radians: {angle}")
        length = arc_length(radius, angle)
        print(f"Arc length: {length:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
import math

def arc_length(radius, angle_in_radians):
    """
    Calculates the length of a circle arc for a given radius and angle in radians.

    Parameters:
    radius (float): Circle radius.
    angle_in_radians (float): Angle in radians.

    Returns:
    float: Arc length of a circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative!")
    if angle_in_radians < 0 or angle_in_radians > 2 * math.pi:
        raise ValueError("The angle must be between 0 and 2π radians!")
    return radius * angle_in_radians

# Основний блок програми з прикладом використання
print("Calculating the length of a circle arc:")

# Заздалегідь задані приклади радіусів і кутів
examples = [
    (6, math.pi / 2),  # Радіус 5, кут π/2
    (11, math.pi),     # Радіус 10, кут π
    (8, 2 * math.pi),  # Радіус 7, повний оберт
    (4, -math.pi / 4)  # Радіус 3, некоректний кут
]

for radius, angle in examples:
    try:
        print(f"\nRadius: {radius}, Angle in radians: {angle}")
        length = arc_length(radius, angle)
        print(f"Arc length: {length:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
