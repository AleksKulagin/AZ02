import random
import pandas as pd

# Создаем данные для DataFrame
data = {
    'Имя': ['Иван', 'Настя', 'Костя', 'Лиза', 'Вася', 'Саша', 'Дина', 'Юра', 'Данил', 'Марина'],
    'Математика': [random.randint(1, 5) for _ in range(10)],
    'Информатика': [random.randint(1, 5) for _ in range(10)],
    'Физика': [random.randint(1, 5) for _ in range(10)],
    'Химия': [random.randint(1, 5) for _ in range(10)],
    'Биология': [random.randint(1, 5) for _ in range(10)]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# 2. Выводим первые несколько строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# 3. Вычисляем среднюю оценку по каждому предмету
print("\nСредняя оценка по каждому предмету:")
print(df.mean(numeric_only=True))

# 4. Вычисляем медианную оценку по каждому предмету
print("\nМедианная оценка по каждому предмету:")
print(df.median(numeric_only=True))

# 5. Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1 для Математики:", Q1_math)
print("Q3 для Математики:", Q3_math)
print("IQR для Математики:", IQR_math)

# 6. Вычисляем стандартное отклонение
print("\nСтандартное отклонение по каждому предмету:")
print(df.std(numeric_only=True))