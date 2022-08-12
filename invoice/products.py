from django.shortcuts import redirect, render
from .models import Products
from django.contrib import messages

def admin(request):
  if request.method == 'POST':
     print(request)
     category=request.POST.get('category')
     name=request.POST.get('name')
     price=request.POST.get('price')
     qty=request.POST.get('qty')
     avater=request.FILES.get('avater')
     print(category,name,price,qty,avater)

     try:
        user=Products.objects.create(
         username=request.user,
         category=category,
         name=name,
         price=price,
         descript=qty,
         avater=avater,
        )
        print('email exist',user)
     except:
        messages.error(request, 'username or password does not exist')
     #return redirect("products/")

  return render(request, "invoice/admin.html", {})

def productList(request):
   data=Products.objects.filter(username=request.user)
   return render(request,"invoice/products.html",{'product':data})

def delete(request,id):
  product=Products.objects.filter(id=id)
  if request.method == 'POST':
    product.delete()
    return redirect('/')
  return render(request, 'invoice/delete.html', {'obj': id})

def edit(request,id):
   product=Products.objects.filter(id=id).values()
   print(product)
   if request.method == 'POST':
     print(id)
     category=request.POST.get('category')
     name=request.POST.get('name')
     price=request.POST.get('price')
     qty=request.POST.get('qty')
     avater=request.FILES.get('avater')
     print(category,name,price,qty,avater)
     try: 
        user=Products.objects.filter(id=id).update(
         category=category,
         name=name,
         price=price,
         descript=qty,
         )
      #   return redirect('/')
     except:
        print('there is an error')

   return render(request,'invoice/edit.html',{'product':product})