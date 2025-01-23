from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),
    path('profile/', views.profile, name='profile'),
]