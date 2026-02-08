Book API uses Django REST Framework generic views to provide CRUD functionality.
Read operations are public, while write operations require authentication.
Validation for publication year is enforced at the serializer level.
URLs follow RESTful structure under /api/books/.

# BookListView supports filtering by title, publication_year, and author,

# searching by title and author name, and ordering by title or publication_year.
