from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *

class UserCrationForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields=('phone','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise ValidationError('Passwords is not Mach')
        return cd['password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('phone','email','password','last_login')


# Authenticated User Login or...

class LoginForm(forms.Form):
    phone=forms.CharField(max_length=11)
    password=forms.CharField(max_length=255)

class SingupForm(forms.Form):
    phone=forms.CharField(max_length=11)
    email=forms.EmailField()
    password=forms.CharField()
    #password2=forms.CharField()

class VeryfySingupForm(forms.Form):
    code=forms.IntegerField()