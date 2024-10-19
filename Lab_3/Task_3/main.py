# Шаг 1: Список гаших студентов
student_list = ["RoSTICK", "NikitOS", "KingArtur1000", "StASS"]

# Шаг 2: Записываем этот список в файл
with open("Task_3/students.txt", "w") as f:
    for student in student_list:
        f.write(student + ",")
