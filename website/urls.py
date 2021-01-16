from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name="website-home"),
    path('guide/', views.guide,name="website-guide"),
    path('contact/', views.contact,name="website-contact"),
    path('about/', views.about,name="website-about"),
    path('plot/', views.plotx,name="website-plot"),
    path('category/<str:cats>', views.CategoryView, name="category"),
    path('article/<int:id>',views.detail,name = "detail"),


]