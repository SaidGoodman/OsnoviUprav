# Демонстрация работы классов книг
from fiction_book import FictionBook
from term_dictionary import TermDictionary
from school_textbook import SchoolTextbook

# Создание объектов, конструктор наследника вызывает конструктор Book
print("Создание объектов (вызов конструкторов):")
novel = FictionBook("Мастер и Маргарита", 480, 650, "М.А. Булгаков", "16+")
dictionary = TermDictionary("Словарь терминов IT", 320, 900, "информатика")
textbook = SchoolTextbook("Алгебра", 256, 540, 8)
books = [novel, dictionary, textbook]

# Вывод информации о каждом объекте
print("\nИнформация об объектах:")
for book in books:
    book.print_info()
    print()

# Средняя стоимость одной страницы
print("Стоимость одной страницы:")
for book in books:
    print(f"{book.title}: {book.page_price():.2f} руб.")

# Увеличение цены, если название начинается с заданного слова
print("\nУвеличение цены:")
word = input("Введите слово: ")
percent = float(input("Введите процент: "))
for book in books:
    if book.raise_price(word, percent):
        print(f"{book.title}: новая цена {book.price:.2f} руб.")
    else:
        print(f"{book.title}: цена не изменилась")

# Метод get_age_limit переопределен только в FictionBook
print("\nВозрастное ограничение:")
print("FictionBook (свой метод):", novel.get_age_limit())
print("TermDictionary (метод Book):", dictionary.get_age_limit())

# Работа свойств
print("\nСвойства:")
print("Автор:", novel.author)
print("Область знаний:", dictionary.field)
textbook.grade = 9
print("Новый класс учебника:", textbook.grade)
try:
    textbook.price = -100
except ValueError as error:
    print("Ошибка:", error)
