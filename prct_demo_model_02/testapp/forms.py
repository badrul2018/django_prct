from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from testapp.models import EmpModel

class EmpForm(forms.ModelForm):
    def clean(self):
        total_clean=super().clean()
        name=total_clean['user']
        if len(name)<=5:
            raise ValidationError('user name error')
        email=total_clean['email']
        if len(email)<=5:
            raise ValidationError('Email field error ')
    class Meta:
        model=EmpModel
        fields=('user','email')            