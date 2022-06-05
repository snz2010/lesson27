# Create your models here.
import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Ad(models.Model):
    # STATUS = [
    #     ("true", "опубликовано"),
    #     ("false", "не опубликовано")
    # ]
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    # status = models.CharField(max_length=5, choices=STATUS, default="false")
    # created = models.DateField(auto_now_add=True)
