<<<<<<< HEAD

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ventas, name='tienda'),
    path('crear-venta/', crear_venta, name='crear_venta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
from django.urls import path
from .views import *

urlpatterns = [
    path('tienda',tienda, name='tienda'), 
]
>>>>>>> c947925fef88a9d68fd6afb7d45e37420187ac7e
