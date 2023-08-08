from django import forms
from .models import crop_loan
from django.contrib.auth.models import User

class cropForm(forms.ModelForm):
    class Meta:
        model=crop_loan
        fields='__all__'
    def clean_name(self):
        data=self.cleaned_data['NAME']
        if data.lower() in ['rohit','sagar','prashant']:
            return data
        else:
            raise forms.ValidationError('Not valid name')
    def clean_city(self):
        data=self.cleaned_data['city']
        if data.lower() in ['mumbai','pune']:
            return data
        else:
            raise forms.ValidationError('Not valid name')
class signupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']


