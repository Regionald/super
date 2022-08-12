from django.urls import path
from . import views
from . import medi
from . import tourism

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('log/', views.log, name='log'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('medical/', medi.landing, name='medical'),
    path('med/', views.med, name='med'),
    path('tourism/', views.tourism, name='tourism'),
    path('edu/', views.edu, name='edu'),
    path('clean/', views.clean, name='clean'),

    # education website route
    path('create/',views.createWebString,name='respond with choosen website'),
    path('create/',views.createWebString,name='respond with the form'),
    path('create/webfying/',views.create,name='create html content'),
    path('urls/<str:cName>/',views.webSites,name='show different websites'),

    # cleaning website route
    path('make/',views.createWebString2,name='respond with choosen website'),
    path('make/',views.createWebString2,name='respond with the form'),
    path('make/webfying/',views.make,name='create html content'),
    path('url/<str:cName>/',views.webSites2,name='show different websites'),

    # medical service route
    path('create3/',medi.createWebString3,name='respond with choosen website'),
    path('create3/',medi.createWebString3,name='respond with the form'),
    path('create3/webfying/',medi.create3,name='create html content'),
    path('urlz/<str:cName>/',medi.webSites3,name='show different websites'),

    # tourism service route
    path('create4/',tourism.createWebString4,name='respond with choosen website'),
    path('create4/',tourism.createWebString4,name='respond with the form'),
    path('create4/webfying/',tourism.create4,name='create html content'),
    path('ursl/<str:cName>/',tourism.webSites4,name='show different websites'),

 
]
