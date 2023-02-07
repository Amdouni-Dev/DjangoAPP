from django.contrib import admin
from events.models import Event # wila hakka from .models import Event khter deja f west l dosier events
from events.models import Participation
# Register your models here.
@admin.register(Event)
class eventadmin(admin.ModelAdmin):
    #pass # l class fergha
    list_display=('title','state','category') # tableau fih hedhom meaach tjini form d'ajout 
    list_filter=('title','state','category')
    ordering=('title','state','category') # ordre 
    search_fields=['title','category']
# admin.site.register(Event,eventadmin)
admin.site.register(Participation)


#Personnalistaion
