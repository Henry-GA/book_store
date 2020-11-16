from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    pages = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/web/media/')
    pub_date = models.DateTimeField(default=now)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField(max_length=280)
    pub_date = models.DateTimeField(default=now)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
