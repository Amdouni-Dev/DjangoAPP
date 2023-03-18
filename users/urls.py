from django.urls import path
from .views import register

urlpatterns = [
    # fonction
    path('register',register,name='register'), 
    # path('loginform',loginform,name='loginform'), 


     

    ]
