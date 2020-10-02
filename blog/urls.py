from django.urls import path
from .views import (PostListView, PostDetailView, 
    PostCreateView, PostUpdateView,
    PostDeleteView, UserListView)
from . import views


#the <> are models already define within django or within our models.py
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"), #This allows us to go to home
    path('user/<str:username>', UserListView.as_view(), name="user-posts"),
    #were using a pk to point to a particular primary key
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    #ensure blog-home as they could be multiple apps.
    path('about/', views.about, name="blog-about")


    #its good practice to put a trailing slash


]

# <app>/<model>_<viewtype>.html -> blog/post_list.html
# we want to change the view