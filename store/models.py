from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    image = models.ImageField(upload_to='static/web/media/')
    pub_date = models.DateTimeField(default=now)
    description = models.TextField(max_length=200)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = HTMLField('Comment')
    pub_date = models.DateTimeField(default=now)
