import random
import matplotlib.pyplot as plt

# Функція для моделювання кидків кубиків
def simulate_dice_rolls(num_rolls):
    results = [0] * 11  # Для сум від 2 до 12 (індекси від 0 до 10)
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        results[roll_sum - 2] += 1
    return results

# Функція для обчислення ймовірностей
def calculate_probabilities(results, num_rolls):
    probabilities = [(result / num_rolls) * 100 for result in results]
    return probabilities

# Симуляція
num_rolls = 1000000
results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(results, num_rolls)

# Аналітичні ймовірності для порівняння
analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

# Порівняння результатів
sums = list(range(2, 13))
plt.plot(sums, probabilities, label='Monte Carlo Probabilities', marker='o')
plt.plot(sums, analytical_probabilities, label='Analytical Probabilities', marker='x')
plt.xlabel('Sum')
plt.ylabel('Probability (%)')
plt.title('Probability of Sums in Dice Rolls: Monte Carlo vs Analytical')
plt.legend()
plt.grid(True)
plt.show()
