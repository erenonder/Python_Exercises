from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [

    {
        'author': 'Onder Eren',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 19, 2020'
    },
    {
        'author': 'Nihan Ocak',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 20, 2020'
    }



]


def home(request):

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
