def validate_data(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Входные данные должны быть в виде словаря!")

        if 'name' not in data or not isinstance(data['name'], str):
            raise ValueError("Ключ 'name' должен иметь строковое значение!")
        
        print("С данными все в порядке!")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
        return False
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return False


validate_data({'name': 'John Doe'})  # Не должно быть никаких исключений
validate_data({'name': 123})       # Вызовет TypeError
validate_data({'age': 30})         # Вызовет ValueError
validate_data(['John Doe'])       # Вызовет TypeError
validate_data({'name': 'John Doe', 'age': 30})  # Не должно быть никаких исключений