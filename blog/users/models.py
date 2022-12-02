from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):                                    # this is a model that inherits from the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if the user is deleted, the profile is deleted too
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # this is the image field
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    #def save(self, *args, **kwargs):
    #   super().save(*args, **kwargs)  # super() <- this is the save method of the parent class, we are calling it here to save the image first
    #    img = Image.open(self.image.path)      
    #   if img.height > 300 or img.width > 300:
    #       output_size = (300, 300)
    #       img.thumbnail(output_size)
    #       img.save(self.image.path)