def cache_decorator(func):
    cache = None  # Для хранения результата функции
    counter = 0   # Счетчик вызовов

    def wrapper():
        nonlocal cache, counter
        if counter < 3:
            # Если счетчик меньше 3, возвращаем кешированный результат
            counter += 1
            return cache
        else:
            # Если достигнут лимит, выполняем функцию заново и кешируем результат
            cache = func()
            counter = 1  # Сбрасываем счётчик после обновления кеша
            return cache

    return wrapper


# Пример функции для декорирования
@cache_decorator
def example_function():
    print("Выполнение функции...")
    return "Результат работы функции"


# Тестирование декоратора
print(example_function())  # Функция выполняется и результат кешируется
print(example_function())  # Возвращается кешированный результат
print(example_function())  # Возвращается кешированный результат
print(example_function())  # Кеш сбрасывается и функция выполняется заново
print(example_function())  # Возвращается новый кешированный результат
