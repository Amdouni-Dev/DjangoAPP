from django.shortcuts import render
from django.http import HttpResponse
#from .models import Event
from django.views.generic import *
from .forms import *
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate
from .models import *
# Create your views here.
# def HomePage(req,id):
#     response='hrllo from %s'
#     return HttpResponse(response %id)
# def eventStatic(req):
#     list=[
#         {
#             'title':'title1',
#             'description':'description'
#         },
#         {
#             'title':'title2',
#             'description':'description2'
#         }
#     ]
#     return render(req,'events/StaticList.html',{'events':list})

# def EventList(request):
#     List=Event.objects.all()
#     return render(request,'events/EventsList.html',{'events':List})

# class EventListClass(ListView):
#     model=Event
#     template_name='events\EvenetListView.html'
#     context_object_name='events'
    
# class EventDetailClass(DetailView):
#     model=Event
#     template_name='events\EventDetailClass.html'
#     context_object_name='event'

# Create your views here.
 ############ Login
 
# def register(req): 
#     form=Registerform()
#     if req.method=='POST': 
#         form=Registerform(req.POST)
#         if form.is_valid():   
#             user=form.save(commit=False)
#             user.save()
#             login(req,user=user)
#             return redirect('eventLisClass')
#     return render(req, 'users/form.html',{'form':form})    

# def login(req):
#     form=loginform()
#     if req.method=='POST':
#         username=req.POST('username')         
#         pwd=req.POST('password')
#         user=authenticate(username=username,password=pwd)
#         if user is not None:
#             login(req,user)
#             return redirect('eventLisClass')
#         else:
#             return redirect('login')
#     return render(req, 'users/form.html',{'form':form})    
def login_def(req):
    form =LoginForm()
    if req.method=="POST":
        username =req.POST['username']
        pwd=req.POST['password']
        user= authenticate(req,username=username,password=pwd)
        if user is not None:
            login(req,user)
            return redirect('event_list_view')
        else:
            return redirect('login')
    return render(req,"users/form.html",{"form":form})        

def register(req):
    form = RegisterForm()
    if req.method=="POST":
        print(req.POST)
        form =RegisterForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user=user)
            return redirect('event_list_view')
       
    return render(req,"users/form.html",{"form":form})