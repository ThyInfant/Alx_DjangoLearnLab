from django.db import models

# Create your models here.
class Author(models.Model):
    # Stores the name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents a book written by an author
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title