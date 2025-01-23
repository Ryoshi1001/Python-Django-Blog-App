from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView, 
  DeleteView,
)

# Create your views here.
# view for blog calendar in base.html file by adding context to home path

def home(request): 
  context = {
    'posts': Post.objects.all(), 
  }
  return render(request, 'blog/home.html', context)

# class based views: 
class PostListView(ListView): 
  model = Post
  #<app>/<model>_<viewtype>.html
  template_name = 'blog/home.html' 
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 4

class UserPostListView(ListView): 
  model = Post
  #<app>/<model>_<viewtype>.html
  template_name = 'blog/user_posts.html' 
  context_object_name = 'posts'
  paginate_by = 4

  def get_queryset(self): 
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView): 
  model = Post
  
# Create View: view with form: title and content
class PostCreateView(LoginRequiredMixin, CreateView): 
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
# Update View: view with same form as Create View: title and content
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
  model = Post
  fields = ['title', 'content']
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  # test function needed for UserPassesTestMixin: This only let’s user update own post and not another post: 
  def test_func(self): 
    post = self.get_object()
    if self.request.user == post.author: 
      return True
    return False

# Update View: view with same form as Create View: title and content
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = ('/')

    # test function needed for UserPassesTestMixin: This only let’s user delete own post and not another post: 
  def test_func(self): 
    post = self.get_object()
    if self.request.user == post.author: 
      return True
    return False
  
 
def about(request): 
  return render(request, 'blog/about.html', { 'title': 'About'})

