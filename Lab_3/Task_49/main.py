# Массив из мебели
furniture = ["Диван", "Стул", "Стол", "Ковёр", "Шкаф", "Полка", "Комод", ""]

# Записываем в файл в каждую строку по 3 элемента
with open("Task_49/furniture.txt", "w", -1, "utf-8") as f:
    for i in range(0, len(furniture), 3):
        line = ' '.join(furniture[i:i+3]) + '\n'
        f.write(line)
