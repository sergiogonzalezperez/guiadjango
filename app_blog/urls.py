from django.urls import path
from . import views  # Importa las vistas de esta misma app

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz de la app
]