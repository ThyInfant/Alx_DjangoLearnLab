Book API uses Django REST Framework generic views to provide CRUD functionality.
Read operations are public, while write operations require authentication.
Validation for publication year is enforced at the serializer level.
URLs follow RESTful structure under /api/books/.

# BookListView supports filtering by title, publication_year, and author,

# searching by title and author name, and ordering by title or publication_year.

API tests are located in api/test_views.py and use Django REST Framework's APITestCase.
They validate CRUD operations, permissions, and advanced query features like filtering, searching, and ordering.
Run tests using: python manage.py test api
A temporary test database is created automatically during execution.
