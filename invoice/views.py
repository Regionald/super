from django.shortcuts import render
#https://coolors.co/palette/0a0908-22333b-eae0d5-c6ac8f-5e503f
# Create your views here.
def home(request):
    return render(request,'invoice/login.html')