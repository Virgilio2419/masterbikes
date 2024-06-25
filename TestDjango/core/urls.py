from django.urls import path
from .views import *

urlpatterns = [
	path('', inicio, name="inicio"),
	path('lista', lista, name="lista"),
 	path('elimina/<str:pk>', elimina, name="elimina"),
  	path('agrega', agrega, name="agrega"),
   	path('nuevo', nuevo, name="nuevo"),
    path('modificar/<str:pk>/', modificar, name="modificar"),
]