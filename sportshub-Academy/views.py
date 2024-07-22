from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages, auth
# from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User is already exists!")
        else:
            if password == confirm_password:

                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User signup successfully!")
                print(str(user))

            else:
                messages.error(request, "Password doesn't matching")
            
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

    
    return render(request, 'login.html')


def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/login')
    


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


def gym(request):
    return render(request, 'gym.html')

def sports(request):
    return render(request, 'sports.html')
def medical(request):
    return render(request, 'medical.html')
def add(request):
    return render(request , 'add.html')
def library(request):
    return render(request, 'library.html')

def feedback(request):
    return render(request , 'feedback.html')

def coach(request):
    return render (request , 'coach.html')

