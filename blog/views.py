from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
  return render(req, 'index.html', {}) 

def post(req):
  return HttpResponse('I am a Post')
  
