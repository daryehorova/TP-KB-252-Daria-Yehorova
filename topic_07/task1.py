class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Книга: '{self.title}' | Автор: {self.author} | Рік: {self.year}"

my_book = Book("Python для початківців", "Іван Петренко", 2023)
print(my_book)