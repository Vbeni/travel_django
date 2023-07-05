from django.contrib import admin
from .models import Country, Destination, Itinerary

admin.site.register(Country) 
admin.site.register(Destination)
admin.site.register(Itinerary)