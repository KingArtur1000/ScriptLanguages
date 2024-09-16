def safe_remove(list, item):
    try:
        list.remove(item)
    except ValueError:
        print(f"{item} not in list")

array = [1, 2, 3, 4, 5]

print("\nСписок до удаления:", array, '\n')

safe_remove(array, 3)

print("\nСписок после удаления: ", array, "\n")