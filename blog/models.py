from django.db import models
from django.utils import timezone
#We import the user model here, Django made this in the location below
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    '''
    each class is going to be its own table,
    each attribute is a field in the database
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    #auto_now - sets it when ever it updated
    #auto_now_add - sets the date
    date_posted = models.DateTimeField(default=timezone.now)
    
    #On_delete- tells django that if a user creates posts and a user is deleted we will delete their post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #To find the URL of a model object:
    #we need to create a get absolute url method, that
    #returns that path to any specific instance of our model

    def get_absolute_url(self):
        #Reverse method returns the string of the url
        return reverse('post-detail', kwargs={'pk':self.pk})

