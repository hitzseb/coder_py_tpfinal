from django.urls import path
from BlogApp import views

urlpatterns = [
    path("", views.home, name = 'Home'),
    path('home/', views.home, name = 'Home'),
    # path('posts/', views.posts, name = 'Posts'),
    # path('categories/', views.categories, name = 'Categories'),
    # path('authors/', views.authors, name = 'Authors'),
    path('search-post/', views.search_post, name='SearchPost'),
    path('search-post-result/', views.search_post_result, name='SearchPostResult'),
    # path('posts-api/', views.apiposts),
    # path('find-posts/', views.find_posts),
    # path('new-post/', views.new_post),
    # path('edit-post/', views.edit_post),
    # path('delete-post/', views.delete_post),
    path('post/list/', views.PostList.as_view(), name='PostList'),
    path('post/detail/<pk>', views.PostDetail.as_view(), name='PostDetail'),
    path('post/create/', views.PostCreate.as_view(), name='NewPost'),
    path('post/update/<pk>', views.PostUpdate.as_view(), name='EditPost'),
    path('post/delete/<pk>', views.PostDelete.as_view(), name='DeletePost'),
]