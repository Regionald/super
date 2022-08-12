from django.shortcuts import render
from .models import Products
# Create your views here.

def catalog(request,name):
   data=Products.objects.filter(username=request.user)
   if request.method == 'POST':
        search=request.POST.get('search')
        category=request.POST.get('category')
        print(name)
        print(search,category)
        data=Products.objects.filter(brand=search)
   return render(request,"invoice/catalog.html",{'product':data})