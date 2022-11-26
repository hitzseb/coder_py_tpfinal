from django.urls import path
from BlogApp import views

urlpatterns = [
    path('home/', views.home),
    path('post/', views.post),
    path('category/', views.category),
    path('author/', views.author),
]