from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
<<<<<<< HEAD
    path('preguntas_frecuentes/', preguntas, name='preguntas_frecuentes'),
    path('tienda',tienda, name='tienda'), 
=======
    path('preguntas_frecuentes/', preguntas, name='preguntas_frecuentes'), 
    path('logout/',exit,name='exit'),
    
>>>>>>> main
]
