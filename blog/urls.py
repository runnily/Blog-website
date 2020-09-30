from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"), #This allows us to go to home
    #ensure blog-home as they could be multiple apps.
    path('about/', views.about, name="blog-about")


    #its good practice to put a trailing slash


]