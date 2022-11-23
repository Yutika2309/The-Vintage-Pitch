from django.shortcuts import render
# from django.http import HttpResponse

posts = [
{
    'author':'Yutika Rege',
    'title': 'First Lady of Jazz',
    'content': 'Ella Fitzgerald was an American jazz singer often referred to as the First Lady of Song, Queen of Jazz, and Lady Ella.',
    'date_posted': 'November 21, 2022'
},
{
    'author':'John Doe',
    'title': 'Born in the USA',
    'content': 'Bruce Frederick Joseph Springsteen is an American singer and songwriter. He has released 21 studio albums, most of which feature his backing band, the E Street Band',
    'date_posted': 'November 22, 2022'
}
]

def home(response):
    context ={
        'posts': posts
    }
    return render(response, 'musicBlog/home.html', context=context)

def about(response):
    return render(response, 'musicBlog/about.html', {'title': 'About'})