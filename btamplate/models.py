from django.db import models
from datetime import date


class Formi(models.Model):
    pro_date = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='media/')
    summary = models.TextField()
    project = models.TextField()
    limitations = models.TextField()
    approach = models.TextField()
    benefits = models.TextField()
    opportunities = models.TextField()
    nobel = models.TextField()
    threat = models.TextField()
    financial = models.TextField()
    risk = models.TextField()
    def __str__(self):
        return self.pro_date



