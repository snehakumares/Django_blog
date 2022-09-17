from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().values()
    context={
        'posts':posts,
    }
    return render(request, 'index.html', context)