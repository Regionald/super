from distutils.log import error
from email import message
from django.shortcuts import render, redirect
from .models import Clients
from link.models import User
from django.contrib import messages

#@descript create account
#@ POST /account/create

def createUserAccount(request):
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
         messages.error(request, 'Sign up successful !!! Log in using your new credentials')

       except:
           print('there is error')
           messages.error(request, 'Username name already exists')
           print(error)

       return redirect('/')

def profile(request):
   userDetails=User.objects.get(email=request.user)
   return render(request,'invoice/edit_profile.html',{'user':userDetails})

def profileUpdate(request):
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
         print(companyName)
         User.objects.filter(username=request.user).update(
           email=email,
         username=username,
         companyName=companyName,
         companyAddress=companyAddress,
         town=town,
         postalCode=postalCode,
         accountNumber=accountNumber,
         avatar=logoName
         )
    
       except:
           print('there is an error')
           print(error)

       return redirect('/')

def picUpload(request):
  if request.method == 'POST':
      
       logoName=request.FILES.get('logoName')
       try: 
         print('Try')
         User.objects.filter(username=request.user).update(
         avatar=logoName
         )
    
       except:
           print('there is an error')
           print(error)

       return redirect('/')