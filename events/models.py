from django.db import models
from users.models import *
from datetime import date
from django.core.exceptions import *
<<<<<<< HEAD
from django.core.validators import * # import MinValueValidator
from  django.utils.timezone import datetime
=======

>>>>>>> 6a021e69174838032b64d50400a85523401b98bd
def isDateIsValid(value):
    if value <=  date.today():
        raise ValidationError("invalid date")
    return value
<<<<<<< HEAD
def TitleValid(value):
    if not value[0].isupper():
        raise ValidationError("La valeur doit commencer par un caractere en maj ")
    return value
=======
        
>>>>>>> 6a021e69174838032b64d50400a85523401b98bd
# Create your models here.
class Event(models.Model): # heritage ==> models.Model
    categories=(('musique','musique'),
                ('cinema','cinema'),
                ('sport','sport')
                )
<<<<<<< HEAD
    title= models.CharField(max_length=255,validators=[TitleValid]) # maxLength est obligatoire 
=======
    title= models.CharField(max_length=255) # maxLength est obligatoire 
>>>>>>> 6a021e69174838032b64d50400a85523401b98bd
    description=models.TextField() # nafsha chartfield ema akber 
    image=models.ImageField(upload_to='images/')  # /Media/Images 
    category=models.CharField(max_length=255,choices=categories)
    state=models.BooleanField(default=False)
<<<<<<< HEAD
    nbrParticipants=models.IntegerField(default=0,validators=[MinValueValidator(limit_value=0,message="la valeur doit etre positif ")])
    # dateEvent=models.DateField(validators=[isDateIsValid])
    dateEvent=models.DateField()
    
=======
    nbrParticipants=models.ImageField(default=0)
    dateEvent=models.DateField(validators=[isDateIsValid])
>>>>>>> 6a021e69174838032b64d50400a85523401b98bd
    created_at=models.DateTimeField(auto_now_add=True) #  auto_now_add==> tetbadel l created At 
    updated_at=models.DateTimeField(auto_now=True)# ki naamel update
    
    
    # associations
    organizer=models.ForeignKey(Person, on_delete=models.CASCADE) # 
    participations=models.ManyToManyField(Person,related_name='Participation',through='Participation')
    #related name==> esm l objet 
<<<<<<< HEAD
    # Meta predefine deja
    def __str__(self):
        # todhherli ki nekli aala add:fou9 l formulaire 
        return f'{self.title} and {self.state}' # naamel affichage l hajtyn fel input 
        #return self.title 
    class Meta:
        verbose_name='Details des evenements'

        constraints=[models.CheckConstraint(check=models.Q(dateEvent__gte=datetime.now()), # pour les operations logiques =>  OU,XOR,OR,&&
                                            name="la date est  invalide")]
    
class Participation(models.Model):   
    participationDate=models.DateField( auto_now=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE) 
  
    class Meta:
        verbose_name="Details Participation"
        unique_together=('person','event')  # lezem ykoun les clés unique khater ynajem yparticpi mara khw    
            
            
            
=======
class Participation(models.Model):   
    participationDate=models.DateField( auto_now=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)        
>>>>>>> 6a021e69174838032b64d50400a85523401b98bd
