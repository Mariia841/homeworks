# завдання 1
temperatures = [2, 5, 4, 6, 7, 3, 1]


avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)
diff_temp = max_temp - min_temp

print("| Показник | Значення |")
print("| :--- | :--- |")
print(f"| Середнє значення | {avg_temp:.2f} |")
print(f"| Максимальне значення | {max_temp} |")
print(f"| Мінімальне значення | {min_temp} |")
print(f"| Різниця (Max - Min) | {diff_temp} |")


# завдання 2
expenses = [1200, 1500, 800, 600, 1000, 400, 900]

total_expenses = sum(expenses)
avg_expenses = total_expenses / len(expenses)
max_expense = max(expenses)
min_expense = min(expenses)
days_above_1000 = sum(1 for x in expenses if x > 1000)

print("| Показник | Значення |")
print("| :--- | :--- |")
print(f"| Загальна сума витрат | {total_expenses} |")
print(f"| Середнє значення | {avg_expenses:.2f} |")
print(f"| Максимальна витрата | {max_expense} |")
print(f"| Мінімальна витрата | {min_expense} |")
print(f"| Кількість днів, коли витрата > 1000 | {days_above_1000} |")

# завдання 3
from collections import Counter

votes = ["apple", "banana", "apple", "orange", "banana", "apple", "apple", "apple", "orange"]

vote_counts = Counter(votes)

winner, winner_count = vote_counts.most_common(1)[0]

print("### Результати голосування")
print("| Фрукт | Кількість |")
print("| :--- | :--- |")
for fruit, count in vote_counts.items():
    print(f"| {fruit} | {count} |")

print(f"\n**Фрукт-лідер:** {winner} ({winner_count} голосів)")

print("\n### Топ-3")
print("| Місце | Фрукт | Кількість |")
print("| :--- | :--- | :--- |")
for rank, (fruit, count) in enumerate(vote_counts.most_common(3), start=1):
    print(f"| {rank} | {fruit} | {count} |")