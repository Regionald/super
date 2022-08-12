from asyncio.windows_events import NULL
from distutils.log import error
from django.shortcuts import render, redirect
from .models import Clients
from link.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
#@descript login/landing page
#@ GET /
def landing(request):
    print(request)
    if request.method == 'POST':
       email=request.POST.get('email')
       username=request.POST.get('email')
       password=request.POST.get('password')
       print(email,password)
       try:
        user=User.objects.get(email=email)
        print('email exist',user)
       except:
        messages.error(request, 'username or password does not exist')

       user=authenticate(request,username=username,password=password)
       print(3,user)
       if user is not None:
           login(request,user)
           print('print is not None')
           return redirect('/home/')
    return render(request,'invoice/login.html')


#@descript login userName and password Validation
#@ Post /user

def user(request):
    if request.method == 'POST':
       email=request.POST.get('email')
       username=request.POST.get('email')
       password=request.POST.get('password')
       print(email,password)
       try:
        user=User.objects.get(email=email)
        print('email exist',user)
       except:
        print('use no exist')
        messages.error(request, 'Username OR password does not exist')

       user=authenticate(request,username=username,password=password)#,password=password) 
       print(3,user)
       if user is not None:
           login(request,user)
           print('print is not None')
           return redirect('/home/')
    print(request.user)
    return redirect('/')




#@descript /page after succeful loging
#@ GET /invoice/
def home(request):
    return render(request,'invoice/index.html')

def logOut(request):
  logout(request)
  return redirect('/')