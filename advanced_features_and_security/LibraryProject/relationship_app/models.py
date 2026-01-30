from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model (ForeignKey relationship)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_year = models.IntegerField(default=2000)
    added_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='relationship_books'
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]


# Library model (ManyToMany relationship)
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


# Librarian model (OneToOne relationship)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name


# class UserProfile(models.Model):
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#     def __str__(self):
#         return f"{self.user.username} ({self.role})"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"



# Signal to automatically create UserProfile when a User is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         # Default role is Member
#         UserProfile.objects.create(user=instance, role='Member')


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
