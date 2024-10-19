def get_positive_float():
    try:
        number = float(input("\nВведите положительное дробное число --> "))
        if number > 0 and isinstance(number, float):
            return number
        else:
            print("Ошибка: введенное значение не является положительным дробным. Попробуйте снова.\n")
    except ValueError:
        print("Ошибка: введённое значение не является числом. Попробуйте снова.\n")


positive_float = get_positive_float()
print(f"Вы ввели: {positive_float}\n")
