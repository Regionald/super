from email.policy import default
from itertools import product
from sqlite3 import Date
from sys import maxsize
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.s

class User(AbstractUser):

    email = models.CharField(unique=True,max_length=60)
    password = models.CharField(max_length=150)
    companyName=models.CharField(max_length=100,default='No name')
    companyAddress=models.CharField(max_length=100,default='No address')
    town=models.CharField(max_length=50,default='no town')
    postalCode=models.IntegerField(default=1540)
    accountNumber=models.IntegerField(default=1541048928)
    logoName=models.CharField(max_length=100,default='logo')
    avatar =models.ImageField(null=True,default="images.png")
    verified=models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




    