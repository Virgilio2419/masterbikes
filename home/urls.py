from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('preguntas_frecuentes/', preguntas, name='preguntas_frecuentes'), 
]
