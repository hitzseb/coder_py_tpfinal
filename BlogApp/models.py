from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=30)
    contact = models.EmailField()

class Category(models.Model):
    name=models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
