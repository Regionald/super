from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import render_pdf_view

app_name = 'btamplate'


urlpatterns = [
    path('', views.index, name='index'),
    path('createTemplate/', views.createTemplate, name='createTemplate'),
    path('update/', views.update, name='update'),
    path('contact/', views.contact, name='contact'), 
    path('test/<object_id>/',render_pdf_view, name='test-view'),
    path('delete_template/<object_id>/',views.delete_template, name='delete_template'),
    path('update_template/<object_id>/',views.update_template, name='update_template'),
    path('email/<object_id>/', views.email, name='email'),
]
