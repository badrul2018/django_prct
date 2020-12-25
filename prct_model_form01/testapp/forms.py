from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from testapp.models import StudModel


class StudForm(forms.ModelForm):
    
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name) <=4:
            raise  ValidationError('length greather then 4')
        return name    
    def clean_roll(self):
        roll=self.cleaned_data['roll']
        if len(roll) <=2:
            raise ValidationError('len should be > then 2')
        return roll    
    def clean_email(self):
        email=self.cleaned_data=['email']
        if len(email)<=7:
            raise ValidationError('length Problem')
        return email    
    def clean_mark(self):
        mark=self.cleaned_data['mark']
        if mark <=75:
            raise ValidationError('mark > =75 ') 
        return mark    
    
   

    class Meta:
        model=StudModel
        fields=('name','roll','email','mark')                   