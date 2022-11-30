from django.urls import path
from BlogApp import views

urlpatterns = [
    path('home/', views.home, name = 'Home'),
    path('posts/', views.posts, name = 'Posts'),
    path('categories/', views.categories, name = 'Categories'),
    path('authors/', views.authors, name = 'Authors'),
    path('postsApi/', views.apiposts),
]