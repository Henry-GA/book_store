from django.db import models
from django.utils.timezone import now


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    publication_date = models.DateTimeField(default=now)
    description = models.TextField(max_length=200)
