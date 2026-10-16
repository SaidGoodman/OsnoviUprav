# Базовый класс книги
class Book:
    def __init__(self, title, pages, price):
        # Название книги
        self._title = title
        # Количество страниц
        self._pages = pages
        # Цена книги в рублях
        self._price = price
        print(f"Вызван конструктор родительского класса Book: {title}")

    # Свойство: название книги (только чтение)
    @property
    def title(self):
        return self._title

    # Свойство: количество страниц (только чтение)
    @property
    def pages(self):
        return self._pages

    # Свойство: цена книги
    @property
    def price(self):
        return self._price

    # Изменение цены с проверкой
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("цена не может быть отрицательной")
        self._price = value

    # Средняя стоимость одной страницы
    def page_price(self):
        return self._price / self._pages

    # Увеличение цены на заданный процент,
    # если название книги начинается с заданного слова
    def raise_price(self, word, percent):
        if self._title.split()[0].lower() == word.lower():
            self.price = self._price * (1 + percent / 100)
            return True
        return False

    # Возрастное ограничение книги
    # Переопределяется в FictionBook, не переопределяется в других
    def get_age_limit(self):
        return "0+"

    # Вывод информации о книге
    def print_info(self):
        print(f"Название: {self.title}")
        print(f"Количество страниц: {self.pages}")
        print(f"Цена: {self.price:.2f} руб.")
        print(f"Возрастное ограничение: {self.get_age_limit()}")
