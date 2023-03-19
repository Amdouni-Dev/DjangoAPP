from django.urls import path
from .views import *
urlpatterns = [
    # fonction
    path('',getEvents,name='getEvents'),
    path('add',addEvent,name='addEvent'),
    path('update/<int:id>',updateEvent,name='updateEvent'),
    path('delete/<int:id>',deleteEvent,name='deleteEvent'),

    

    

     

    ]
