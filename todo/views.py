from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    # Create new user
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'] )
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Username already been taken. Pleasue choose a new username.'})

        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    # Create new user
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'] )
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Username already been taken. Pleasue choose a new username.'})

        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})    

def logoutuser(request):
    #Only logout USER if it is a POST-request. !BrowserLoading in advance restriction 
    if request.method == 'POST':
        logout(request) 
        return redirect('home')   
def currenttodos(request):
    return render(request, 'todo/currenttodos.html', {'form':UserCreationForm()})


