from django.urls import path
from .views import *

urlpatterns = [
    # fonction
    path('homepage/<int:id>',HomePage,name='HomePage'), # http://localhost:8000/events/homepage/1  ==>hello from 1
    path('eventsStatic',eventStatic,name='eventStatic'), 
    path('listevent',eventList,name='eventList'),
    path('createEvent',createEventEorm,name='createEvent'),
    path('createEventModelForm',createEventModelForm,name="createEventModelForm"),
    path('IncrementNbParticipants/<int:id>',IncrementNbParticipants,name='IncrementNbParticipants'),
    path('IncrementNbParticipation/<int:id>',IncrementNbParticipation,name='IncrementNbParticipation'),
    path('supprimer_participation/<int:id>/supprimer_participation/', supprimer_participation, name='supprimer_participation'),
    path('participate/<int:event_id>',participate,name="participate"),
    path('listeventsView/' ,EventListClass.as_view() ,name='event_list_view'),
    path('detailsEvent/<int:pk>' ,EventDetail.as_view() ,name='event_details_view'),
    path('deleteView/<int:pk>', EventDeleteView.as_view(),
         name="Events_Delete_View"),
    path('create_event_view',CreateEvent.as_view(),name="create_event_view"),
    path('update_event_view/<int:pk>',UpdateEvent.as_view(),name="update_event_view"),
    
    # class
    path('eventLisClass',EventListClass.as_view(),name="eventLisClass"),
    path('EventDetailClass/<int:pk>',EventDetailClass.as_view(),name="EventDetailClass"),
    path('createEvent',createEvent.as_view(),name="createEvent"),
    path('ModelUpdateView/<int:pk>',ModelUpdateView.as_view(),name="ModelUpdateView"),
    path('ModelDeleteView/<int:pk>',ModelDeleteView.as_view(),name="ModelDeleteView"),
    path('DeleteEventView/<int:pk>',DeleteEventView.as_view(),name="DeleteEventView"),
    path('AddParticipation/<int:pk>',AddParticipation.as_view(),name="AddParticipation"),
    path('EventPartipations/<int:pk>',EventPartipations.as_view(),name="EventPartipations"),
    path('ModelDeleteParticipation/',ModelDeleteParticipation.as_view(),name="ModelDeleteParticipation"),
    
    
    
    

    

     

    ]
