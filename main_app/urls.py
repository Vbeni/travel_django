from django.contrib import admin
from django.urls import path, include 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('countries/', views.CountryList.as_view(), name="country_list" )
]
