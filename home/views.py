import http
from urllib import request
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm

def user_reg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()
       
    else:
        form = RegisterForm()
    return render(request,'registration.html',{"form":form})

def user_login(request) :
    

    if request.method == 'POST' :
        username=request.POST['username']
        password =request.POST['password']
        user = authenticate(username = username , password = password )
        if user is not None :
            login(request, user)
            return redirect('home')
        else :
              messages.error(request,'username or password not correct')
 
    return render ( request , 'login.html')
 

def home ( request ) :
    if not request.user:
        return redirect ("login_user")
    return render ( request,'home.html')
    



def user_logout ( request ) :
    logout(request)
    return redirect ("login_user")