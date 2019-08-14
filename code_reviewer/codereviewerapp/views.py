from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author':'Muhire ',
        'title': 'Post 1',
        'content' : 'The first every time content',
        'date_posted' : 'August 12,2019'
    },
    {
        'author':'Heritier',
        'title': 'Sample conn Post 1',
        'content' : 'No comments about hit life The first every time content',
        'date_posted' : 'August 12,2019'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'codereviewerapp/home.html', context)

def about(request):
    return render(request, 'codereviewerapp/about.html', {'title': 'About'})
