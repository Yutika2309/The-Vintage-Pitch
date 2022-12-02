from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # user -> post is a one to many relationship, post -> user vice-versa
from django.urls import reverse

class Post(models.Model):                           #the Post function will inherit from the models.Model class
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #the default value is the current time and will change, should there be any edits
    author = models.ForeignKey(User, on_delete=models.CASCADE) #the author is a foreign key to the User model, and if the user is deleted, the post will be deleted as well

    def __str__(self): #this function will return the title of the post
        return self.title
    
    def get_absolute_url(self): #this function will return the url of the post
        return reverse('post-detail', kwargs={'pk': self.pk}) #this is the url of the post-detail page, and the primary key of the post is passed to the url
