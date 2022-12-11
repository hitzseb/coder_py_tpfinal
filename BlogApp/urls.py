from django.urls import path
from BlogApp import views

urlpatterns = [
    path("", views.home, name = 'Home'),
    path('home/', views.home, name = 'Home'),
    path('post/search/', views.search_post, name='PostSearch'),
    path('post/list/', views.PostList.as_view(), name='PostList'),
    path('post/detail/<pk>', views.PostDetail.as_view(), name='PostDetail'),
    path('post/create/', views.PostCreate.as_view(), name='PostCreate'),
    path('post/update/<pk>', views.PostUpdate.as_view(), name='PostUpdate'),
    path('post/delete/<pk>', views.PostDelete.as_view(), name='PostDelete'),
    path('category/search/', views.search_category, name='CategorySearch'),
    path('category/list/', views.CategoryList.as_view(), name='CategoryList'),
    path('category/detail/<pk>', views.CategoryDetail.as_view(), name='CategoryDetail'),
    path('category/create/', views.CategoryCreate.as_view(), name='CategoryCreate'),
    path('category/update/<pk>', views.CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('category/delete/<pk>', views.CategoryDelete.as_view(), name='CategoryDelete'),
    path('author/search/', views.search_author, name='AuthorSearch'),
    path('author/list/', views.AuthorList.as_view(), name='AuthorList'),
    path('author/detail/<pk>', views.AuthorDetail.as_view(), name='AuthorDetail'),
    path('author/create/', views.AuthorCreate.as_view(), name='AuthorCreate'),
    path('author/update/<pk>', views.AuthorUpdate.as_view(), name='AuthorUpdate'),
    path('author/delete/<pk>', views.AuthorDelete.as_view(), name='AuthorDelete'),
]