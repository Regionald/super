from cgitb import html
from django.db import models

# Create your models here.
class webSite(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')

class webSite2(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')
  
class webSite3(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')   
    
class webSite4(models.Model):
    htmlString = models.TextField()
    companyName = models.CharField(max_length=60,default='No name')   
    
  
