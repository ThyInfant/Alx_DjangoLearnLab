from relationship_app.models import Author, Book, Library, Librarian

# ---- Sample Data Creation ----
# Create an author
author1 = Author.objects.create(name="George Orwell")

# Create books
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)

# Create a library
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)

# Create a librarian
librarian1 = Librarian.objects.create(name="Alice", library=library1)

# ---- Queries ----

# 1️⃣ Query all books by a specific author
books_by_orwell = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:")
for book in books_by_orwell:
    print(book.title)

# 2️⃣ List all books in a library
books_in_library = library1.books.all()
print(f"\nBooks in {library1.name}:")
for book in books_in_library:
    print(book.title)

# 3️⃣ Retrieve the librarian for a library
library_librarian = library1.librarian
print(f"\nLibrarian of {library1.name}: {library_librarian.name}")
