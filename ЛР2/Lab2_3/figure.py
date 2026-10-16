# Базовый класс геометрической фигуры
class Figure:
    # Поле класса: количество созданных фигур
    count = 0

    def __init__(self, name, color):
        # Название фигуры
        self._name = name
        # Цвет фигуры
        self._color = color
        Figure.count += 1
        print(f"Вызван конструктор родительского класса Figure: {name}")

    # Свойство: название фигуры (только чтение)
    @property
    def name(self):
        return self._name

    # Свойство: цвет фигуры
    @property
    def color(self):
        return self._color

    # Изменение цвета с проверкой
    @color.setter
    def color(self, new_color):
        if new_color == "":
            raise ValueError("цвет не может быть пустым")
        self._color = new_color

    # Площадь фигуры, переопределяется в наследниках
    def area(self):
        return 0

    # Периметр фигуры, переопределяется в наследниках
    def perimeter(self):
        return 0

    # Проверка существования фигуры
    # Переопределяется в Triangle, не переопределяется в Circle и Rectangle
    def is_valid(self):
        return self.area() > 0

    # Сравнение площади с другой фигурой
    def compare_area(self, other):
        if self.area() > other.area():
            return f"{self.name} больше по площади, чем {other.name}"
        if self.area() < other.area():
            return f"{self.name} меньше по площади, чем {other.name}"
        return f"{self.name} и {other.name} равны по площади"

    # Вывод информации о фигуре
    def print_info(self):
        print(f"Фигура: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area():.2f}")
        print(f"Периметр: {self.perimeter():.2f}")
