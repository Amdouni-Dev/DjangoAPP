from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from events.models import Event
from .Serializers import EventSerializer
@api_view(['GET'])
def getEvents(req):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True) 
    return Response(serializer.data,status=status.HTTP_200_OK)  
# Create your views here.
@api_view(['POST'])
def addEvent(req):
    serializer=EventSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
def updateEvent(req, id=None):
    event=Event.objects.get(id=id)
    serializer=EventSerializer(instance=event,data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','DELETE'])
def deleteEvent(req,id=None):
    try:
        event=Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response(status="Event not found")    
    event.delete
    return Response("Event deleted")