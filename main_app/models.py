from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):

    name = models.CharField(max_length=200, default='Unnamed Country')
    image = models.URLField(max_length=400, default='No Image URL')
    capital = models.CharField(max_length=200, default='No Capital')
    language = models.CharField(max_length=200, default='No Language')
    currency = models.CharField(max_length=200, default='No Currency')
    population = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Destination(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="destinations")
    best_time_to_visit = models.CharField(max_length=200)
    budget_range = models.CharField(max_length=200)
    image = models.URLField(max_length=400, default='No Image URL')
    
    def __str__(self):
        return self.title

class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    countries = models.ManyToManyField(Country, related_name="itineraries")
    destinations = models.ManyToManyField(Destination, related_name="itineraries")

    def __str__(self):
        return self.name

class TravelDestination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    best_time_to_visit = models.CharField(max_length=200)
    budget_range = models.CharField(max_length=200)
    image = models.URLField(max_length=400, default='No Image URL')
