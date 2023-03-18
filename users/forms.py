from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class Registerform(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['cin','username','first_name','last_name','email','password1','password2']
    def save(self,commit=True):
        return super(Registerform,self).save(commit)

