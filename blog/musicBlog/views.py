from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   #this is a mixin that will be used to restrict access to certain pages
from .models import Post
from django.contrib.auth.models import User

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
# from django.http import HttpResponse



def home(response):
    context ={
        'posts': Post.objects.all()
    }
    return render(response, 'musicBlog/home.html', context=context) 


class PostListView(ListView):   #this class inherits from the ListView class of django and is used to display a list of objects/blog posts
    model = Post
    template_name = 'musicBlog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']   #sorting the posts by date_posted in descending order
    paginate_by = 4   #this is used to paginate the posts

class UserPostListView(ListView):   #this class inherits from the ListView class of django and is used to display a list of objects/blog posts
    model = Post
    template_name = 'musicBlog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']   #sorting the posts by date_posted in descending order
    paginate_by = 4   #this is used to paginate the posts

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  #this will get the username from the url if the user exists else it will return a 404 error
        return Post.objects.filter(author=user).order_by('-date_posted')  #this will return the posts of the user

class PostDetailView(DetailView): #this class inherits from the DetailView class of django and is used to display a single object/blog post
    model = Post  


class PostCreateView(LoginRequiredMixin,CreateView):   
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):   
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):                #this function will be used to restrict access to the page
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #this class inherits from the DetailView class of django and is used to display a single object/blog post
    model = Post  
    success_url = '/'
    
    def test_func(self):                #this function will be used to restrict access to the page
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False

def about(response):
    return render(response, 'musicBlog/about.html', {'title': 'About'})
















'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<--- Dummy data for testing --->

posts = [
{
    'author':'Yutika Rege',
    'title': 'First Lady of Jazz',
    'content': 'Ella Fitzgerald was an American jazz singer often referred to as the First Lady of Song, Queen of Jazz, and Lady Ella.',
    'date_posted': 'November 21, 2022'
},
{
    'author':'Jane Doe',
    'title': 'Born in the USA',
    'content': 'Bruce Frederick Joseph Springsteen is an American singer and songwriter. He has released 21 studio albums, most of which feature his backing band, the E Street Band',
    'date_posted': 'November 22, 2022'
}
]'''