from email.policy import default
from itertools import product
from sqlite3 import Date
from sys import maxsize
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.s

# class User(AbstractUser):

#     email = models.CharField(unique=True,max_length=60)
#     password = models.CharField(max_length=150)
#     companyName=models.CharField(max_length=100,default='No name')
#     companyAddress=models.CharField(max_length=100,default='No address')
#     town=models.CharField(max_length=50,default='no town')
#     postalCode=models.IntegerField(default=1540)
#     accountNumber=models.IntegerField(default=1541048928)
#     logoName=models.CharField(max_length=100,default='logo')
#     avatar =models.ImageField(null=True,default="images.png")
#     verified=models.BooleanField(default=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Clients(models.Model):
    email = models.CharField(max_length=30,)
    clientName = models.CharField(max_length=60,default='No name')
    clientAddress = models.CharField(max_length=60,default='No name')
    clientTown=models.CharField(max_length=100,default='No name')
    clientpostalCode=models.IntegerField(default=1540)
    products=models.JSONField(default=dict)
    subTotal=models.FloatField(default=0)
    vat=models.FloatField(default=0)
    Total=models.FloatField(default=0)
    dueDate=models.CharField(max_length=60,null=True,blank=True)
    date=models.CharField(max_length=60,null=True,blank=True)
    status=models.CharField(max_length=60,null=True,blank=True)
    clientEmail=models.EmailField(max_length=60,null=True,blank=True)  

class Products(models.Model):
    username=models.CharField(max_length=45,default='No name')
    category=models.CharField(max_length=30,)
    name=models.CharField(max_length=30,)
    price=models.FloatField(default=0)
    descript=models.CharField(max_length=30,)
    avater=models.ImageField(null=True,default="images.png")
