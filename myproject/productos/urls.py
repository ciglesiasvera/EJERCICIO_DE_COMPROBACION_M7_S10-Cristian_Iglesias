from django.urls import path
from .views import producto_list, registrar_producto, mostrar_username

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('registrar/', registrar_producto, name='registrar_producto'),
    path('productos/', producto_list, name='producto_list'),
    path('producto/username/<str:cadena>/', mostrar_username, name='mostrar_username'),
]