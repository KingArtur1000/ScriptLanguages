def find_item_in_list(list, item):
    try:
        index = list.index(item)  # Если элемент найден, index() вернёт его индекс
        print(f"\nЭлемент {list[index]} найден!\n")
        return item
    except ValueError:
        print(f"\nЭлемент {item} НЕ найден!\n")
        return None


my_list = [1, 2, 3, 4, 5]

find_item_in_list(my_list, 3)
find_item_in_list(my_list, 6)
