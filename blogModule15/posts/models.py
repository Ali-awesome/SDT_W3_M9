from django.db import models
from catagories.models import Catagory
from authors.models import Author
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField() 
    catagory = models.ManyToManyField(Catagory)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.title