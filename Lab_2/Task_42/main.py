def get_value_from_dict(data, key):
    try:
        return data[key]
    except KeyError:
        print("Ключ не найден в словаре!")
        return None
    except Exception as e:
        print("Произошла ошибка:", e)
        return None


my_dict = {"A": 1, "B": 2, "C": 3}

key_to_get = "A"
result = get_value_from_dict(my_dict, key_to_get)
print("\nЗначение для ключа ", key_to_get, " это: ", result, "\n")

key_to_get = "D"
result = get_value_from_dict(my_dict, key_to_get)
print("Значение для ключа ", key_to_get, " это: ", result, "\n")

key_to_get = "B"
result = get_value_from_dict(my_dict, key_to_get)
print("Значение для ключа ", key_to_get, " это: ", result, "\n")

