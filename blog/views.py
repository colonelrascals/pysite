from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html', {'posts': posts})


def post(req, slug):
    print(slug)
    return render_to_response('post.html', {
    'post': get_object_or_404(Post, slug=slug)
  })
