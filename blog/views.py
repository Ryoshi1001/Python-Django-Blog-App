from django.shortcuts import render
from django.http import HttpResponse


# unreal data for post 

posts = [
  {
    'author': 'CoreyMS', 
    'title': 'Blog Post 1', 
    'content': "First post comment", 
    'date_posted': 'August 14, 2024'
  }, 
  {
    'author': 'Tomi Toko', 
    'title': 'Blog Post 2', 
    'content': "Second post comment", 
    'date_posted': 'August 4, 2024'
  }
]

# Create your views here.
def home(request): 
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request): 
  return render(request, 'blog/about.html', { 'title': 'About'})