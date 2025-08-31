from library.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year

# Expected Output:
# (1, '1984', 'George Orwell', 1949)
