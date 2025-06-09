from django.urls import path
from . import views
urlpatterns=[
    path('', views.inicioI),
    path('nuevaImpresora/', views.nuevaImpresora),
    path('guardarImpresora/', views.guardarImpresora),
    path('editarImpresora/<int:id>/', views.editarImpresora),
    path('procesarEdicionImpresora/<int:id>/', views.procesarEdicionImpresora),
    path('eliminarImpresora/<int:id>/', views.eliminarImpresora),
]