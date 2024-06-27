
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('servicio/',servicio,name='servicio'),
    path('elimina/<str:pk>',elimina,name='elimina'),
    path('editar_servicio/<str:pk>/',editar_servicio,name='editar_servicio'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)