import numpy as np
from vars import *

# Создание матрицы
matrix = np.array([col_1, col_2])

# Вычисление определителя
det_matrix = np.linalg.det(matrix)
print("Определитель:", det_matrix)

# Решение системы линейных уравнений
coefficients = np.array([[col_1, col_2]])  # Коэффициенты уравений
constants = np.array([5, 6])             # Константы

solution = np.linalg.solve(coefficients, constants)
print("Результат:", solution)
