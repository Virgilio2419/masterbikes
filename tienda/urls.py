
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', tienda, name='tienda'),
    path('venta/', venta, name='venta'), 
    path('agregar_venta/', agregar_venta, name='agregar_venta'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)