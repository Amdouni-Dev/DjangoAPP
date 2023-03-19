from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import *
from .models import Event,Participation
from .forms import EventForm,EventModelForm,DeleteEventForm,EventModelFormPArticipation
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import date
#kol methode leezem traja3 objet http response
def HomePage(req,id):
    response='hello from %s'
    return HttpResponse(response %id)

def eventStatic(req):
    list=[
        {
            'title': 'title1',
            'description': 'description1'
        },
        {
            'title': 'title2',
            'description': 'description2'


        }
    ]
    return render(req,'events/StaticList.html',{'events':list})

def eventList(req):
    List=Event.objects.filter(state=True) # ya3meli filter lel les evenements eli aandhom state=true
    return render(req,'events/eventsList.html',{'events':List})


 
def event_participant(req,id):
    obj = Event.objects.get(id=id)
    count=obj.participations.count()
    return count  
     
################Classsssss
class EventListClass(ListView):
 
    model=Event
    template_name='events/eventsList.html'

    context_object_name='events' # nabaathou bech tsir aalih l boucle
    
    
    
class EventDetailClass(DetailView):
    model=Event
    template_name='events/eventDetailClass.html'
    context_object_name='event' 

######### def crud
def createEventEorm(req):
    form=EventForm()
    if req.method=='POST':
        form=EventForm(req.POST,req.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect('eventLisClass')
        else:
            print(form.errors)
    return render(req,'events/createEvent.html',{'form':form})
            

def createEventModelForm(req):
    if req.method=='GET':
        form=EventModelForm()
        return render(req,'events/createEvent.html',{'form':form})
    if req.method == 'POST':
        form=EventModelForm(req.POST, req.FILES)
        if form.is_valid():
            Event=form.save(commit=False)
            Event.save()
            return redirect('eventLisClass')
        else:
            return render(req,'events/createEvent.html',{'form':form})
#ahsen wahda fel exam CreateView
class createEvent(CreateView): #CreateView est une classe générique Django qui fournit une vue pour créer un nouvel objet dans une base de données.
    model=Event # spécifier le modèle
    template_name='events/createEvent.html'
    form_class=EventModelForm #spécifier la classe de formulaire associée à la vue. 
    success_url=reverse_lazy('eventLisClass') #spécifier l'URL de redirection après la création réussie de l'objet Event

class ModelUpdateView(UpdateView):
    model=Event
    template_name='events/createEvent.html'
    form_class=EventModelForm
    success_url=reverse_lazy('eventLisClass')
    
class ModelDeleteView(DeleteView):
    model=Event
    template_name='events/deleteEvent.html'
    success_url=reverse_lazy('eventLisClass')
class ModelDeleteParticipation(DeleteView):
    model=Event.participations
    template_name='events/deleteParticipation.html'
    success_url=reverse_lazy('eventLisClass')    
class DeleteEventView(DeleteMessageMixin, FormView):
    model = Event
    form_class = DeleteEventForm
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('eventLisClass')
def increment_number(id, increment_by):
    # Retrieve the object from the database
    obj = Event.objects.get(id=id)

    # Increment the number
    obj.nbrParticipants += increment_by

    # Save the object with the new value
    obj.save()
def increment_numberParticipation(id, increment_by):
    # Retrieve the object from the database
    obj = Event.objects.get(id=id)

    # Increment the number
    obj.participations += increment_by

    # Save the object with the new value
    obj.save()    
def IncrementNbParticipants(req,id):
    event=Event.objects.get(id=id)
    increment_number(id, 1)
    count= event.participations.count()
    return HttpResponse(f"Le nombre de partipant pour levenement  {event.title} est incrementé par 1 {count} ")

def IncrementNbParticipation(req,id):
    event=Event.objects.get(id=id)
    increment_number(id, 1)
    return HttpResponse(f"Le nombre de participation pour levenement  {event.title} est incrementé par 1")   

             
 
class AddParticipation(UpdateView):
    model=Event
    template_name='events/createEvent.html'
    form_class=EventModelFormPArticipation
    success_url=reverse_lazy('eventLisClass')  
class EventPartipations(DetailView):
    model=Event
    template_name='events/eventDetailClass.html'
    context_object_name='event' 
def supprimer_participation(request, id):
    evenement = get_object_or_404(Event, pk=id) #from django.shortcuts import get_object_or_404, redirect
    participation = get_object_or_404(Participation, event=evenement)
    participation.delete()
    return redirect('eventLisClass', id=id)    
        
              



    








# Create your views here.
@login_required(login_url="login")
def create_event(request):
    form=EventForm()
    if request.method == "POST":
        form=EventForm(request.POST,request.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect('event_list_view')
        else :
            print(form.errors)
    return render(request,"events/event_form.html",{'form' :form})

def add_event(req):
    if req.method =="GET":
        form =EventModelForm()
        return render(req,"events/event_form.html",{'form' :form})
    if req.method =="POST":
        form= EventModelForm(req.POST,req.FILES)
        if form.is_valid():
            Event= form.save(commit=False)
            Event.save()
            return redirect('event_list_view')
        else :
            return render(req,"events/event_form.html",{'form' :form})

def participate(req, event_id):
    user = req.user
    event = Event.objects.get(id=event_id)
    if Participation.objects.filter(person=user, event=event).count() == 0:
        part = Participation.objects.create(person=user, event=event, participationDate=date.today)
        part.save()
        event.nbrParticipants += 1
        event.save()
        return redirect('event_list_view')
    else:
        return HttpResponse('You have already participated in this event.')
    user=req.user
    event=Event.objects.get(id=event_id)
    if Participation.objects.filter(person=user,event=event).count() ==0:
        part=Participation.objects.create(person=user,event=event,participationDate=date.today)
        part.save()
        event.nbr_participant+=1
        event.save()
        return redirect('event_list_view')
class EventListClass(LoginRequiredMixin,ListView):
    login_url="/users/login"
    model=Event
    template_name ='events/EventListView.html'
    context_object_name ='events'
    # queryset = Event.objects.filter(state=True)
    def get_queryset(self):
        return Event.objects.filter(state=True)
    

class EventDetail(DetailView):
    model=Event
    template_name ='events/EventDetails.html'
    context_object_name ='event'
    
    
class CreateEvent(LoginRequiredMixin,CreateView):
    login_url="/users/login"
    model =Event
    template_name="events/event_form.html"
    form_class =EventModelForm
    success_url = reverse_lazy('event_list_view')
    def form_valid(self, form) -> HttpResponse:
        form.instance.organizer = Person.objects.get(cin=self.request.user.cin)
        return super().form_valid(form)
    
class UpdateEvent(UpdateView):
    model=Event
    template_name ="events/event_form.html"
    form_class =EventModelForm
    success_url = reverse_lazy('event_list_view')
    
class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list_view')            