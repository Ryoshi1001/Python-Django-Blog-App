from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request): 
  if request.method == "POST": 
    form = UserRegisterForm(request.POST)
    if form.is_valid(): 
      form.save()
      # username = form.cleaned_data.get('username')
      messages.success(request, f'Your account is now Active. You are now able to log into Django Blog.')
      return redirect('login')
  else: 
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

# Login and Logout handled by Django LoginView in Project settings.py

@login_required
def profile(request): 
  if request.method == 'POST':
    # if new data in POST method add POST data
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid(): 
      u_form.save()
      p_form.save()

      # message back to end user that form can be saved
      messages.success(request, f'Account profile updated: ')
      return redirect('profile')

  else: 
    # no new data in POST method
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  # Python dictionary with keys
  context = {
    'u_form': u_form, 
    'p_form': p_form
  }
  # Pass context into template
  return render(request, 'users/profile.html', context)






