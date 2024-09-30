from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('county_weather/', views.county_weather, name='county_weather'),
    path('weather_graph/', views.weather_graph, name='weather_graph'),
    path('weather_api/', views.weather_api, name='weather_api'),
]