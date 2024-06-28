
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('servicio/',servicio,name='servicio'),
    path('elimina/<str:pk>',elimina,name='elimina'),
    path('editar_servicio/<str:pk>/',editar_servicio,name='editar_servicio'),
    path('agrega_servicio/',agrega_servicio,name='agrega_servicio'),
    path('agrega_cliente/',agrega_cliente,name='agrega_cliente'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)