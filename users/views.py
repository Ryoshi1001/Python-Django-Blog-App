from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request): 
  if request.method == "POST": 
    form = UserRegisterForm(request.POST)
    if form.is_valid(): 
      form.save()
      # username = form.cleaned_data.get('username')
      messages.success(request, f'Your account is now Active. You are now able to log into Django Blog.')
      return redirect('login', )
  else: 
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

# Login handled by Django LoginView in Project settings.py
      







