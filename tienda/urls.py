from django.urls import path
from .views import *

urlpatterns = [
    path('tienda',tienda, name='tienda'), 
]
