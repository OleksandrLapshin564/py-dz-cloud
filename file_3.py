import math


def circle_area(radius):
    """
  Calculates the area of a circle given a given radius.

    Parameters:
    radius (float): Radius of the circle.

    Returns:
    float: Area of a circle.
    """
    if radius < 0:
        raise ValueError("The radius cannot be negative!")
    return math.pi * radius ** 2


# Основний блок програми з прикладом радіусів
print("Example of the program working with given radii:")

# Заздалегідь задані радіуси
radii = [4, 5.5, -3, 1]  # Радіуси можна змінювати за потреби

print(f"Selected radii: {radii}")

print("\nCalculation results:")
for r in radii:
    try:
        area = circle_area(r)
        print(f"The area of a circle with radius {r} is equal to {area:.2f}")
    except ValueError as e:
        print(f"Error for radius {r}: {e}")


