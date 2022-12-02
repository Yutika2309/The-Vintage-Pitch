from django.db.models.signals import post_save  # this is the signal we want to listen to
from django.contrib.auth.models import User     
from django.dispatch import receiver  # this is the receiver of the signal
from .models import Profile  # this is the model we want to create when the signal is received

@receiver(post_save, sender=User)  # this is the receiver decorator, it takes the signal and the sender as arguments    
def create_profile(sender, instance, created, **kwargs):  # this is the function that will be called when the signal is received
    if created:  # if the user is created
        Profile.objects.create(user=instance)  # create a profile for the user
    
@receiver(post_save, sender=User)  # this is the receiver decorator, it takes the signal and the sender as arguments
def save_profile(sender, instance, **kwargs):  # this is the function that will be called when the signal is received
    instance.profile.save()  # save the profile
    

