from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(req):
  posts = Post.objects.all()
  return render(req, 'index.html', {'posts' : posts}) 

def post(req):
  return HttpResponse('I am a Post')
  
