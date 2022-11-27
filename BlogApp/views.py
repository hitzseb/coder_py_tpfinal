from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import Post
from django.core import serializers

def home(request):
    return render(request, 'BlogApp/index.html')

def posts(request):
    return render(request, 'BlogApp/posts.html')

def category(request):
    return HttpResponse('category')

def author(request):
    return HttpResponse('author')

def apiposts(request):
    all_posts = Post.objects.all()
    return HttpResponse(serializers.serialize('json', all_posts))
