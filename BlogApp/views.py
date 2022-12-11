from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import *
from django.core import serializers
from BlogApp.forms import *
from datetime import date
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'BlogApp/index.html')

# POST

def search_post(request):
    title_views = request.GET['title']
    all_posts = Post.objects.filter(title=title_views)
    return render(request,"BlogApp/post_search_result.html",{"title":title_views,"posts":all_posts})

class PostList(ListView):
    model = Post
    template = '/BlogApp/post_list.html'

class PostDetail(DetailView):
    model = Post
    template = '/BlogApp/post_detail.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/BlogApp/post/list/'

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/BlogApp/post/list/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/BlogApp/post/list/'

# CATEGORY

def search_category(request):
    name_views = request.GET['name']
    all_categories = Category.objects.filter(name=name_views)
    return render(request,"BlogApp/category_search_result.html",{"name":name_views,"categories":all_categories})

class CategoryList(ListView):
    model = Category
    template = '/BlogApp/category_list.html'

class CategoryDetail(DetailView):
    model = Category
    template = '/BlogApp/category_detail.html'

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/BlogApp/category/list/'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/BlogApp/category/list/'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/BlogApp/category/list/'

# AUTHOR

def search_author(request):
    name_views = request.GET['name']
    all_authors = Author.objects.filter(name=name_views)
    return render(request,"BlogApp/author_search_result.html",{"name":name_views,"authors":all_authors})

class AuthorList(ListView):
    model = Author
    template = '/BlogApp/author_list.html'

class AuthorDetail(DetailView):
    model = Author
    template = '/BlogApp/author_detail.html'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/BlogApp/author/list/'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    success_url = '/BlogApp/author/list/'

class AuthorDelete(DeleteView):
    model = Author
    success_url = '/BlogApp/author/list/'