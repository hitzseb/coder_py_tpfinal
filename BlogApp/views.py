from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import *
from django.core import serializers
from BlogApp.forms import *

def home(request):
    return render(request, 'BlogApp/index.html')

def posts(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        print(postForm)
        if postForm.is_valid:
            postData = postForm.cleaned_data
            post = Post(title = postData['title'], date = postData['date'], content = postData['content'], author = postData['author'], category = postData['category'])
            post.save()
            return render(request, 'BlogApp/index.html')
    else:
        postForm = PostForm()
    return render(request, 'BlogApp/posts.html', {'postForm':postForm})

def categories(request):
    if request.method == 'POST':
        categoryForm = AuthorForm(request.POST)
        print(categoryForm)
        if categoryForm.is_valid:
            categoryData = categoryForm.cleaned_data
            category = Category(name = categoryData['name'])
            category.save()
            return render(request, 'BlogApp/index.html')
    else:
        categoryForm = CategoryForm()
    return render(request, 'BlogApp/categories.html', {'categoryForm':categoryForm})

def authors(request):
    if request.method == 'POST':
        authorForm = AuthorForm(request.POST)
        print(authorForm)
        if authorForm.is_valid:
            authorData = authorForm.cleaned_data
            author = Author(name = authorData['name'], contact = authorData['contact'])
            author.save()
            return render(request, 'BlogApp/index.html')
    else:
        authorForm = AuthorForm()
    return render(request, 'BlogApp/authors.html', {'authorForm':authorForm})

def apiposts(request):
    all_posts = Post.objects.all()
    return HttpResponse(serializers.serialize('json', all_posts))
