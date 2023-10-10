from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

 

 

# Create your views here.

def signIn(request):
    if request.method =='POST':
        Username = request.POST['username']
        Password1 = request.POST['password']
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, 'Successfully signed in!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return  render(request, "./Accounts/signIn.html")  
    return render(request, './Accounts/signIn.html')

def signUp(request):
    if request.method == 'POST':
        Email = request.POST['email']  # inside the [] should be the id name of the tag/element
        Username = request.POST['username']  
        Password1 = request.POST['password']
        Password2 = request.POST['confirmpass']
        try:
            user = User.objects.create_user(Username='username', password1='password') # type: ignore
            login(request, user)
            messages.success(request, 'Successfully signed up and signed in!')
        except IntegrityError:
            messages.error(request, 'Username already taken. Please choose a different one.')
        if Password1 == Password2:
            user = User.objects.create(username=Username, email=Email, password=make_password(Password1))
            if user:
                user.save()
                messages.success(request,"User created successfully")
                return redirect('/')
            else:
                messages.info(request,"Something went wrong")
                return render(request, './Accounts/signUp.html')
    return render(request, './Accounts/signUp.html')

 

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out success")
    return redirect('/')

def aboutUs(request):
     return render(request, "./accounts/aboutUS.html")
 
 
def blog(request):
     return render(request, "./accounts/blog.html")
def gall(request):
     return render(request, "./accounts/gall.html")
def becomeDonor(request):
    return render(request, "./accounts/becomeDonar.html")
def findDonor(request):
    return render(request, "./accounts/findDonor.html")

def contactUs(request):
     return render(request, "./accounts/contactUs.html")
 
def whoweare(request):
     return render(request, "./accounts/whoweare.html")


def bookAppointment(request):
    return render(request, "./accounts/bookAppointment.html")

 
 
   