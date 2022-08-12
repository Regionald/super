from django.urls import path
from .import views
from django.urls import path

app_name = 'link'

urlpatterns = [
    path('', views.landing, name='login'),
    path('user/',views.user,name='user'),
    path('signup/',views.signup, name='signup'),
    path('index/',views.index, name='index'),

]