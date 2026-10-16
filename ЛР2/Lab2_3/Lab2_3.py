# Демонстрация работы классов геометрических фигур
from figure import Figure
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

# Создание объектов, конструктор наследника вызывает конструктор Figure
print("Создание объектов (вызов конструкторов):")
radius = float(input("Введите радиус круга: "))
circle = Circle(radius, "красный")
rectangle_sizes = input("Введите ширину и высоту прямоугольника: ")
width, height = map(float, rectangle_sizes.split())
rectangle = Rectangle(width, height, "синий")
triangle_sides = input("Введите стороны треугольника: ")
side_a, side_b, side_c = map(float, triangle_sides.split())
triangle = Triangle(side_a, side_b, side_c, "зеленый")
print("Всего создано фигур:", Figure.count)

# Вывод информации о каждом объекте
print("\nИнформация об объектах:")
figures = [circle, rectangle, triangle]
for shape in figures:
    shape.print_info()
    print()

# Собственные методы и свойства наследников
print("Собственные методы и свойства:")
circle.scale(2)
print("Радиус круга после увеличения в 2 раза:", circle.radius)
print("Диаметр круга:", circle.diameter)
print(f"Площадь круга: {circle.area():.2f}")
print(f"Диагональ прямоугольника: {rectangle.diagonal():.2f}")
print("Прямоугольник является квадратом:", rectangle.is_square())
rectangle.width = rectangle.height
print("Новая ширина прямоугольника:", rectangle.width)
print("Прямоугольник является квадратом:", rectangle.is_square())
print("Тип треугольника:", triangle.get_type())
triangle.sides = (5, 5, 5)
print("Новые стороны треугольника:", triangle.sides)
print("Тип треугольника:", triangle.get_type())

# Изменение свойств базового и дочернего класса
print("\nИзменение свойств:")
circle.color = "желтый"
print("Новый цвет круга:", circle.color)
try:
    circle.radius = -3
except ValueError as error:
    print("Ошибка:", error)

# Метод is_valid: в Circle и Rectangle из Figure, в Triangle переопределен
print("\nПроверка существования фигур:")
print("Круг существует (метод Figure):", circle.is_valid())
print("Прямоугольник существует (метод Figure):", rectangle.is_valid())
print("Треугольник существует (метод Triangle):", triangle.is_valid())
wrong_triangle = Triangle(1, 2, 10, "черный")
print("Треугольник 1, 2, 10 существует:", wrong_triangle.is_valid())

# Сравнение площадей фигур
print("\nСравнение площадей:")
print(circle.compare_area(rectangle))
print(triangle.compare_area(rectangle))
print("Всего создано фигур:", Figure.count)
