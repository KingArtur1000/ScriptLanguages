from vars import *
import pandas as pd

# Создаем Series на основе данных из col_1 и col_2
# Используем col_1 как индексы, а col_2 как значения
series = pd.Series(data=col_2, index=col_1)
print("Исходная серия:")
print(series)

# Выбираем значение для заданного первого индекса
# Предположим, что нужно выбрать значение для индекса 3
index_to_select = 3
selected_value = series.loc[index_to_select]
print(f"\nЗначение для индекса {index_to_select}: {selected_value}")
