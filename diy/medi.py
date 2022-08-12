from cgitb import html
from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .models import webSite3
from django.core.files.storage import FileSystemStorage

# Create your views here.

# Create your views here.
#@descript login/landing page
#@ GET /
def landing(request):
    print(request)
    return render(request,'diy/medical/home.html')

def create3(request):
 if request.method == 'POST' and request.FILES['picture']:
    heading=request.POST.get('heading')
    picture=request.FILES.get('picture')
    subHead=request.POST.get('subHead')
    content1=request.POST.get('content1')
    content2=request.POST.get('content2') 
    content3=request.POST.get('content3')
    content4=request.POST.get('content4')
    aboutUs=request.POST.get('aboutUs')
    adrs1=request.POST.get('adrs1')
    adrs2=request.POST.get('adrs2')
    adrs3=request.POST.get('adrs3')
    celNo=request.POST.get('celNo')
    email=request.POST.get('email')
    fss = FileSystemStorage()
    file = fss.save(picture.name, picture)
    file_url = fss.url(file)
  

    content={'heading':heading,
    'picture':picture,
    'subHead':subHead,
    'content1':content1,
    'content2':content2,
    'content3':content3,
    'content4':content4,
    'aboutUs':aboutUs,
    'adrs1':adrs1,
    'adrs2':adrs2,
    'adrs3':adrs3,
    'celNo':celNo,
    'email':email}
    
    companyName=request.POST.get('companyName')

    html_content=render_to_string("medical/medic.html",{'content':content,'file_url':file_url }) 


    user=webSite.objects.create(
        htmlString=html_content,
        companyName=companyName
    )
    return render(request,'medical/view3.html',{'body':html_content})
    
def createWebString3(request):
      if request.method == 'POST' and request.FILES['picture']:
         heading=request.POST.get('heading')
         picture=request.FILES.get('picture')
         subHead=request.POST.get('subHead')
         content1=request.POST.get('content1')
         content2=request.POST.get('content2') 
         content3=request.POST.get('content3')
         content4=request.POST.get('content4')
         aboutUs=request.POST.get('aboutUs')
         adrs1=request.POST.get('adrs1')
         adrs2=request.POST.get('adrs2')
         adrs3=request.POST.get('adrs3')
         celNo=request.POST.get('celNo')
         email=request.POST.get('email')
         fss = FileSystemStorage()
         file = fss.save(picture.name, picture)
         file_url = fss.url(file)

         content={'heading':heading,
          'picture':picture,
          'subHead':subHead,
         'content1':content1,
         'content2':content2,
          'content3':content3,
          'content4':content4,
          'aboutUs':aboutUs,
          'adrs1':adrs1,
           'adrs2':adrs2,
         'adrs3':adrs3,
         'celNo':celNo,
         'email':email}
         companyName=request.POST.get('companyName') 
         html_content=render_to_string("diy/medical/medic.html",{'content':content,'file_url':file_url}) 
         user=webSite3.objects.create(
         htmlString=html_content,
         companyName=companyName
         )

         return render(request,'diy/complete3.html',{'body':html_content,'companyName':companyName})
      return render(request,'diy/medical/create3.html')

def webSites3(request,cName):
    html_content=webSite3.objects.get(companyName=cName).htmlString
    #print(html_content)
    return render(request,'diy/medical/view3.html',{'container':html_content,'companyName':cName})