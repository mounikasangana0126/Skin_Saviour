from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
import time
# Create your views here.

def SignUp(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if not (password==cpassword):
            messages.warning(request, "Both passwords should be same")
            return redirect('signup')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "User already exists with this username")
            return redirect('signup')
        user=User.objects.filter(email=email)
        if user.exists():
            messages.warning(request, "User already exists with this email")
            return redirect('signup')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )

        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'registration/signup.html')


def LoginAPI(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username):
            messages.warning(request,"User doesn't exist")
            return redirect('login')

        user=authenticate(username=username,password=password)
        if not user:
            messages.warning(request,"Password is incorrect")
            return redirect('login')

        else:
            login(request,user) 
            return redirect('skin_treatment')

    return render(request, 'registration/login.html')

def Logout(request):
    logout(request)
    time.sleep(3)
    return redirect('home')

