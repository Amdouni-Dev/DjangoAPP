from django.urls import path
from .views import *

urlpatterns = [
    # fonction
    path('homepage/<int:id>',HomePage,name='HomePage'), # http://localhost:8000/events/homepage/1  ==>hello from 1
    path('eventsStatic',eventStatic,name='eventStatic'), 
    path('listevent',eventList,name='eventList'),
    path('createEvent',createEventEorm,name='createEvent'),
    path('createEventModelForm',createEventModelForm,name="createEventModelForm"),
    # class
    path('eventLisClass',EventListClass.as_view(),name="eventLisClass"),
    path('EventDetailClass/<int:pk>',EventDetailClass.as_view(),name="EventDetailClass"),
    path('createEvent',createEvent.as_view(),name="createEvent"),
    path('ModelUpdateView/<int:pk>',ModelUpdateView.as_view(),name="ModelUpdateView")
     

    ]
