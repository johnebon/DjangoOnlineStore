from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render

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