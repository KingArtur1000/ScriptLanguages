from vars import *
import numpy as np

# Создаем матрицу A из столбцов col_1 и col_2
A = np.column_stack((col_1, col_2))
print("Матрица A (5 строк, 2 столбца):")
print(A)

# Транспонируем матрицу A
AT = A.T
print("\nТранспонированная матрица A (AT):")
print(AT)
