import math
from figure import Figure


# Класс круга, наследник Figure
class Circle(Figure):
    def __init__(self, radius, color):
        # Вызов конструктора родительского класса
        super().__init__("Круг", color)
        # Радиус круга, задается через свойство с проверкой
        self.radius = radius
        print("Вызван конструктор дочернего класса Circle")

    # Свойство: радиус круга
    @property
    def radius(self):
        return self._radius

    # Изменение радиуса с проверкой
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("радиус должен быть больше нуля")
        self._radius = value

    # Свойство: диаметр круга (только чтение)
    @property
    def diameter(self):
        return 2 * self._radius

    # Площадь круга
    def area(self):
        return math.pi * self._radius ** 2

    # Периметр круга (длина окружности)
    def perimeter(self):
        return 2 * math.pi * self._radius

    # Увеличение радиуса в заданное число раз
    def scale(self, factor):
        self.radius = self._radius * factor

    # Вывод информации о круге
    def print_info(self):
        super().print_info()
        print(f"Радиус: {self.radius}")
        print(f"Диаметр: {self.diameter}")
