from django import forms
from django.core import validators

def check_x(value):
    if value[0].lower() != 'x':
        raise forms.ValidationError(" name start with a X")

class Formname(forms.Form):
    name = forms.CharField(validators=[check_x])
    email = forms.EmailField()
    verify_email =forms.EmailField(label= " Re enter Email ")
    text =forms.CharField(widget=forms.Textarea)
    botcap = forms.CharField(required=False,
                             widget=forms.HiddenInput,
                             validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail =all_clean_data['verify_email']

        if email != vemail:
            raise  forms.ValidationError(" make sure email match ")