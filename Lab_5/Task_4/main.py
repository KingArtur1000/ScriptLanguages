from vars import *

vector = [0] * X

for i in range(len(vector)):
    vector[i] = i + 1

    # Проверьте, находится ли элемент в пределах диапазона [K, M], и замените его отрицательным значением
    if K <= vector[i] <= M:
        vector[i] = -vector[i]

print(vector)
