from book import Book


# Класс словаря профессиональных терминов, наследник Book
class TermDictionary(Book):
    def __init__(self, title, pages, price, field):
        # Вызов конструктора родительского класса
        super().__init__(title, pages, price)
        # Область знаний, к которой относятся термины
        self._field = field
        print("Вызван конструктор дочернего класса TermDictionary")

    # Свойство: область знаний
    @property
    def field(self):
        return self._field

    # Вывод информации о словаре
    def print_info(self):
        print("Тип: словарь профессиональных терминов")
        super().print_info()
        print(f"Область знаний: {self.field}")
