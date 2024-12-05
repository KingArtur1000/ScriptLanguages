from vars import *
import pandas as pd

# Создаем Series с иерархическими индексами
# Используем col_1 как первый уровень индекса и col_2 как второй уровень индекса
data = {
    ('A', 'first'): [1, 2, 3],
    ('A', 'second'): [4, 5, 6],
    ('B', 'first'): [7, 8, 9],
    ('B', 'second'): [10, 11, 12]
}

multi_index_series = pd.Series(data, index=pd.MultiIndex.from_tuples([('A', 'first'), ('A', 'second'), ('B', 'first'), ('B', 'second')]))

print("Исходная Series с иерархическими индексами:")
print(multi_index_series)

# Конвертация в DataFrame, где второй уровень индексов превращается в колонки
df = multi_index_series.unstack()
print("\nПреобразованный DataFrame:")
print(df)
