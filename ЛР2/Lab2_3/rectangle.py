import math
from figure import Figure


# Класс прямоугольника, наследник Figure
class Rectangle(Figure):
    def __init__(self, width, height, color):
        # Вызов конструктора родительского класса
        super().__init__("Прямоугольник", color)
        # Ширина и высота, задаются через свойства с проверкой
        self.width = width
        self.height = height
        print("Вызван конструктор дочернего класса Rectangle")

    # Свойство: ширина прямоугольника
    @property
    def width(self):
        return self._width

    # Изменение ширины с проверкой
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("ширина должна быть больше нуля")
        self._width = value

    # Свойство: высота прямоугольника
    @property
    def height(self):
        return self._height

    # Изменение высоты с проверкой
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("высота должна быть больше нуля")
        self._height = value

    # Площадь прямоугольника
    def area(self):
        return self._width * self._height

    # Периметр прямоугольника
    def perimeter(self):
        return 2 * (self._width + self._height)

    # Длина диагонали
    def diagonal(self):
        return math.sqrt(self._width ** 2 + self._height ** 2)

    # Проверка, является ли прямоугольник квадратом
    def is_square(self):
        return self._width == self._height

    # Вывод информации о прямоугольнике
    def print_info(self):
        super().print_info()
        print(f"Ширина: {self.width}")
        print(f"Высота: {self.height}")
        print(f"Диагональ: {self.diagonal():.2f}")
