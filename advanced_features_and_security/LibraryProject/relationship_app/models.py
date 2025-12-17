from django.db import models
from django.conf import settings


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name='books')

    class Meta():
        permissions = (
            ("can_add_book", "can Add a new book"),
            ( "can_change_book", "can Change book details"),
            ("can_delete_book", "can Delete a book")
        )

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("librarian", "Librarian"),
        ("member", "Member")
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="member")

    def __str__(self):
        return self.user.username