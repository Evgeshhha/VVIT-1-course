class Book:
    title = "Книга1"
    author = "Садовникова"
    year = "2024"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
bk = Book()
print(bk.get_info())