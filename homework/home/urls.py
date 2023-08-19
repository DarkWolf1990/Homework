from django.contrib import admin
from django.urls import path
import home.views as homeapp

app_name = 'homeapp'

urlpatterns = [
    path('', homeapp.get_page, name='get_page'),
    path('accommodation_details/<int:pk>/', homeapp.accommodation, name='accommodation'),

]
