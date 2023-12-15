from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('category/<slug>', category, name='category'),
    path('single/<slug>', single, name='single'),
]
