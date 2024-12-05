from vars import *
import pandas as pd

# Создаем Series на основе данных из col_1 и col_2
# Используем col_1 как индексы, а col_2 как значения
series = pd.Series(data=col_2, index=col_1)
print("Исходная серия:")
print(series)

# Выбираем конкретное значение по позиции
# Например, значение с индексом 2 (в порядке хранения в Series)
position_to_select = 2
selected_value = series.iloc[position_to_select]
print(f"\nЗначение на позиции {position_to_select}: {selected_value}")
