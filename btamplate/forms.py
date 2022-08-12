from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Formi
from django.forms import ModelForm

class updateTemplate(forms.ModelForm):
    class Meta:
        model = Formi
        fields = ['pro_date', 'name','role','logo','summary','project','limitations','approach','benefits',
        'opportunities','nobel','threat','financial','risk']
 
class createForm(forms.Form):
    class Meta:
        model = Formi
        fields = ['pro_date','name','role','logo','summary','project','limitations','approach','benefits',
        'opportunities','nobel','threat','financial','risk']

