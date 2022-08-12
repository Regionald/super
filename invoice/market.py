from django.shortcuts import render
from .models import Products
# Create your views here.

def market(request):
   data=Products.objects.filter()
   if request.method == 'POST':
        search=request.POST.get('search')
        category=request.POST.get('category')
        print(search,category)
        data=Products.objects.filter(brand=search)
   return render(request,"invoice/market.html",{'product':data})