from django.urls import path
from BlogApp import views

urlpatterns = [
    path('home/', views.home, name = 'Home'),
    path('posts/', views.posts, name = 'Posts'),
    path('category/', views.category, name = 'Category'),
    path('author/', views.author, name = 'Author'),
    path('postsApi/', views.apiposts),
]