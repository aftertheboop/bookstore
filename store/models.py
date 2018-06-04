from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)
