class Point:
    def __init__(self, x=0, y=0):
        """Конструктор класса, инициализирует координаты точки."""
        self.x = x
        self.y = y

    def getXY(self):
        """Возвращает координаты точки в виде списка."""
        return [self.x, self.y]

    def __add__(self, other):
        """Перегрузка оператора + для сложения координат по осям X и Y."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Операция сложения возможна только между объектами типа Point")

    def Show(self):
        """Выводит координаты точки на экран."""
        print(f"Координаты точки: ({self.x}, {self.y})")


# Пример использования
p1 = Point(3, 4)
p2 = Point(5, 7)

p3 = p1 + p2  # Использование перегруженного оператора +
p3.Show()     # Ожидаемый вывод: Координаты точки: (8, 11)
