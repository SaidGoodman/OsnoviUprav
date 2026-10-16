books = {}
while True:
    line = input("Введите автора и название книги: ")
    if line == "":
        break
    author, title = line.split(":", 1)
    author = author.strip()
    if author not in books:
        books[author] = title.strip()

print("Словарь уникальных авторов:")
for author, title in books.items():
    print(author + ": " + title)
