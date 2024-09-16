def safe_divide(a, b):
    if b == 0:
        return "Ошибка! Попытка деления на ноль..."
    else:
        return a / b

A = 8
B = 4

result = safe_divide(A, B)
print("Результат деления - ", result)
