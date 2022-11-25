from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    contact = models.EmailField()
    description = models.CharField(max_length=200)
    avatar = models.CharField(max_length=100)

class Category(models.Model):
    name=models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
