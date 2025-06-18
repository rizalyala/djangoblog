from django.shortcuts import render, get_object_or_404
from .models import Post

def homepage(request):
    posts = Post.objects.all().order_by('-created_at')[:15]
    return render(request, 'index.html', {'posts': posts})

def blog_list(request):
    blogs = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'blogs': blogs})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})