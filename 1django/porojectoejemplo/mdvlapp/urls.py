from django.urls import path
from .views import saludar, nuevococinero, consultarpedido,redes

urlpatterns = [
    path('hola/',saludar),
    path('nuevo/',nuevococinero),
    path('pedido/',consultarpedido),
    path('redes/',redes),