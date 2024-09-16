def find_item_in_list(lst, item):
    try:
        print(f"\nЭлемент {item} найден!\n")
        return item
    except ValueError:
        print(f"\nЭлемент {item} НЕ найден!\n")
        return None


my_list = [1, 2, 3, 4, 5]

find_item_in_list(my_list, 3)
find_item_in_list(my_list, 6)
