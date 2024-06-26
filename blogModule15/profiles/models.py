from django.db import models
from authors.models import Author
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=25)
    bio = models.TextField()
    author = models.OneToOneField(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.name