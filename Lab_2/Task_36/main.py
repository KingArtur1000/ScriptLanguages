def get_valid_age():
    while True:
        try:
            age = int(input("Введите свой возраст: "))
            if age < 0 or age > 120:
                print("Неверный возраст! Пожалуйста введите возраст от 0 до 120 лет.")
            else:
                return age
        except ValueError:
            print("Неверный ввод! Пожалуйста введите возраст используя целочисленные значения!")

age = get_valid_age()
print(f"Ваш возраст: {age}")
