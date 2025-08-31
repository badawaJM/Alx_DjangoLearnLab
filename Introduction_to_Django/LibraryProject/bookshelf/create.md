from library.models import Book

# Create a book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# Expected Output:
# <Book: 1984 by George Orwell>
