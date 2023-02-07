from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import *
# Create your models here.
def validMail(value):
    if not str(value).endswith("@esprit.tn"):
        raise ValidationError("mail")
    return value

def ValidLength(value):
    if len(value)!=8:
        raise ValidationError("le longueur de num cin doit avoir 8 caracteres")
    return value 
class Person(AbstractUser):
    cin=models.CharField(primary_key=True, max_length=255,validators=[MinLengthValidator(8,message='La valeur doit contenir au moins 8 caracteres '),MaxLengthValidator(8,"La valeur doit avoir au max 8 caracteres ")])
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=10,unique=True)
    USERNAME_FIELD='username'
    def __str__(self):
        return self.username
    
