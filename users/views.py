from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import *

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user != None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error, try again...')
            return redirect('login')
        
    else:
        return render(request, 'authenticate/login.html')
    

def LogoutView(request):
    logout(request)
    return redirect('index')


def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationCustomForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)
            
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error, try again...')
            return redirect('register')
        
    else:
        form = UserCreationCustomForm()
        
    return render(request, 'authenticate/register.html', {'form': form})
    

class ProfileView(TemplateView):
    template_name = 'users/profile.html'