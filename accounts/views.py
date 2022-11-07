from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth    
from django.contrib.auth.forms import UserCreationForm    
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.db import models
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    
    else:
        return render(request,'sign.html')

def logout(request):
    django_logout(request)
    return redirect("/")



# normal user login -- temp, temp12345
#superuser login -- abhi, abhishek12345