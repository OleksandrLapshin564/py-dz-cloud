import math

def ellipse_area(a, b):
    """
    Calculates the area of an ellipse using the semi-major and minor axes.

    Parameters:
    a (float): length of the semi-major axis
    b (float): length of the semi-minor axis

    Returns:
    float: area of the ellipse
    """
    if a <= 0 or b <= 0:
        raise ValueError("The length of the semi-axes must be positive!")
    return math.pi * a * b

# Заздалегідь задані приклади
predefined_examples = [
    (3, 4),  # Велика піввісь = 3, Мала піввісь = 4
    (5.5, 2.3),  # Велика піввісь = 5.5, Мала піввісь = 2.3
    (7, 7),  # Велика піввісь = 7, Мала піввісь = 7 (коло)
]

# Обчислення площі для заданих прикладів
print("Results for predefined examples:")
for i, (a, b) in enumerate(predefined_examples, start=1):
    try:
        area = ellipse_area(a, b)
        print(f"Example {i}: a = {a}, b = {b} -> Area: {area:.2f}")
    except ValueError as e:
        print(f"Example {i}: a = {a}, b = {b} -> Error: {e}")

# Обчислення площі для значень, введених користувачем
print("\nArea calculation based on user input:")
try:
    a = float(input("Enter the length of the semi-major axis (a): "))
    b = float(input("Enter the length of the semi-minor axis (b): "))
    area = ellipse_area(a, b)
    print(f"Area of an ellipse: {area:.2f}")
except ValueError as e:
    print(f"Error: {e}")
