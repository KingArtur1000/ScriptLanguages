def get_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "":
            raise ValueError("Строка не должна быть пустой!")
        else:
            return user_input


try:
    non_empty_str = get_non_empty_string("Введите строку (не пустую) --> ")
    print(f"Вы ввели: {non_empty_str}")
except ValueError as e:
    print(e)
