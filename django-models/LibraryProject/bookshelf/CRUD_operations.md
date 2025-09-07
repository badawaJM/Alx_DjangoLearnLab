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

from library.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year

# Expected Output:
# (1, '1984', 'George Orwell', 1949)

from library.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Expected Output:
# 'Nineteen Eighty-Four'

from library.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Try retrieving all books
Book.objects.all()

# Expected Output:
# <QuerySet []>
