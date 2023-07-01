from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Country
from django.views.generic.edit import CreateView


class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

class CountryList(TemplateView):
    template_name = "country_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["countries"] = Country.objects.filter(name__icontains=name)
        else:
            context["countries"] = Country.objects.all()
            context["header"] = "Trending Countries"
        return context

class TravelDestinationList(TemplateView):
    template_name = "travel_destination_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["travel_destinations"] = travel_destinations
        return context

class TravelDestination:
    def __init__(self, name, description, country, best_time_to_visit, budget_range, image):
        self.name = name
        self.description = description
        self.country = country
        self.best_time_to_visit = best_time_to_visit
        self.budget_range = budget_range
        self.image = image

class CountryCreate(CreateView):
    model = Country
    fields = ['name', 'capital', 'language', 'currency', 'population']
    template_name = 'country_create.html'
    success_url = '/countries/'

travel_destinations = [
    TravelDestination("New York City", "The city that never sleeps, a bustling metropolis with iconic landmarks.", "United States", "Spring and Autumn", "$$$", "https://images.unsplash.com/photo-1538970272646-f61fabb3a8a2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=790&q=80"),
    TravelDestination("Paris", "Known as the city of love, with stunning architecture and world-renowned cuisine.", "France", "Spring", "$$$", "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1773&q=80"),
    TravelDestination("Sydney", "Famous for its harbourfront Sydney Opera House and vibrant arts scene.", "Australia", "Spring and Autumn", "$$$", "https://images.unsplash.com/photo-1624138784614-87fd1b6528f8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1933&q=80"),
]

class CountryData:
    def __init__(self, name, image, capital, language, currency, population):
        self.name = name
        self.image = image
        self.capital = capital
        self.language = language
        self.currency = currency
        self.population = population


countries = [
    Country("United States", "https://www.countryflags.com/wp-content/uploads/united-states-of-america-flag-png-large.png" , "Washington D.C.", "English", "USD", 331449281),
    Country("United Kingdom","https://www.countryflags.com/wp-content/uploads/united-kingdom-flag-png-large.png", "London", "English", "GBP", 66650000),
    Country("France","https://www.countryflags.com/wp-content/uploads/france-flag-png-large.png","Paris", "French", "EUR", 67060000),
    Country("Japan","https://www.countryflags.com/wp-content/uploads/japan-flag-png-large.png", "Tokyo", "Japanese", "JPY", 126500000),
    Country("Canada","https://www.countryflags.com/wp-content/uploads/canada-flag-png-large.png", "Ottawa", "English and French", "CAD", 37742154),
    Country("Australia","https://www.countryflags.com/wp-content/uploads/flag-jpg-xl-9-2048x1024.jpg","Canberra", "English", "AUD", 25600000)
]
