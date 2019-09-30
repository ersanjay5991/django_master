from django import forms
from django.core import validators

from .models import User_md

class Newuserform(forms.ModelForm):
    class Meta :
        model = User_md
        fields = '__all__'