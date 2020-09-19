from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return  render(request, 'signup.html', {'form':form})

def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
                user = User.objects.get(username=username)
            except:
                return render(request, 'login.html')
            if user.password == password:
                return redirect('index')
        return redirect('index')
    return render(request, 'login.html')
