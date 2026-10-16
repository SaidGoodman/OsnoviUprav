import math
from figure import Figure


# Класс треугольника, наследник Figure
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, color):
        # Вызов конструктора родительского класса
        super().__init__("Треугольник", color)
        # Длины сторон, задаются через свойство с проверкой
        self.sides = (side_a, side_b, side_c)
        print("Вызван конструктор дочернего класса Triangle")

    # Свойство: стороны треугольника в виде кортежа
    @property
    def sides(self):
        return self._side_a, self._side_b, self._side_c

    # Изменение сторон с проверкой
    @sides.setter
    def sides(self, values):
        for value in values:
            if value <= 0:
                raise ValueError("стороны должны быть больше нуля")
        self._side_a, self._side_b, self._side_c = values

    # Переопределение метода Figure:
    # треугольник существует, если каждая сторона меньше суммы двух других
    def is_valid(self):
        a, b, c = self.sides
        return a < b + c and b < a + c and c < a + b

    # Площадь по формуле Герона
    def area(self):
        if not self.is_valid():
            return 0
        a, b, c = self.sides
        p = self.perimeter() / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    # Периметр треугольника
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    # Тип треугольника по длинам сторон
    def get_type(self):
        a, b, c = self.sides
        if a == b == c:
            return "равносторонний"
        if a == b or b == c or a == c:
            return "равнобедренный"
        return "разносторонний"

    # Вывод информации о треугольнике
    def print_info(self):
        super().print_info()
        print(f"Стороны: {self._side_a}, {self._side_b}, {self._side_c}")
        print(f"Тип: {self.get_type()}")
