import random


# Функція для обчислення числа Пі методом Монте-Карло
def estimate_pi(num_points):
    inside_circle = 0

    # Генерація випадкових точок і перевірка, чи знаходяться вони всередині кола
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Перевірка чи точка всередині кола
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    # Обчислення наближеного значення числа Пі
    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate


# Тестування функції з різною кількістю точок
test_cases = [200, 2000, 20000, 200000, 2000000]  # заздалегідь задані приклади кількості точок

# Для кожного прикладу обчислюємо наближене значення числа Пі
for num_points in test_cases:
    pi_value = estimate_pi(num_points)
    print(f"Estimate Pi for {num_points} points: {pi_value}")

