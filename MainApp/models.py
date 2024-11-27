from django.db import models
from pip._vendor.rich.color import Color


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(default="")
    colors = models.ManyToManyField(to="Color")

    def __str__(self):
        return  self.name

class Color(models.Model):
    name = models.CharField(max_length=16, unique=True)