# Создаём класс MinVoda
class MinVoda:
    def __init__(self, type):
        self.type = type

    def show_my_drink(self):
        print('Минеральная вода -', self.type)  


# Пример использования
stool_water = MinVoda('Столовая')
leather_water = MinVoda('Лечебная')
common_water = MinVoda('Хлорированная (18 общежитие)')


stool_water.show_my_drink()  # Output: Минеральная вода - Столовая
leather_water.show_my_drink()  # Output: Минеральная вода - Лечебная
common_water.show_my_drink()   # Output: Минеральная вода - Хлорированная (18 общежитие)