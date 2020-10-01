'''
This allows a new user for time they register it automatically
generates a new profile. This is done by using django signials
'''

#Below we import a signial specifcally the post_save
#This is a signial that gets server when a user is saved
from django.db.models.signals import post_save

#We need import a user, as the post_save would send a signial
#when a user is saved
from django.contrib.auth.models import User

#A reciever is a function which recieves a signial and performs some task
from django.dispatch import receiver

#we import profile as we want a new profile
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This function act as an reciever so when post_save signials a new
    User (when its save a user). We do the action that is performed below
    which is to create a new user instance. Create profile is taking all the variables
    from the post_save signial
    """
    if created:
        Profile.objects.create(user=instance)

#**kwargs accepts any addition key word
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """This saves the profile when the user saves"""
    instance.profile.save()
    
