from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    #ON Cascade means to delete user as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default="default.jpg", upload_to='profile_pics')

    #dunder str function
    def __str__(self):
        return f'{self.user.username} Profile'
    """
    def save(self, *args, **kawrgs):

        #override the save method of a model
     
        super().save(*args, **kawrgs) #parnets class run

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    """
    


        