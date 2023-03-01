from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import *
from .models import Event
from .forms import EventForm,EventModelForm
from django.urls import reverse_lazy


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



    








# Create your views here.
