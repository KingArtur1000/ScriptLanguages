class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    def perimeter(self):
        print("Периметр треугольника = ", self.side1 + self.side2 + self.side3)
    

    def can_be_formed(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            print("Треугольник можно построить!")
        elif self.side1 == self.side2 and self.side2 == self.side3:
            print("Треугольник - равносторонний")
        else:
            print("Треугольник нельзя построить!")
  

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


print("\tТреугольник №1:")
triangle1 = Triangle(1, 2, 3)
triangle1.can_be_formed()

print("\tТреугольник №2:")
triangle2 = Triangle(2, 2, 3)
triangle2.can_be_formed()
triangle2.perimeter() 

print("\tТреугольник №3:")
triangle3 = EquilateralTriangle(3)
triangle3.can_be_formed()
triangle3.perimeter()
