from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
  path('', views.home, name='blog-home'),
  path('about/', views.about, name='about'),
  path('login/', LoginView.as_view(template_name='blog/login.html'))
]