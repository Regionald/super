from cgitb import html
from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .models import webSite4
from django.core.files.storage import FileSystemStorage

# Create your views here.

# Create your views here.
#@descript login/landing page
#@ GET /
def landing(request):
    print(request)
    return render(request,'diy/tourism/home.html')

def create4(request):
 if request.method == 'POST' and request.FILES['image1'] and request.FILES['image2'] and request.FILES['image3'] and request.FILES['image4']:
    heading=request.POST.get('heading')
    image1=request.FILES.get('image1')
    image2=request.FILES.get('image2')
    image3=request.FILES.get('image3')
    image4=request.FILES.get('image4')
    subHead=request.POST.get('subHead')
    content1=request.POST.get('content1')
    content2=request.POST.get('content2') 
    content3=request.POST.get('content3')
    content4=request.POST.get('content4')
    header1=request.POST.get('header1')
    header2=request.POST.get('header2') 
    header3=request.POST.get('header3')
    aboutUs=request.POST.get('aboutUs')
    adrs1=request.POST.get('adrs1')
    adrs2=request.POST.get('adrs2')
    adrs3=request.POST.get('adrs3')
    celNo=request.POST.get('celNo')
    email=request.POST.get('email')
    fss = FileSystemStorage()
    fs = FileSystemStorage()
    fz = FileSystemStorage()
    fa = FileSystemStorage()
    file = fss.save(image1.name, image1)
    filename = fs.save(image2.name, image2)
    filenam = fz.save(image3.name, image3)
    filena = fz.save(image4.name, image4)
    file_url = fss.url(file)
    upload_file_url = fz.url(filenam)
    uploaded_file_url = fs.url(filename)
    uploade_file_url = fa.url(filena)
   



    content={'heading':heading,
    'image1':image1,
    'image2':image2,
    'image3':image3,
    'image4':image4,
    'subHead':subHead,
    'content1':content1,
    'content2':content2,
    'content3':content3,
    'content4':content4,
    'header1':header1,
    'header2':header2,
    'header3':header3,
    'aboutUs':aboutUs,
    'adrs1':adrs1,
    'adrs2':adrs2,
    'adrs3':adrs3,
    'celNo':celNo,
    'email':email}
    
    companyName=request.POST.get('companyName')

    html_content=render_to_string("tourism/home.html",{'content':content,'file_url':file_url,'uploaded_file_url':uploaded_file_url,
    'upload_file_url':upload_file_url,'uploade_file_url':uploade_file_url}) 


    user=webSite4.objects.create(
        htmlString=html_content,
        companyName=companyName
    )
    return render(request,'tourism/view4.html',{'body':html_content})
    
def createWebString4(request):
      if request.method == 'POST' and request.FILES['image1'] and request.FILES['image2'] and request.FILES['image3'] and request.FILES['image4']:
         heading=request.POST.get('heading')
         image1=request.FILES.get('image1')
         image2=request.FILES.get('image2')
         image3=request.FILES.get('image3')
         image4=request.FILES.get('image4')
         subHead=request.POST.get('subHead')
         content1=request.POST.get('content1')
         content2=request.POST.get('content2') 
         content3=request.POST.get('content3')
         header1=request.POST.get('header1')
         header2=request.POST.get('header2') 
         header3=request.POST.get('header3')
         aboutUs=request.POST.get('aboutUs')
         adrs1=request.POST.get('adrs1')
         adrs2=request.POST.get('adrs2')
         adrs3=request.POST.get('adrs3')
         celNo=request.POST.get('celNo')
         email=request.POST.get('email')
         fss = FileSystemStorage()
         fs = FileSystemStorage()
         fz = FileSystemStorage()
         fa = FileSystemStorage()
         file = fss.save(image1.name, image1)
         filename = fs.save(image2.name, image2)
         filenam = fz.save(image3.name, image3)
         filena = fa.save(image4.name, image4)
         file_url = fss.url(file)
         upload_file_url = fz.url(filenam)
         uploaded_file_url = fss.url(filename)
         uploade_file_url = fa.url(filena)
    
        
         content={'heading':heading,
          'image1':image1,
          'image2':image2,
          'image3':image3,
          'image4':image4,
          'subHead':subHead,
          'content1':content1,
          'content2':content2,
          'content3':content3,
          'header1':header1,
          'header2':header2,
          'header3':header3,
          'aboutUs':aboutUs,
          'adrs1':adrs1,
         'adrs2':adrs2,
         'adrs3':adrs3,
         'celNo':celNo,
         'email':email}
         companyName=request.POST.get('companyName') 
         html_content=render_to_string("diy/tourism/home.html",{'content':content,'file_url':file_url,'uploaded_file_url':uploaded_file_url,
         'upload_file_url':upload_file_url,'uploade_file_url':uploade_file_url}) 
         user=webSite4.objects.create(
         htmlString=html_content,
         companyName=companyName
         )

         return render(request,'diy/complete4.html',{'body':html_content,'companyName':companyName})
      return render(request,'diy/tourism/create4.html')

def webSites4(request,cName):
    html_content=webSite4.objects.get(companyName=cName).htmlString
    return render(request,'diy/tourism/view4.html',{'container':html_content,'companyName':cName})