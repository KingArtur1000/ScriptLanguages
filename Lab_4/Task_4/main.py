import math


class Point:
    def __init__(self, x=0, y=0):
        """Инициализирует координаты точки."""
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """Вычисляет расстояние от точки до начала координат."""
        return math.sqrt(self.x ** 2 + self.y ** 2)


    def getPoint(self):
        """Возвращает координаты точки в виде списка."""
        return [self.x, self.y]



class PointColor(Point):
    def __init__(self, x=0, y=0, color="black"):
        """Инициализирует координаты точки и ее цвет."""
        super().__init__(x, y)
        self.color = color


    def getColor(self):
        """Возвращает цвет точки."""
        return self.color



# Пример использования
point = Point(3, 4)
print("Координаты точки:", point.getPoint())  # Ожидаемый вывод: [3, 4]
print("Расстояние до начала координат:", point.distance_from_origin())  # Ожидаемый вывод: 5.0

colored_point = PointColor(5, 7, "red")
print("Координаты цветной точки:", colored_point.getPoint())  # Ожидаемый вывод: [5, 7]
print("Цвет точки:", colored_point.getColor())  # Ожидаемый вывод: red
print("Расстояние до начала координат:", colored_point.distance_from_origin())  # Ожидаемый вывод: примерно 8.6
