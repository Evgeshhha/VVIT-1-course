class Book:
    title = "Книга1"
    author = "Садовникова"
    year = "2024"

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
bk = Book()
print(bk.get_info())
