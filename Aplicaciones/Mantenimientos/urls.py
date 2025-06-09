#configuracion de rutas
from django.urls import path
from . import views
urlpatterns=[
    path('mantenimientos/', views.inicioMantenimientos, name='inicio_mantenimientos'),
    path('mantenimientos/nuevo/', views.nuevoMantenimiento, name='nuevo_mantenimiento'),
    path('mantenimientos/guardar/', views.guardarMantenimiento, name='guardar_mantenimiento'),
    path('mantenimientos/editar/<int:id>/', views.editarMantenimiento, name='editar_mantenimiento'),
    path('mantenimientos/actualizar/<int:id>/', views.procesarEdicionMantenimiento, name='procesar_edicion_mantenimiento'),
    path('mantenimientos/eliminar/<int:id>/', views.eliminarMantenimiento, name='eliminar_mantenimiento'),
]