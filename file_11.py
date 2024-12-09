import math
import matplotlib.pyplot as plt

def projectile_trajectory(v0, angle_deg, time_step=0.01):
    """
    Simulates the trajectory of a ball throw.

    Parameters:
    v0 (float): initial velocity (m/s)
    angle_deg (float): throw angle (degrees)
    time_step (float): time interval for simulation (s)

    Returns:
    tuple: lists of coordinates x та y
    """
    g = 9.81  # Прискорення вільного падіння, м/с^2
    angle_rad = math.radians(angle_deg)  # Переводимо кут у радіани

    # Розрахунок компонент швидкості
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)

    # Ініціалізація списків координат
    x_coords = []
    y_coords = []

    # Моделювання руху
    t = 0
    y = 0
    while y >= 0:  # Поки м'яч не досягне землі
        x = vx * t
        y = vy * t - 0.5 * g * t ** 2
        if y >= 0:  # Записуємо лише ті точки, де y >= 0
            x_coords.append(x)
            y_coords.append(y)
        t += time_step

    return x_coords, y_coords

def plot_trajectory(x, y):
    """
    Plots a trajectory graph.

    Parameters:
    x (list): coordinates x
    y (list): coordinates y
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Ball trajectory")
    plt.title("Ball throw trajectory")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Приклади використання
try:
    # Заздалегідь задані приклади
    v0_examples = [10, 20, 30]
    angle_examples = [30, 45, 60]

    print("Graphs for predefined examples:")
    for v0, angle in zip(v0_examples, angle_examples):
        x, y = projectile_trajectory(v0, angle)
        print(f"Initial speed: {v0} m/s, Angle: {angle}°")
        plot_trajectory(x, y)

    # Введення користувача
    print("\nUser-input-based modeling:")
    v0 = float(input("Enter the initial velocity of the ball (m/s): "))
    angle = float(input("Enter the throw angle (degrees): "))
    x, y = projectile_trajectory(v0, angle)
    plot_trajectory(x, y)
except ValueError as e:
    print(f"Error: {e}")
