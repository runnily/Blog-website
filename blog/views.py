from django.shortcuts import render
from django.views.generic import (ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


# Create your views here.
def home(request):
    """
    Handles traffic from homepage of our blog
    """
    #this is what is going to be assessed in our html
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',  context)


class PostListView(ListView):
    #Model should the view interact with
    model = Post #what model to query in order to create our post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html 
    context_object_name = 'posts' #we need to change this inial attribute from 'object.list' to ->  'posts'
    ordering = ['-date_posted'] #changes from newest to oldest

class PostDetailView(DetailView):
    model = Post #what model to query in order to create our post

class PostCreateView(LoginRequiredMixin, CreateView):
    #Model should the view interact with
    model = Post #what model to query in order to create our post
    fields = ["title", "content"]
    #template name (default ) -> 'post_form.html'

    def form_valid(self, form):
        #Every post needs to have an author which should not be null
        #This function lets the view know that the author is the 
        #current logged in user
        form.instance.author = self.request.user #form which we are trying to submit is equal to the current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #Model should the view interact with
    model = Post #what model to query in order to create our post
    fields = ["title", "content"]
    #template name (default ) -> 'post_form.html'

    def form_valid(self, form):
        #Every post needs to have an author which should not be null
        #This function lets the view know that the author is the 
        #current logged in user
        form.instance.author = self.request.user #form which we are trying to submit is equal to the current user
        return super().form_valid(form)

    def test_func(self):
        #A function our UserPassesTestMixin would run in order to know
        #to see if our user passes a certain test condition

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post #what model to query in order to create our post
    success_url = '/'
    
    def test_func(self):
    #A function our UserPassesTestMixin would run in order to know
    #to see if our user passes a certain test condition

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {"title": "About"}) 

