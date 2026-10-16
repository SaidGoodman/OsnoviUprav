from book import Book


# Класс школьного учебника, наследник Book
class SchoolTextbook(Book):
    def __init__(self, title, pages, price, grade):
        # Вызов конструктора родительского класса
        super().__init__(title, pages, price)
        # Класс обучения
        self._grade = grade
        print("Вызван конструктор дочернего класса SchoolTextbook")

    # Свойство: класс обучения
    @property
    def grade(self):
        return self._grade

    # Изменение класса с проверкой
    @grade.setter
    def grade(self, value):
        if value < 1 or value > 11:
            raise ValueError("класс должен быть от 1 до 11")
        self._grade = value

    # Вывод информации об учебнике
    def print_info(self):
        print("Тип: школьный учебник")
        super().print_info()
        print(f"Класс: {self.grade}")
