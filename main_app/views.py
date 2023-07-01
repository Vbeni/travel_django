from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView



class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

class CountryList(TemplateView):
    template_name = "country_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = countries
        return context


class Country:
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
