from distutils.log import error
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import stripe
from .models import User
from django.contrib.auth import authenticate,login,logout



def index(request):
    return render(request, 'link/index.html')
def landing(request):
    return render(request,'link/login.html')

def user(request):
    if request.method == 'POST':
       email=request.POST.get('email')
       username=request.POST.get('email')
       password=request.POST.get('password')
    #    print(email,password)
       try:
        user=User.objects.get(email=email)
        print('email exist',user)
       except:
        print('use no exist')
        messages.error(request, 'Username OR password does not exit')

       user=authenticate(request,username=username,password=password)#,password=password) 
       print(3,user)
       if user is not None:
           login(request,user)
           print('print is not None')
           return redirect('/link/index/')
           print(request.user)
           return redirect('/link/')


def signup(request):
    if request.method == 'POST':
       email=request.POST.get('email')
       password=request.POST.get('password')
       username=request.POST.get('email')
       companyName=request.POST.get('companyName')
       companyAddress=request.POST.get('companyAddress')
       town=request.POST.get('town')
       postalCode=request.POST.get('postalCode')
       accountNumber=request.POST.get('accountNumber')
       logoName=request.FILES.get('logoName')
       print(email)
       try: 
         print('Try')
         user=User.objects.create(
         email=email,
         #password=password,
         username=username,
         companyName=companyName,
         companyAddress=companyAddress,
         town=town,
         postalCode=postalCode,
         accountNumber=accountNumber,
         avatar=logoName)
         user.set_password(password)
         user.save()
         return redirect('/link/')

       except:
           print('there is error')
           print(error)
    else:
        user = User()
        return render(request, 'link/signup.html', {'user': user})










	# if request.method == "POST":
    #         email=request.POST.get('email')
    #         password=request.POST.get('password')
    #         username=request.POST.get('email')
    #         companyName=request.POST.get('companyName')
    #         companyAddress=request.POST.get('companyAddress')
    #         town=request.POST.get('town')
    #         postalCode=request.POST.get('postalCode')
    #         accountNumber=request.POST.get('accountNumber')
    #         logoName=request.FILES.get('logoName')
    #             try:
    #         user=User.objects.create(email=email,username=username,companyName=companyName,companyAddress=companyAddress,town=town,postalCode=postalCode,accountNumber=accountNumber,avatar=logoName)
    #         user.set_password(password)
    #         user.save()
    #         return redirect('link:login')
    #         # return redirect('link:login')	
	# else:
	# 	 user = User()
	# return render(request, 'link/signup.html', {'user': user})


	
	