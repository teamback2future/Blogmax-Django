from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name="website-home"),
    path('contact/', views.contact,name="website-contact"),
    path('about/', views.about,name="website-about"),


]