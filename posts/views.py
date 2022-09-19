from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().values()
    context={
        'posts':posts,
    }
    return render(request, 'index.html', context)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post.html", {"post": post})