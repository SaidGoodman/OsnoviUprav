from book import Book


# Класс художественной книги, наследник Book
class FictionBook(Book):
    def __init__(self, title, pages, price, author, age_limit):
        # Вызов конструктора родительского класса
        super().__init__(title, pages, price)
        # Автор книги
        self._author = author
        # Возрастное ограничение, например 16+
        self._age_limit = age_limit
        print("Вызван конструктор дочернего класса FictionBook")

    # Свойство: автор книги
    @property
    def author(self):
        return self._author

    # Переопределение метода Book
    def get_age_limit(self):
        return self._age_limit

    # Вывод информации о художественной книге
    def print_info(self):
        print("Тип: художественная книга")
        super().print_info()
        print(f"Автор: {self.author}")
