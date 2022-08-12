from cgitb import html
from copyreg import clear_extension_cache
import datetime
from django.db.models import Sum
import email
from email.policy import HTTP
from functools import lru_cache
from importlib.resources import contents
from multiprocessing import context
from multiprocessing.connection import Client
from pickle import TRUE
from pickletools import read_bytes4
from re import sub
from django.shortcuts import render,redirect
import operator
from invoice.models import Clients
from link.models import User
from django.contrib import messages
from django.http import HttpResponse
import os
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
#os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
#os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\lib\girepository-1.0")
#from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#@descript /page after succeful loging
#@ GET /invoice/

def invoice(request):
    client=Clients.objects.filter(email=request.user).values()
    if request.method == 'POST':
       clientName=request.POST.get('clientName')
       print(clientName)
       client=Clients.objects.filter(clientName=clientName)
       print(client)
    return render(request,'invoice/invoice.html',{'client':client})

def revenue(request):
    client=Clients.objects.filter(email=request.user).values()
    total=Clients.objects.filter(email=request.user).aggregate(Sum('Total'))
    subTotal=Clients.objects.filter(email=request.user).aggregate(Sum('subTotal'))
    tax=total['Total__sum']-subTotal['subTotal__sum']
    tax=round(tax,2)
    print('salary')
    print(total)
    if request.method == 'POST':
       clientName=request.POST.get('clientName')
       print(clientName)
       client=Clients.objects.filter(clientName=clientName)
       total=Clients.objects.filter(clientName=clientName,email=request.user).aggregate(Sum('Total'))
       print('salary')
       print(total)
    return render(request,'invoice/revenue.html',{'client':client,'total':total,'subTotal':subTotal,'tax':tax})

#@descript /create invoice 
#@ GET /invoice/create
def create(request):
    if request.method == 'POST':
       date=datetime.date.today()
       clientName=request.POST.get('name')
       clientAddress=request.POST.get('address')
       clientTown=request.POST.get('town')
       clientpostalCode=request.POST.get('code')
       descript=request.POST.getlist('descript')
       rate=request.POST.getlist('rate')
       dueDate=request.POST.get('dueDate')
       clientEmail=request.POST.get('clientEmail')
       qty=request.POST.getlist('qty')
       
       rate=[float(i) for i in rate]
       qty=[int(i) for i in qty]
       
       amount=list(map(operator.mul,rate,qty))
       print('ammount',amount)
       products=[{'descpript': descript, 'rate': rate,'qty':qty,'amount':amount} for descript, rate,qty,amount in zip(descript, rate,qty,amount)]
       total=sum(amount)
       print('total',total)
       subTotal=0
       vat=0
       if request.POST.get('typeOFinvoice')=='Tax invoice':
        subTotal=round(0.85*total,2)
        vat=round(0.15*total,2)
       print(request.user)
       try :
         clientCreateInvoice=Clients.objects.create(
         email=request.user,
         clientName = clientName,
         clientAddress =clientAddress,
         clientTown=clientTown,
         clientpostalCode=clientpostalCode,
         products=products,
         clientEmail=clientEmail,
         dueDate=dueDate,
         subTotal=subTotal,
         status='notSent',
         date=date,
         vat=vat,
         Total=total,)
       except:
        messages.error(request, 'Username OR password does not exit')
    return redirect('/invoice/')

def download(request,id):
  invoice=Clients.objects.filter(id=id).values()
  userDetails=User.objects.get(email=request.user)
  print(userDetails)
  return render(request,'invoice/download.html',{'client':invoice,'user':userDetails})

def delete(request,id):
  invoice=Clients.objects.filter(id=id)
  if request.method == 'POST':
    invoice.delete()
    return redirect('/invoice/')
  return render(request, 'invoice/delete.html', {'obj': id})

def copy(request,id):
  invoice=Clients.objects.filter(id=id).values()
  userDetails=User.objects.get(email=request.user)
  if request.method == 'POST':
    dueDate=request.POST.get('dueDate')
    try:
     invoice=Clients.objects.get(id=id)
     invoice.id=None
     invoice.status='notSent'
     invoice.dueDate=dueDate
     invoice.save()
     return redirect('/invoice/')
    except:
     print('error')
     
  return render(request,'invoice/copy_invoice.html',{'client':invoice,'user':userDetails})

def editInvoice(request,id):
   invoice=Clients.objects.filter(id=id).values()
   userDetails=User.objects.get(email=request.user)
   if request.method == 'POST':
     print(id)
     clientName=request.POST.get('name')
     clientAddress=request.POST.get('address')
     clientTown=request.POST.get('town')
     clientpostalCode=request.POST.get('code')
     dueDate=request.POST.get('dueDate')
     clientEmail=request.POST.get('clientEmail')
     try: 
        Clients.objects.filter(id=id).update(
         clientName=clientName,
         clientAddress=clientAddress,
         clientTown=clientTown,
         clientpostalCode=clientpostalCode,
         dueDate= dueDate,
         clientEmail=clientEmail
         )
        return redirect('/invoice/')
     except:
        print('there is an error')

   return render(request,'invoice/edit_invoice.html',{'client':invoice,'user':userDetails})

@lru_cache()
def logo_data():
  with open(finders.find('images/A_UdwzmPQ.png'),'rb') as f:
    logo_data=f.read()
  logo=MIMEImage(logo_data)
  logo.add_header('Content-ID','<logo>')
  return logo

def sendEmail(request,id):
  status='sent'
  send=Clients.objects.filter(id=id).values()
  email=Clients.objects.filter(id=id).first()
  emailClient=email.clientEmail
  emailSME=email.email
  to=[emailClient,emailSME]
  html_content=render_to_string("invoice/email_template.html",{'client':send})
  text_contect=strip_tags(html_content)
  print(text_contect)

  email=EmailMultiAlternatives(
    'Testing',
    text_contect,
    'regionaldmongwe@gmail.com',
    to
  )
  email.attach_alternative(html_content,"text/html")
  Clients.objects.filter(id=id).update(status=status)
  email.attach(logo_data())
  email.mixed_subtype='related'
  email.send()
  return redirect('/invoice/')





















# source codes weasy print
 #'''response=HttpResponse(content_type='application/pdf')
 #  response['Content-Disposition']='attachement;filename'+\
 #   str(datetime.datetime.now())+'.pdf'
 #  response['Content-Transfer-Encoding']='binary'
 # html_string=render_to_string('invoice/download.html')
  #html=HTML(string=html_string)
  #result=html.write_pdf()

  #with tempfile.NamedTemporaryFile(delete=True) as output:
  #  output.write(result)
  #  output.flush()
  # output=open(output.name,'rb')
  #  response.write(output.read())
  #return response''' 

