from vars import *
import numpy as np

# Создаем одномерный массив А
A = np.arange(K, K + X)
print("Одномерный массив A:")
print(A)

# Создаем двумерные массивы из массива A
print("\nДвумерные массивы из A:")
# Размерность 2x7
A_2x7 = A.reshape(2, 7)
print("2x7:\n", A_2x7)
# Размерность 7x2
A_7x2 = A.reshape(7, 2)
print("7x2:\n", A_7x2)

# Создаем трехмерные массивы из массива A
print("\nТрехмерные массивы из A:")
# Размерность 2x2x7
try:
    A_2x2x7 = A.reshape(2, 2, 7)
    print("2x2x7:\n", A_2x2x7)
except ValueError:
    print("Невозможно преобразовать в 2x2x7.")

# Размерность 2x7x1
try:
    A_2x7x1 = A.reshape(2, 7, 1)
    print("2x7x1:\n", A_2x7x1)
except ValueError:
    print("Невозможно преобразовать в 2x7x1.")
