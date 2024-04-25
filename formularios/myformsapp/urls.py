from django.urls import path
from . import views

#app_name = 'myformsapp'  # Nombre de la aplicación

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),  # Ruta para la página de inicio
    path('pagina_confirmacion/', views.pagina_confirmacion, name='pagina_confirmacion'), # Ruta para la página contactanos
    path('nueva-pagina/', views.nueva_pagina, name='nueva_pagina'), 
]
