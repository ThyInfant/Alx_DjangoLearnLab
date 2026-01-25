from relationship_app.models import Author, Book, Library, Librarian

# -------------------------------
# Query all books by a specific author
# -------------------------------

author = Author.objects.get(name="George Orwell")
books_by_author = author.books.all()

for book in books_by_author:
    print(book.title)


# -------------------------------
# List all books in a library
# -------------------------------

library = Library.objects.get(name="Central Library")
library_books = library.books.all()

for book in library_books:
    print(book.title)


# -------------------------------
# Retrieve the librarian for a library
# -------------------------------

library = Library.objects.get(name="Central Library")
librarian = library.librarian

print(librarian.name)
