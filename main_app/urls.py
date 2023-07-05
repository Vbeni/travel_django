from django.contrib import admin
from django.urls import path, include 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('countries/', views.CountryList.as_view(), name="country_list" ),
    path('destinations/', views.TravelDestinationList.as_view(), name="travel_destinations_list"),
    path('countries/new/', views.CountryCreate.as_view(), name="country_create"),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name="country_detail"),
    path('country/<int:pk>/update',views.CountryUpdate.as_view(), name="country_update"),
    path('country/<int:pk>/delete',views.CountryDelete.as_view(), name="country_delete"),
    path('countries/<int:pk>/destinations/new/', views.DestinationCreate.as_view(), name="destination_create"),
    path('itineraries/<int:pk>/destinations/<int:destination_pk>/', views.ItineraryDestinationAssoc.as_view(), name="itinerary_destination_assoc"),


]
