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

# def posts(request):
#     if request.method == 'POST':
#         postForm = PostForm(request.POST)
#         print(postForm)
#         if postForm.is_valid:
#             postData = postForm.cleaned_data
#             post = Post(title = postData['title'], date = postData['date'], content = postData['content'], author = postData['author'], category = postData['category'])
#             post.save()
#             return render(request, 'BlogApp/index.html')
#     else:
#         postForm = PostForm()
#     return render(request, 'BlogApp/posts.html', {'postForm':postForm})

def search_post(request):
    return render(request, "BlogApp/search-post.html")

def search_post_result(request):
    title_views = request.GET['title']
    all_posts = Post.objects.filter(title=title_views)
    return render(request,"BlogApp/search-post-result.html",{"title":title_views,"posts":all_posts})

# def categories(request):
#     if request.method == 'POST':
#         categoryForm = AuthorForm(request.POST)
#         print(categoryForm)
#         if categoryForm.is_valid:
#             categoryData = categoryForm.cleaned_data
#             category = Category(name = categoryData['name'])
#             category.save()
#             return render(request, 'BlogApp/index.html')
#     else:
#         categoryForm = CategoryForm()
#     return render(request, 'BlogApp/categories.html', {'categoryForm':categoryForm})

# def authors(request):
#     if request.method == 'POST':
#         authorForm = AuthorForm(request.POST)
#         print(authorForm)
#         if authorForm.is_valid:
#             authorData = authorForm.cleaned_data
#             author = Author(name = authorData['name'], contact = authorData['contact'])
#             author.save()
#             return render(request, 'BlogApp/index.html')
#     else:
#         authorForm = AuthorForm()
#     return render(request, 'BlogApp/authors.html', {'authorForm':authorForm})

# def apiposts(request):
#     all_posts = Post.objects.all()
#     return HttpResponse(serializers.serialize('json', all_posts))

# def find_posts(request):
#     all_posts = Post.objects.all()
#     return HttpResponse(serializers.serialize('json', all_posts))

# def new_post(request):
#     post = Post(title = 'TituloTest', date = date.today(), content = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam earum rem, voluptate nostrum repudiandae aliquid ut quae quidem hic numquam quasi magnam dolore error facilis sed nobis perspiciatis eius dignissimos.', author = 'Author', category = 'Category' )
#     post.save()
#     return HttpResponse(f'El post {post.title} ha sido creado')

# def edit_post(request):
#     post_title = 'TituloTest'
#     Post.objects.filter(title = post_title).update(title = 'TituloTestEditado')
#     return HttpResponse(f'El titulo {post_title} ha sido modificado')

# def delete_post(request):
#     post_title = 'TituloTestEditado'
#     post = Post.objects.get(title = post_title)
#     post.delete()
#     return HttpResponse(f'el post {post.title} ha sido eliminado')

class PostList(ListView):
    model = Post
    template = 'BlogApp/post_list.html'

class PostDetail(DetailView):
    model = Post
    template = 'BlogApp/post_detail.html'

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